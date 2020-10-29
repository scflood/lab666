#!/usr/bin/env python3
import io
import math
import numpy as np
from PIL import Image

def addxy(a , b):
  return a+b

def ssize (imgg):
  ioBuffer = io.BytesIO(imgg)
  img = Image.open(ioBuffer)
  return img.size[0], img.size[1]
