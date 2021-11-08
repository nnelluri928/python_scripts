#!/usr/bin/env python3

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(levelname)s')


file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#logging.basicConfig(filename='sample.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(levelname)s')


def add(x,y):
  return x+y


def suntract(x,y):
  return x-y

def multiply(x,y):
  return x*y


def devide(x,y):
  return x/y


num_1=20
num_2=10

add_result = add(num_1,num_2)
logger.info("Add: {} + {} = {}".format(num_1,num_2,add_result))

sub_result = suntract(num_1,num_2)
logger.info("Sub: {} - {} = {}".format(num_1,num_2,sub_result))

mul_result = multiply(num_1,num_2)
logger.info("Mul: {} * {} = {}".format(num_1,num_2,mul_result))

dev_result = devide(num_1,num_2)
logger.info("Dev: {} / {} = {}".format(num_1,num_2,dev_result))

