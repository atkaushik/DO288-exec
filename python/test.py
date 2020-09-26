
import time
import socket
def host_IP():
   try:
      hname = socket.gethostname()
      hip = socket.gethostbyname(hname)
      print("Hostname:  ",hname)
      print("IP Address: ",hip)
   except:
      print("Unable to get Hostname and IP")
# Driver code
i=2
while i > 1:
   host_IP() #Function call
   time.sleep (2)
