#!/usr/bin/env python3

import numpy as np
from PIL import Image
import io

def ssize (imgg):
  import io
  ioBuffer = io.BytesIO(imgg)
  img = Image.open(ioBuffer)
  return img.size[0], img.size[1]
