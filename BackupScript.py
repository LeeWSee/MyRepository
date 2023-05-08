#!/usr/bin/python3
import subprocess, sys, time, multiprocessing

class BackupScript(): #automatically copy files from /root/Desktop/Programms/synkthing/ to special folder with name like "backup-YYYY:MM:DD-hh-mm-ss" and path /root/Desktop/Programms/backups/
    def __init__(self):
        print("Please, ensure you have activated syncthing on your device") #before executing BackupScript you should start yncthing on your device
        self.command = str(input("Do you want to proceed? [y/n] "))
        if self.command == 'y':
            self.border()
            self.exchange()
            self.execution()
            self.cheking_result()
        else:
            sys.exit


    def border(self):
        print("--------------------------------------")
    
    
    def exchange(self): #starting exchange between devices
        self.syncthing_start_process = multiprocessing.Process(target=self.syncthing_start, args=()) #creating new process for "start syncthing" programm
        self.syncthing_start_process.start()
        time.sleep(60)

    
    def syncthing_start(self):
        subprocess.run(["/usr/bin/syncthing", "serve", "--no-browser", "--logfile=default"]) #"start syncthing" launch

        
    def execution(self):
        self.source_directory = "/root/Desktop/Programms/synkthing/" #source folder's path
        self.backup_directory = "/root/Desktop/Programms/backups/" #backups folder's path

        self.current_date = subprocess.check_output("date +%Y:%m:%d-%H:%M:%S", shell=True).decode().replace("\n", "") #receiving curent date and time from system
        self.backup_directory_name = "backup-" + self.current_date #creating name for new backup with "backup-YYYY:MM:DD-hh-mm-ss" pattern
        
        subprocess.run(["cp", "-r", self.source_directory, self.backup_directory]) #copying files from source to new backup folder
        subprocess.run(["mv", self.backup_directory + "synkthing/", self.backup_directory + self.backup_directory_name]) #renaming new backup folder from "synkthing" to "backup-YYYY:MM:DD-hh-mm-ss"


    def cheking_result(self):
        result_backup = subprocess.check_output("ls " + self.backup_directory + self.backup_directory_name, shell=True).decode().split() #creating array with files and folders from new backup folder
        result_source = subprocess.check_output("ls " + self.source_directory, shell=True).decode().split() #creating array with files and folders from source folder

        for title in result_source: #cheking that files and folers from source and new backup match
            if title in result_backup:
                pass
            else:
                self.border()
                print("[-] Something went wrong")
                self.syncthing_start_process.terminate() #"start syncthing" terminating
                sys.exit
        self.border()
        print("[+] The backup was successful")
        self.syncthing_start_process.terminate() #"start syncthing" terminating
        sys.exit
        
            
backup = BackupScript()

