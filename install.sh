#!/bin/sh
#Github: https://github.com/sujitmandal
#Pypi : https://pypi.org/user/sujitmandal/
#LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/

sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install python3-pip

echo $'\n'
pip3 install -r requirements.txt

echo $'\n'
python3 anaconda.py

echo $'\n'
python3 install.py