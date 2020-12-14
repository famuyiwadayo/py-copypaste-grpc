from __future__ import print_function
import logging

import grpc

import paste_pb2_grpc as pb2_grpc
import paste_pb2 as pb2

from uuid import uuid4


def sendPaste(stub):

    myId = str(uuid4())

    try:
        while True:
            receiver = input(f'{myId} : Receiver > ')
            text = input(f'{myId} : Content > ')
            request = pb2.PasteDTO(content=text,
                                   receiver=receiver, sender=myId)
            stub.SendPaste(request)
    except KeyboardInterrupt:
        print('\nClient closed')


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.PasteServiceStub(channel)
        sendPaste(stub=stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
