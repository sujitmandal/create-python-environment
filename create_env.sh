#!/bin/sh
#Github: https://github.com/sujitmandal
#Pypi : https://pypi.org/user/sujitmandal/
#LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/

echo $'\n'
echo $'Enter Environment Name : ' 
read environment
echo $'Enter Python Version : '
read version

#conda update -n base -c defaults conda

conda create --name $environment python=$version
conda info --envs