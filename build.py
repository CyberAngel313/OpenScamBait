from subprocess import Popen
from sys import argv

def BDbuild():
    Popen("pyinstaller --onefile toolkit/backdoor.py")

if argv[1] == "backdoor":
    BDbuild()