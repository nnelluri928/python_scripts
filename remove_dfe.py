




with open("Test.cfg") as file:
  output = file.readlines()




for line in output:
  if "dfe" in line:
    continue
  with open("Test1.cfg", "a") as new:
    new.write(line)



