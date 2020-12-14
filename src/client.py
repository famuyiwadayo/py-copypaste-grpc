from __future__ import print_function
import logging

import grpc

import paste_pb2_grpc as pb2_grpc
import paste_pb2 as pb2

from uuid import uuid4
import time


def receivePaste(stub):
    """
    docstring
    """

    receiverId = str(uuid4())

    request = pb2.ByReceiver(receiver=receiverId)
    pastes = stub.ReceivePaste(request)

    print(f'Your ID is: {receiverId}')

    # def toStr(paste):
    #     return (f'\n\ncontent= {paste.content}\nreceiver= {paste.receiver}\nsender= {paste.sender}\ntimestamp= {paste.timestamp}\nid= {paste.id}\n\n')

    # try:
    # while True:
    for paste in pastes:
        print(f"< {paste.sender} > sent a paste\n")
        print(f"Content is: \n {paste.content} \n")
        # time.sleep(0.5)
    # except Exception:
    #     print('An unexpected error occured!')


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.PasteServiceStub(channel)
        receivePaste(stub=stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
