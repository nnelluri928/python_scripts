#!/usr/bin/env python
import re
from pprint import pprint

int_cfg = '''
interface Ethernet1/1
  description "server port1"
  Speed 10000
  Shutdown

interface Ethernet1/2
  description "server port2"
  Speed 40000
  Shutdown
  '''


int_match = re.findall(r"(interface\s+Ethernet[0-9]/[0-9])",int_cfg)
dec_match = re.findall(r"description\s+(\S+\s+\S+)",int_cfg)
speed_match = re.findall(r"Speed\s+(\d+)",int_cfg)


int_dict = {int_match:{"description":dec_match,"speed":speed_match} for int_match,dec_match,speed_match in zip(int_match,dec_match,speed_match)}

pprint(int_dict)



