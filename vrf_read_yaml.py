import yaml



from pprint import pprint

with open("my_vrf.yml") as f:
  output = yaml.load(f)


pprint(output)

