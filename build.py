from subprocess import Popen
from sys import argv
from os import system
from time import sleep

system("color 0a")

if argv[1] == "backdoor":
    if argv[2] == "enhanced":
        print("[!] Building payload...")
        sleep(5)
        Popen("pyinstaller --onefile --onedir Backdoor/Backdoor.pyw")
