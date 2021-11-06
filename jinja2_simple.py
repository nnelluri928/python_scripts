#!/usr/local/bin/python3

from __future__ import print_function ,unicode_literals
import jinja2


bgp_vars = {

"peer1_ip":"10.255.255.2",
"peer1_as":"20",
"local_as":"10",
"advertiosed_route1":"10.10.200.0/24",
"advertiosed_route2":"10.10.201.0/24",
"advertiosed_route3":"10.10.202.0/24"

}


with open('nxos_bgp.j2') as f:
  bgp_template = f.read()

template = jinja2.Template(bgp_template)

print(template.render(bgp_vars))


