#!/usr/bin/env python3

import re
import csv
import operator
per_user = {}
error = {}


with open('syslog.log') as file:
  for line in file:
    if "INFO" or "ERROR" in line:
      match = re.search(r"INFO .* \((\S+)\)",line)
      match_err = re.search(r"ERROR .* \((\S+)\)",line)
      

      if match is not None:
        if match.group(1) not in per_user:
          per_user[match.group(1)] = {'INFO':1,'ERROR':0}
        else:
          per_user[match.group(1)]['INFO'] +=1
      if match_err is not None:
        if match_err.group(1) not in per_user:
          per_user[match_err.group(1)] = {'INFO':0,'ERROR':1}
        else:
          per_user[match_err.group(1)]['ERROR'] += 1

 
      new_match = re.search(r"ticky: ERROR ([\w ]*)",line)
      if new_match is not None:
        if new_match.group(1) not in error:
          error[new_match.group(1)] = 1
        else:
           error[new_match.group(1)] += 1
 
  per_user = sorted(per_user.items(),key = operator.itemgetter(0))
          
  error = sorted(error.items(),key = operator.itemgetter(1),reverse=True)

  error.insert(0,("Error","Count"))
  per_user.insert(0,("UserName","INFO","ERROR"))



def make_row(elements):
  row = list()
  for obj in elements:
    if isinstance(obj,dict):
      row += obj.values()
    else:
      row.append(obj)
  return row


with open("user_statistics.csv","w") as file:
  writer = csv.writer(file)
  for row in per_user:
    writer.writerow(make_row(row))


with open("error_message.csv","w") as file:
  
  writer = csv.writer(file)
  writer.writerows(error)


