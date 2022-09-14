import socket
import threading # for threading 

# socket info 
HOST = 'localhost'
PORT = 8888
global account 
account = 1000
error = "Yoo are Enter value larger than "
msg = "   Done   "


   
def req_thread( client , address):
      print("----------------------------------") 
   
   
      data_user = client.recv( 1024 ).decode( )
      print("Received :", repr(data_user))

   
      if ("" != data_user):
          reply = "of User information"
          client.send(reply.encode('utf-8'))
    
    
      data_passwd = client.recv( 1024 ).decode()
      print("Received :", repr(data_passwd))
      # Send data to client in utf-8
      if ("" != data_passwd):
         reply = "of Password "
         client.send(reply.encode('utf-8'))
    
      data_tran = client.recv( 1024 ).decode(  )
      print("Received :", repr(data_tran))
      # Send data to client in utf-8
      if ('' != data_tran ):
          reply = "of transaction "
          client.send(reply.encode('utf-8'))
    
    
      data_amount = int(client.recv( 1024 ).decode( ))
      print("Received :", repr(data_amount))
      # Send data to client in utf-8
      if ( data_amount != ''):
          reply = "of Amount "
          client.send(reply.encode('utf-8'))
    
    
      if data_user.lower() == 'moh' and data_passwd.lower() == '1234' :
         if data_tran.lower().rstrip() == "deposit" : 
            deposit(data_amount,account,client)
         elif data_tran.lower().rstrip() == "withdraw" : 
            withdraw(data_amount,account,client)
         elif data_tran.lower().rstrip() == 'inquery':
            inquery(data_amount,account,client) 
         else:
            reply = "Enter Valid Transaction "
            client.send(reply.encode('utf-8'))
      else :
           reply = "Enter Valid Cradintials "
           client.send(reply.encode('utf-8'))

   
      client.close()
   

# deposit function
def deposit(data_amount,account,client): 
    account = data_amount + account
    client.send(str(account).encode('utf-8'))
    print(account)
   
   
# withdraw function
def withdraw(data_amount,account,client): 
     account =  account - data_amount
     client.send(str(account).encode('utf-8'))
     print(account)
    
# inqusery function
def inquery(data_amount,account,client):
    return client.send(str(account).encode('utf-8'))
    
     
        



# main function 
def main():
# Server loop
  
     

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen() # Number of connections
    print("[+] listening on {} #####".format(s.getsockname()))
    print("[+] Wating Clint to send ####")
    # Accept connections
    
    while True:
       client , address = s.accept()
       print("Active Connection" , threading.activeCount()-1)
       print("Connected to", address)
       thread = threading.Thread(target=req_thread , args=(client , address))
       thread.start()
       
    
     
     
if __name__ == '__main__':
   main()