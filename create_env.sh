#!/bin/sh
#Github: https://github.com/sujitmandal
#Pypi : https://pypi.org/user/sujitmandal/
#LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/

sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install python3-pip

echo $'\n'
pip install -r requirements.txt

echo $'\n'
python3 anaconda.py

echo $'\n'
bash Anaconda3-2020.07-Linux-x86_64.sh

echo $'\n'
echo $'Enter Environment Name : ' 
read environment
echo $'Enter Python Version : '
read version

#conda update -n base -c defaults conda

conda create --name $environment python=$version

conda info --envs