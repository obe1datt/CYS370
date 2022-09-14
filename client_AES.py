import socket # socket lib
import sys  # sys lib
from cryptography.fernet import Fernet # for sysmetric encrption 
from colorama import Fore,init # colorama lib for coloring
import os
init()

print(Fore.YELLOW,"""
  /$$$$$$  /$$$$$$$$ /$$      /$$
 /$$__  $$|__  $$__/| $$$    /$$$
| $$  \ $$   | $$   | $$$$  /$$$$
| $$$$$$$$   | $$   | $$ $$/$$ $$
| $$__  $$   | $$   | $$  $$$| $$
| $$  | $$   | $$   | $$\  $ | $$
| $$  | $$   | $$   | $$ \/  | $$
|__/  |__/   |__/   |__/     |__/   

*********************************************** *
* Coded by :  Mohammad Qeis Obeidat 2019904115  *
*             Majdi Bashara         2019904139  *
*             Oday Abuzaid          2019904091  *
*             Thaer Al-shorman      2019904002  *
*********************************************** *           
        
All Rights Recieved 2022 
"""                           
)


for i in os.listdir():
     if i == 'key.pem':
        with open('key.pem','rb') as fff: 
           key = fff.read()
           print("The Client/Server Shared Secret Key : " ,key)
     else:
         continue 


           
# Fernet(key).encrypt(content)



# socket Error handling 
try:
     # Create socket and connect it to server tcp socket 
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect(('localhost',8008))
except socket.error:
   print("Error in socket Creation")
except socket.herror :
   print("Error in socket Creation") 
except socket.gaierror:
   print("Error in socket Creation") 
except socket.timeout:
   print("Error in socket Creation") 
except OSError :
   print("Error in socket Creation") 




           


# mian function 

def main():

  try :
    print(Fore.RED,"")
    user = Fernet(key).encrypt(sys.argv[1].encode())
    s.send(user)
    print("Awaiting the reply...")
    reply = s.recv( 1024 ).decode( 'utf-8' )
    print("Received ", str(reply))
    
    passwd = Fernet(key).encrypt(sys.argv[2].encode())
    s.send(passwd)
    print("Awaiting the reply...")
    reply = s.recv( 1024 ).decode( 'utf-8' )
    print("Received ", str(reply))
    
    tran =  Fernet(key).encrypt(sys.argv[3].encode())
    s.send(tran)
    print("Awaiting the reply...")
    reply = s.recv( 1024 ).decode( 'utf-8' )
    print("Received ", str(reply))
    
    amount = Fernet(key).encrypt(sys.argv[4].encode())
    s.send(amount)
    print("Awaiting the reply...")
    reply = s.recv( 1024 ).decode( 'utf-8' )
    print("Received", str(reply))
    
    reply1 = s.recv( 1024 ).decode( 'utf-8' )
    print("Received", str(reply1))
    
    #reply2 = s.recv( 1024 ).decode( 'utf-8' )
    #print("Received", str(reply1))
    
    s.close()
  except IndexError :
    print(" Usage Python3 clint.py moh 1234 deposit/withdraw/inqury 400 ")    
   
 
  
if __name__ == '__main__': 
   if len(sys.argv) != 5 :
      print("Usage Python3 clint.py moh 1234 deposit/withdraw/inqury 400 ")
   else:
      main()
