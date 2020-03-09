# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:07:45 2020
@author: Andreas
"""

# Check whether the tensorflow works
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())