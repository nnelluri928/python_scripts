#!/usr/bin/env python3

import jinja2


advertised_routes = ["10.10.200.0/24", "10.10.201.0/24", "10.10.202.0/24"]

bgp_vars = {
	"local_as": 10,
	"peer1_ip": "10.255.255.2",
	"peer1_as": 20,
	"peer1_ipv6": True,
	"advertised_routes": advertised_routes
	}

template_file = "nxos-bgp-template.j2"
with open(template_file) as f:
  bgp_template = f.read()

template = jinja2.Template(bgp_template)

print(template.render(bgp_vars))

