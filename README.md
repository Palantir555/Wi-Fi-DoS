`aireplay-ng` only supports 2 deauthentication modes: 1 client or all of them.
In some cases you may want to keep a few clients off your network, but not all
of them. This script does that for you.

`wifidos.py` takes no arguments; everything is configured from the source code:

```
#Deauthenticate all clients (you should use aircrack-ng directly):
#network = "de:ad:be:ef:fe:ed"
#victims = []

#Deauthenticate these specific clients:
network = "de:ad:be:ef:fe:ed"
victims = [
   "00:00:00:00:00:11", #Client 01
   "00:00:00:00:00:22", #Client 02
   "00:00:00:00:00:33", #Client 03
   "00:00:00:00:00:44", #Client 04
   "00:00:00:00:00:55"] #Client 05

#Network interface:
interface = "wlan1mon"
```

Don't do anything nasty with it :)
