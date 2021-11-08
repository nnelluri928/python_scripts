#!/usr/bin/env python3



import time
from datetime import datetime


def display_time(time_to_print=datetime.now()):


  time_to_print = datetime.now()
  print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))


print(display_time.__defaults__)
display_time()
time.sleep(1)
display_time()
time.sleep(1)

