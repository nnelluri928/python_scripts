#!/usr/bin/env python3
import glob
from os.path import join
from pprint import pprint

def apply_func_to_dir(dirname, func):


  output = {}

  for one_filename in glob.glob(join(dirname, '*')):
  
    output[one_filename] = func(one_filename)
  return output


pprint(apply_func_to_dir('/etc',len))
