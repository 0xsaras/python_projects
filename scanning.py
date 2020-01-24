import socket
import subprocess   #to run system commands
import sys
import os
from datetime import datetime

# Clearing the screen
subprocess.call(['clear'])


# taking input 
remote_ser    = input("Enter  remote host to scan : ")
remoteSer_IP  = socket.gethostbyname(remote_Ser)

print ("Please wait, scanning remote host", remoteServerIP)


# time that scan starts
t1 = datetime.now()

# function will scans all ports between 1 and 1024)



try:
    for port in range(1,1026):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteser_IP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
            nmapR = (os.popen('nmap -sC -sV -p '+str(port)+" "+remoteSer_IP).read()).split("\n")[5]
            print(nmapR)
        sock.close()

except KeyboardInterrupt:
    print (" Ctrl+C exiting")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

#time that scan stops 

t2 = datetime.now()

# time that attack took
Tot =  t2 - t1

print ('Scanning Completed in: ', Tol)
