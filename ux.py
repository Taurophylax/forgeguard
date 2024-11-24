import os
from colorama import Fore, Back, Style

def cls():
    os.system('cls') if os.name == 'nt' else os.system('clear')

def system(text):
    print("\n" + Fore.GREEN + "SYSTEM: " + Style.RESET_ALL + text + "\n")

EM = Style.BRIGHT + Fore.YELLOW
NPC = Style.BRIGHT + Fore.CYAN
OBJ = Style.BRIGHT + Fore.MAGENTA
WALL = Style.BRIGHT + Fore.BLACK
MOB = Fore.RED
BOSS = Style.BRIGHT + Fore.RED
RST = Style.RESET_ALL