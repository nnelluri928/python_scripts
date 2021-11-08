#!/usr/local/bin/python3

import paramiko
import time


def send_cmd(conn,cmd):

  conn.send(cmd + "\n")
  time.sleep(1.0)



def get_output(conn):

  return  conn.recv(65535).decode("utf-8")



def main():


  R1 = "172.29.207.8"
  R2 = "172.29.207.9"

  host_dict = {
	R1 : "show running-config | sec vrf",
	R2 : "show running-config vrf management"
	}


  for hostname,vrf_cmd in host_dict.items():
    
    conn_params = paramiko.SSHClient()
    conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    conn_params.connect(hostname = hostname,port = 22,username = 'admin', password = 'insieme' ,look_for_keys=False,allow_agent=False)

    conn=conn_params.invoke_shell()
    time.sleep(1.0)
    

    #print(f"Loogged in to the {get_output(conn).strip()} successfully")


    commands = [
	"terminal length 0",
	"show version | in image",
	vrf_cmd.upper()
	]

    conn_output = ""
    for cmd in commands:

      breakpoint()
      send_cmd(conn,cmd)
      #print(get_output(conn))
      conn_output += get_output(conn)
   
    conn.close()
    
    print(f"writing {hostname} facts to file")
    with open(f"{hostname}_facts.txt","w") as handle:
      handle.write(conn_output)


if __name__ == "__main__":

  main()





