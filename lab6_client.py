import time
import math
from time import perf_counter
import grpc
import sys
import lab6_m_pb2
import lab6_m_pb2_grpc
import numpy as np
from PIL import Image
import io

def doMath(stub):
  a = 15
  b = 5
  number = lab6_pb2.AddMsg(a=a,b=b)
  response = stub.GetAddMsg(number)
  #print(response)

def doImg(stub):
  img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
  data = lab6_m_pb2.ImageMsg(img=img)
  response = stub.GetImgMsg(data)
  #print(response)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    addr = sys.argv[1]
    method = sys.argv[2]#'localhost:50051'
    b = sys.argv[3] 
    with grpc.insecure_channel(str(addr)) as channel:
      stub = lab6_m_pb2_grpc.lab6Stub(channel)
      if method =='add':
          
          print("-------------- Add --------------")
          times = 0
          bound = int(b)
          for x in range(0,bound):
            start = perf_counter()
            doMath(stub)
            stop = perf_counter()
            times += (stop-start)
          print("average add time is", times/bound )
      else:
        print("-------------- Img --------------")
        times = 0
        bound = int(b)
        for x in range(0,bound):
          start = perf_counter()
          doImg(stub)
          stop = perf_counter()
          times += (stop-start)
        print("average img time is", times/bound )
        
        
        


if __name__ == '__main__':
    #logging.basicConfig()
    run()
