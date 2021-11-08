#!/usr/bin/env python3
import sys

def pytail(args):
    
    with open(args[0],"r") as file:
        if len(args) > 1:
            lines = file.readlines()[-int(args[1]):]
        else:
            lines = file.readlines()[-10:]


    for line in lines:
        print(line.strip())


pytail(sys.argv[1:])



