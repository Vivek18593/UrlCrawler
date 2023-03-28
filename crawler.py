from bs4 import BeautifulSoup
import requests, os
from termcolor import colored
os.system('color')

paths = []
def scrap(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    content = soup.find_all('a')
    for link in content:
        links = link.get('href')
        paths.append(links)
    get_links()

def get_links():
    for link in paths:
        try:
            if link == None:
                pass
            if link[:4] == 'http':
                add_url(link)
            if link[0] != '/' and link[:4] != 'http':
                if baseurl[-1] != '/':
                    url = baseurl+'/'+link
                else:
                    url = baseurl+link
                add_url(url)
            if link[0] == '/':
                if baseurl[-1] != '/':
                    url = baseurl+link
                else:
                    link = link.replace('/','',1)
                    url = baseurl+link
                add_url(url)
        except:
            pass

count = 0
test_links = []
def add_url(url):
    global count
    if url not in test_links:
        test_links.append(url)
        count+=1
        print(url)

def result():
    for urls in test_links:
        print(urls)


run = True
while run:
    baseurl = input(colored('Enter URL: ','green'))
    print(colored('Crawling...\n','magenta'))
    scrap(baseurl)
    backup_link = test_links
    for url in backup_link:
        if url != baseurl:
            try:
                scrap(url)
            except:
                pass
    #result()
    print(colored('\nCompleted!','green'))
    print(colored('Total count of urls found: ','yellow') + colored(f'{count}','red'))
    print('\n')
    q = input(colored('Do you want to run again?(Y/N): ','red')).lower()
    if q == 'y':
        run = True
    else:
        run = False


