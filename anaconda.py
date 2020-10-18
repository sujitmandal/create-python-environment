import os
import wget
import requests
from bs4 import BeautifulSoup

"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
"""

URL = 'https://www.anaconda.com/products/individual'
request = requests.get(URL)

if request.status_code == 200:
    soup = BeautifulSoup(request.content, 'html.parser')
    downloadLinks = []

    for i in soup.find_all('a', {'class' : 'link-download js-event-individual'}):
        link = i['href']
        downloadLinks.append(link)

    downloadLink = downloadLinks[-2]
    fileName = downloadLink.split('/')

    try:
        if not os.path.exists(fileName[-1]):
            shFile = wget.download(downloadLink)
            print('\n')
            print('Download Completed.')

        else:
            print('\n')
            print('File Exists On The Current Directory..')
            directory = os.popen('sh shell.sh').readline()
            print(directory)
            
    except OSError:
        print('Error: Creating directory!')
        
else:
    print('Connection Error..')