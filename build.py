from subprocess import Popen
from sys import argv
from os import system

system("color 0a")

if argv[1] == "backdoor":
    if argv[2] == 1:
        Popen("pyinstaller --onefile --onedir Backdoor/backdoor.py")