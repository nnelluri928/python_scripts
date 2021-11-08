#!/usr/bin/env python3
import os


def print_filename(dirname):
  all_filenames = os.listdir(dirname)
  
  for one_filename in all_filenames:
    print(one_filename)


print_filename("/etc")

