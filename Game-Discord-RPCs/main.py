#!/usr/bin/env python
"""Main file used to run program"""

from threading import Event
import os
import pypresence
import atexit
import signal

exit = Event()

def handle_exit(*args):
    print("\x1b[0m") #Reset to original terminal color upon exiting the program

#Calls the handle_exit function incase of program termination
atexit.register(handle_exit)
signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)

client_id = "1038701147545944105" #Client id, allows this to work so don't change unless you know what you're doing
RPC = pypresence.Presence(client_id)
RPC.connect()

class colors:
    error = "\x1b[0;31;40m" #Red
    neutral = "\x1b[1;36;40m" #Light Cyan
    answer = "\x1b[0;32;40m" #Green

class rpc_status:
    def __init__(self):
        self.status = 0

    def set_status(self, status):
        self.status = status

    def run_rpc(self):
        try:
            if start == "N":
                start = None
        except UnboundLocalError:
            start = None
        if self.status == "whitespace":
            RPC.update(large_image = "white_space", details="Stuck in white space", state="You've been living here for as long as you can remember.", start=start)
        if self.status == "blackspace":
            RPC.update(large_image = "black_space", details="Stuck in black space", state="You've been living here for as long as you can remember.", start=start)
        if self.status == "bee":
            RPC.update(large_image = "bee", details="Bee", state="bzzzzz", start=start)

rpc_status = rpc_status()

os.system("") #Allows setting terminal colors to work
print(colors.neutral) #Sets terminal color

def pick_game(): #Allows user to pick game
    global game #Makes game a global variable

    try:
        game = int(input(f"{colors.neutral}1) OMORI\n2) Minecraft\n\ngame: {colors.answer}"))
        if game > 0 and game <= 2:
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
    except EOFError:
        print("\x1b[0m")
        exit()

def pick_status(): #Allows user to pick specific status for game
    global status #Make status a global variable

    try:
        if game == 1:
            status = int(input(f"{colors.neutral}1) White Space\n2) Black Space\n\nstatus: {colors.answer}"))
            if status == 1:
                rpc_status.set_status("whitespace")
            if status == 2:
                rpc_status.set_status("blackspace")
            else:
                print(f"\n{colors.error}Invalid status{colors.neutral}\n")
                return pick_status()
        elif game == 2:
            status = int(input(f"{colors.neutral}1) Bee\n\nstatus: "))
            if status == 1:
                rpc_status.set_status("bee")
            else:
                print(f"\n{colors.error}Invalid status{colors.neutral}\n")
                return pick_status()
    except ValueError:
        print(f"\n{colors.error}Please choose a number{colors.neutral}\n")
        return pick_game()
    except KeyboardInterrupt:
        print("\x1b[0m")
        exit()
    except EOFError:
        print("\x1b[0m")
        exit()

def _time():
    try:
        _time = str(input(f"{colors.neutral}Display elapsed time?\nY\\n: {colors.answer}").upper())
        if _time == "Y":
            return int(time.time())
        elif _time == "N":
            return _time
        else:
            print(f"\n{colors.error}Please choose Y\\n{colors.neutral}\n")
            return _time()
    except ValueError:
        print(f"\n{colors.error}Please choose Y\\n{colors.neutral}\n")
        return _time()
    except KeyboardInterrupt:
        print("\x1b[0m")
        exit()
    except EOFError:
        print("\x1b[0m")
        exit()

def main():
    pick_game()
    pick_status()
    start = _time()

def quit(signo, _frame):
    print (f"Interupted by {signo}")
    exit.set()

if __name__ == "__main__":
    for sig in ('TERM', 'INT'):
        signal.signal(getattr(signal, 'SIG'+sig), quit);

    main()

    while not exit.is_set():
        try:
            rpc_status.run_rpc() #Keeps the rpc running
            for i in range(15000):
                exit.wait(0.001)
        except Exception as e: #If keyboard interupt exit
            print(e)
