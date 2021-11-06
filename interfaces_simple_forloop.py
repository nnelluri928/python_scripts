#!/usr/local/bin/python3
  

import jinja2
import sys
import yaml
#from jinja2 import Environment, FileSystemLoader, jinja2

# Initialize the Jinja2 environment to load templates
# from the current directory
#env = Environment(loader=FileSystemLoader('.'))
#template = env.get_template(sys.argv[1])

with open(sys.argv[1]) as f:
  intf_template = f.read()

template = jinja2.Template(intf_template)

# Load the context YAML file into a Python dictionary
with open(sys.argv[2], 'r') as datafile:
    context = yaml.load(datafile)

# Render the template and print the resulting document
rendered_template = template.render(**context)
print(rendered_template)
