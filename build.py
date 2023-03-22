from subprocess import Popen
from sys import argv

def BDbuild():
    Popen("pyinstaller --onefile toolkit/Backdoor/backdoor.py")

if argv[1] == "backdoor":
    BDbuild()