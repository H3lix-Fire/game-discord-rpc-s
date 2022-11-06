#!/usr/bin/env python
"""Main file used to run program"""

import time
import os
import pypresence
import atexit
import signal

def handle_exit(*args):
    print("\x1b[0m") #Reset to original terminal color upon exiting the program

#Calls the handle_exit function incase of program termination
atexit.register(handle_exit)
signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)

client_id = "1038701147545944105" #Client id, allows this to work so don't change unless you know what you're doing
RPC = pypresence.Presence(client_id)
RPC.connect()

start = int(time.time()) #Sets start time

class colors:
    error = "\x1b[0;31;40m" #Red
    neutral = "\x1b[1;36;40m" #Cyan

class rpc_status:
    def __init__(self):
        self.status = 0

    def set_status(self, status):
        self.status = status

    def run_rpc(self):
        if self.status == "whitespace":
            RPC.update(large_image = "white_space", details="Stuck in white space", state="You've been living here for as long as you can remember.", start=start)
        if self.status == "blackspace":
            RPC.update(large_image = "black_space", details="Stuck in black space", state="You've been living here for as long as you can remember.", start=start)

rpc_status = rpc_status()

os.system("") #Allows setting terminal colors to work
print(colors.neutral) #Sets terminal color

def pick_game(): #Allows user to pick game
    global game #Makes game a global variable

    try:
        game = int(input("1) OMORI\n\ngame: "))
        if game > 0 and game <= 1:
            pass
        else:
            print(f"\n{colors.error}Invalid game{colors.neutral}\n")
            return pick_game()
    except ValueError:
        print(f"\n{colors.error}Please choose a number{colors.neutral}\n")
        return pick_game()
    except KeyboardInterrupt:
        print("\x1b[0m")
        exit()

def pick_status(): #Allows user to pick specific status for game
    global status #Make status a global variable

    try:
        if game == 1:
            status = int(input("1) White Space\n2) Black Space\n\nstatus: "))
            if status == 1:
                rpc_status.set_status("whitespace")
            if status == 2:
                rpc_status.set_status("blackspace")
            else:
                print(f"\n{colors.error}Invalid status{colors.neutral}\n")
                return pick_status()
    except ValueError:
        print(f"\n{colors.error}Please choose a number{colors.neutral}\n")
        return pick_game()
    except KeyboardInterrupt:
        print("\x1b[0m")
        exit()

pick_game()
pick_status()

while(1):
    try:
        rpc_status.run_rpc() #Keeps the rpc running
        time.sleep(15)
    except KeyboardInterrupt: #If keyboard interupt exit
        exit()
    except Exception as e: #If any other exception, ignore it and continue
        print(e)
