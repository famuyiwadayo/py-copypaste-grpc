import grpc
from concurrent import futures
import time
import paste_pb2_grpc as pb2_grpc
import paste_pb2 as pb2
import datetime
import logging
from uuid import uuid4
from session import Memory as MemorySession

from pymongo import MongoClient
from bson.json_util import loads, dumps

_ONE_DAY = datetime.timedelta(days=1)
_LOGGER = logging.getLogger(__name__)

client = MongoClient(
    'mongodb+srv://daniel:famuyiwa@cluster0.a36yi.mongodb.net/copypaste-db?retryWrites=true&w=majority')


class Paste(pb2_grpc.PasteServiceServicer):

    def __init__(self, session_impl):
        self._session = session_impl
        self.db = client['copypaste-db']

    def createPaste(self, paste: pb2.PasteDTO):
        db = client['copypaste-db']
        data = {
            **paste,
            'timestamp': str(datetime.datetime.now())
        }
        result = db.pastes.insert_one(data)
        # print(dumps(result))

    def SendPaste(self, request, context):
        # receiver = request.receiver

        # if not self._session.has(receiver):
        #     raise ValueError('invalid session')

        # message = {
        #     'id': str(uuid4()),
        #     'timestamp': str(time.time()),
        #     'content': request.content,
        #     'receiver': request.receiver,
        #     'sender': request.sender
        # }

        self.createPaste({'content': request.content,
                          'receiver': request.receiver,
                          'sender': request.sender
                          })

        # self._session.append_unread_message(receiver, message)

        # print(request)

        return pb2.EMPTY()

    # def ReceivePaste(self, request, context):
    #     receiver = request.receiver
    #     print(f'< {receiver} > is now connected')

    #     if not self._session.has(receiver):
    #         # raise ValueError('invalid session')
    #         self._session.initialize(receiver)

    #     while True:
    #         for message in self._session.pop_unread_messages(receiver):
    #             print(message)
    #             yield pb2.Paste(
    #                 _id=message['_id'],
    #                 timestamp=message['timestamp'],
    #                 content=message['content'],
    #                 receiver=message['receiver'],
    #                 sender=message['sender']
    #             )

    def ReceivePaste(self, request, context):
        receiver = request.receiver
        print(f'< {receiver} > is now connected')

        pipeline = [
            {'$match': {'operationType': {'$in': ['insert']}}},
            {'$match': {'fullDocument.receiver': receiver}},
        ]
        stream = self.db.watch(pipeline=pipeline)

        for paste in stream:
            doc = loads(dumps(paste))
            fullDoc = doc['fullDocument']
            _id = fullDoc['_id']
            print(f'paste from stream:: {fullDoc} \n\n type:: {type(doc)}')
            yield pb2.Paste(
                _id=str(fullDoc['_id']),
                content=fullDoc['content'],
                receiver=fullDoc['receiver'],
                sender=fullDoc['sender'],
                timestamp=fullDoc['timestamp']
            )


def _wait_forever(server):
    try:
        while True:
            time.sleep(_ONE_DAY.total_seconds())
    except KeyboardInterrupt:
        server.stop(None)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_PasteServiceServicer_to_server(Paste(MemorySession()), server)
    server.add_insecure_port('[::]:50051')
    print('Paste RPC server started ⛑')
    server.start()
    _wait_forever(server)


if __name__ == '__main__':
    serve()
