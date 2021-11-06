
import yaml
from pprint import pprint

my_dict = {
  'rtr1': {'bgp_peers': ['20.1.1.1', '20.1.1.2'],
          'device_type': 'jumiper',
          'ip_address': '10.1.1.1',
          'password': 'wahtever',
          'username': 'admin'},
  'rtr2': {'bgp_peers': ['2.1.1.1', '2.2.2.1'],
          'device_type': 'nx_os',
          'ip_address': '10.1.1.122',
          'password': 'wahtever',
          'username': 'admin'}

  }
filename = "outfile.yml"

with open(filename , "w") as f:
  output = yaml.dump(my_dict , f , default_flow_style = True)


