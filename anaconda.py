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

def Anaconda(URL):
    request = requests.get(URL)

    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        downloadLinks = []

        for i in soup.find_all('a', {'class' : 'link-download js-event-individual'}):
            link = i['href']
            downloadLinks.append(link)

        downloadLink = downloadLinks[-2]
        fileNames = downloadLink.split('/')
        fileName = fileNames[-1]

        try:
            if not os.path.exists('Download'):
                os.mkdir('Download')
                folder = (os.getcwd() + '/Download')

                destination = os.path.join(folder, fileName)
                wget.download(downloadLink, out=destination)
                print('\n')
                print('Download Completed.')

            else:
                print('\n')
                print('File Exists On This Directory..')
                print('Directory : {}'.format(os.getcwd()) + '/Download')
                
        except OSError:
            print('Error: Creating directory!')
            
    else:
        print('Connection Error..')

if __name__ == "__main__":
    Anaconda(URL)