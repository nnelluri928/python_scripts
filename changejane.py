#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1],"r") as file:
  

  for line in file.readlines():
  
    old_string = line.strip()
    new_string = old_string.replace("jane","jade")
    subprocess.run(["mv","/Users/nnelluri/data/" + old_string,"/Users/nnelluri/data/" + new_string])



