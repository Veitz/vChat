## vChat

vChat is a simple encrypted multithreading CommandLine ChatApp.  
It included a Keyfilegenerator to generate a fresh shared Key for Server and all Clients.

## Features  

* Serverfile
* Clientfile for multiple Client connections
* configfile for both
* Keyfilegenerator


## Build instructions  

It is tested on Ubuntu 18 & 20 LTS but it should run on any platform.   
Install the packages from the `requiremets.sh` or run it via `sudo sh requirements.sh`    
You can create a fresh Key with `python3 keyfilegen.py` afterward share the Keyfile with all clients and the server,    
change your IP's in `chatconfig.ini` and run the server `python3 chatServerEncrypted.py`.   
Clientconnection via `python3 chatClientEncryptet.py`.

## Requirements

install python3: https://www.python.org/  

* `sudo apt install screen` for pip3 on Ubuntu
* `sudo apt install python3-pip` for pip3 on Ubuntu
* `pip3 install --upgrade pip`   
* `pip3 install cryptography`   
* `pip3 install configparser`   
* `pip3 install datetime`    
