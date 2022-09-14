import socket # socket lib
import sys  # sys lib
from colorama import Fore,init # colorama lib for coloring
init()

IP = '127.0.0.1'
PORT = 8888



def banner():
   print(Fore.YELLOW,"""
*********************************************** *
* Coded by :  Oday Abuzaid          2019904091  *
*             Mohammad Obeidat      2019904115  *
*             Majdi Bshara          2019904139  *
*             Thaer Al-shorman      2019904002  *
*********************************************** *           
        """                           
)

banner()

def main():

   
     # Create socket and connect it to server tcp socket 
     try :
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect((IP,PORT))
         print(f"Connected to server ")
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



     print(Fore.RED,"")
     user = input("Enter your Username : ")
     s.send(str.encode(user))
     print("Awaiting the reply...")
     reply = s.recv( 1024 ).decode( 'utf-8' )
     print("Received ", str(reply))
     
     passwd = input("Enter your passwd : ")
     s.send(str.encode(passwd))
     print("Awaiting the reply...")
     reply = s.recv( 1024 ).decode( 'utf-8' )
     print("Received ", str(reply))
     
     tran = input("Enter your TRansaction : ")
     s.send(str.encode(tran))
     print("Awaiting the reply...")
     reply = s.recv( 1024 ).decode( 'utf-8' )
     print("Received ", str(reply))
     
     amount = input("Enter your TRansaction : ")
     s.send(str.encode(amount))
     print("Awaiting the reply...")
     reply = s.recv( 1024 ).decode( 'utf-8' )
     print("Received ", str(reply))
     
     
     if  user == '' or passwd == '' or  tran == ''  or amount  == '' :
         quit()
    
if __name__ == '__main__': 
     
         main()
