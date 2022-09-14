import socket
import os 
from cryptography.fernet import Fernet # for sysmetric encrption 
# socket info 
HOST = 'localhost'
PORT = 8008
account = 1000
error = "Yoo are Enter value larger than "
msg = "   Done   "



for i in os.listdir():
    if i == "key.pem":
       continue 
    else :            
       # symtric key generation               
       key=Fernet.generate_key()
     
       # Add key to the file 
       with open('key.pem','wb') as keyf :
          keyf.write(key)
          

with open('key.pem','rb') as fff: 
           key = fff.read()
           print("The Client/Server Shared Secret Key : " ,key)
#Fernet(key).decrypt(content)

# socket error handling 

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((HOST, PORT))
  s.listen(5) # Number of connections
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


# deposit function
def deposit(data_amount,account,client): 
    account = int(Fernet(key).decrypt(data_amount).decode('utf-8')) + account
    client.send(str(account).encode('utf-8'))
    print(account)
   
   
# withdraw function
def withdraw(data_amount,account,client): 
      account =  account - int(Fernet(key).decrypt(data_amount).decode('utf-8'))
      client.send(str(account).encode('utf-8'))
      print(account)
   
# inqusery function
def inquery(data_amount,account,client):
    return client.send(str(account).encode('utf-8'))
    
     
        
print("[+] listening on {} #####".format(s.getsockname()))
print("[+] Wating Clint to send ####")


# main function 
def main():
# Server loop
  while True:
     
     with open('key.pem','rb') as fff: 
           keyr = fff.read()
          
     
     # Accept connections
     client , address = s.accept()
     print("Connected to", address)
     
  
     
     # Receive data and decode using utf-8
     data_user = client.recv( 1024 )
     print("Received :", repr(data_user))

     # Send data to client in utf-8
     if ("" != data_user):
         reply = "of User information"
         client.send(reply.encode('utf-8'))
    
     # Receive data and decode using utf-8
     data_passwd = client.recv( 1024 )
     print("Received :", repr(data_passwd))
     # Send data to client in utf-8
     if ("" != data_passwd):
        reply = "of Password "
        client.send(reply.encode('utf-8'))
    
     data_tran = client.recv( 1024 )
     print("Received :", repr(data_tran))
     # Send data to client in utf-8
     if ('' != data_tran ):
         reply = "of transaction "
         client.send(reply.encode('utf-8'))
    
    
     data_amount = client.recv( 1024 )
     print("Received :", repr(data_amount))
     # Send data to client in utf-8
     if ( data_amount != ''):
         reply = "of Amount "
         client.send(reply.encode('utf-8'))
    
    
     if Fernet(key).decrypt(data_user).decode('utf-8') == 'moh' and Fernet(key).decrypt(data_passwd).decode('utf-8') == '1234' :
        
        if  Fernet(key).decrypt(data_tran).decode('utf-8') == "deposit" : 
           deposit(data_amount,account,client)
        elif  Fernet(key).decrypt(data_tran).decode('utf-8')== "withdraw" : 
           withdraw(data_amount,account,client)
        elif  Fernet(key).decrypt(data_tran).decode('utf-8') == 'inquery':
           inquery(data_amount,account,client) 
        else:
           reply = "Enter Valid Transaction "
           client.send(reply.encode('utf-8'))
     else :
          reply = "Enter Valid Cradintials "
          client.send(reply.encode('utf-8'))
     
     client.send(str.encode(msg))
     
if __name__ == '__main__':
   main()