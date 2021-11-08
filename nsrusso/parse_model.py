#!/usr/bin/env python



import re


def parse_model_ios():

  text = "cisco CSR1000v (VXE) processor (revision VXE) with 31/32K memory"

  pattern = re.compile(r"cisco\s+(?P<model>\S+)\s+\(\S+\)\s+processor\s+")

  model_match = pattern.search(text)
  
  if model_match:
    return model_match.group("model")
  print("no match found") 
  return None


def parse_model_iosxr():

  text = " PID		: R-IOSXRV9000-RP_C"


  #model_regex = re.compile(r"\s+PID\s+:[ \t]+(?P<model>\S+)")
  model_regex = re.compile(r"\s+PID\s+:\s+(?P<model>\S+)")

  model_match = model_regex.search(text)

  if model_match:
    return model_match.groupdict()
  return None



def main():

  print(parse_model_ios())
  print(parse_model_iosxr())


if __name__ == "__main__":
  main()
