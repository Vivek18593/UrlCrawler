from bs4 import BeautifulSoup
import requests

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

test_links = []
def add_url(url):
    if url not in test_links:
        test_links.append(url)
        print(url)

def result():
    for urls in test_links:
        print(urls)


run = True
while run:
    baseurl = input('Enter URL: ')
    print('Crawling...\n')
    scrap(baseurl)
    backup_link = test_links
    for url in backup_link:
        if url != baseurl:
            try:
                scrap(url)
            except:
                pass
    #result()
    print('\nCompleted!')
    q = input('Do you want to run again?(Y/N): ').lower()
    if q == 'y':
        run = True
    else:
        run = False


