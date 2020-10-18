#!/bin/sh
#Github: https://github.com/sujitmandal
#Pypi : https://pypi.org/user/sujitmandal/
#LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/

conda info --envs

echo $'Enter Environment Name : ' 
read environment
conda activate $environment

echo $'\n'
pip install -r requirements.txt

conda install -c conda-forge opencv=4.2.0

pip install -q git+https://github.com/tensorflow/docs