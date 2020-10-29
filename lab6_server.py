import time
import math
import numpy as np
from PIL import Image


import grpc

from concurrent import futures

# import lab6_pb2
# import lab6_pb2_grpc
import lab6_m_pb2
import lab6_m_pb2_grpc
import add
import size
#import jsonpickle
import numpy as np
from PIL import Image
import io

class lab6Servicer(lab6_m_pb2_grpc.lab6Servicer):
  def GetAddMsg(self, request, context):
    response = lab6_m_pb2.Sum()
    response.s = add.addxy(request.a, request.b)
    return response
  def GetImgMsg(self, request, context):
    response = lab6_m_pb2.Size()
    response.width, response.height = add.ssize(request.img)
    #response_pickled = jsonpickle.encode(response)
    return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lab6_m_pb2_grpc.add_lab6Servicer_to_server(
        lab6Servicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    #logging.basicConfig()
    serve()


