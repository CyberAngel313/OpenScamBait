from subprocess import Popen
from sys import argv
from os import system

system("color 0a")

def BDbuild():
    Popen("pyinstaller --onefile --onedir toolkit/Backdoor/backdoor.py")

if argv[1] == "backdoor":
    BDbuild()