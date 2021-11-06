#!/usr/bin/env python3

import yaml

file_name = "my_devices_dict.yml"

with open(file_name) as f:
  output = yaml.load(f)

print(output)
print(output['rtr1'])
