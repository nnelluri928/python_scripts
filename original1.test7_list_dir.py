#!/usr/bin/env python3

import glob
from os.path import join,isdir


def print_filenames(dirname):

  all_filenames = glob.glob(join(dirname, '*'))
  
  for one_filename in all_filenames:
    if isdir(one_filename):
      print(f"**{one_filename}")
      print(glob.glob(join(one_filename, '*'))) 

    else:
      print(one_filename)
print_filenames('/etc/')
