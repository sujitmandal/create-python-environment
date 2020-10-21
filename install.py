import os 

"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
"""

def fileName():
    fileNames = os.listdir('Download')
    fileName = fileNames[0]

    insall = 'bash'+ ' ' + fileName
    return(insall)

if __name__ == "__main__":
    fileName()