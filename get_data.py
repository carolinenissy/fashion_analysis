from urllib.request import urlopen
url = 'https://www.rheos.jp/'
html  =urlopen(url)

from bs4 import BeautifulSoup
from requests import get


url = 'http://wear.jp/saekowear/'
html = get(url)
bsobj = BeautifulSoup(html.content, 'html.parser')

intro = bsobj.find('h1', {'class':'name'})
name = intro.get_text()
info = intro.span.attrs['class']


profile = bsobj.find('ul', {'class':'info clearfix'})

user = profile.findAll('li')[0].get_text()

prof_list =[]
for i in range(1,len(profile.findAll('li'))):
    prof_list.append(profile.findAll('li')[i].get_text())



#for li in brand[0].findAll('li'):
#    print(li.find('div', {'class':'main'}).find('p', {'class':'brand'}).get_text() )
#    print(li.find('div', {'class':'main'}).find('a', {'href': re.compile('/category/')}).get_text())

