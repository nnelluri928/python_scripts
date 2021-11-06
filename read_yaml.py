import yaml
import sys
from pprint import pprint

with open(sys.argv[1]) as f:
  output = yaml.load(f)


pprint(output)

