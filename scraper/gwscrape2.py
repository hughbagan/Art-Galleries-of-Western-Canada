# gwscrape2
from bs4 import BeautifulSoup
import urllib
import urllib.request
import time
from westgalleries import *

url = 'http://www.gallerieswest.ca/search/location/'
filename = 'gwscrape2.txt'

location = 'alberta'

for i in range(1,5):
    link = "%s%s/#page=%i" % (url,location,i)
    print(link)
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, "html.parser")
    locations = soup.find_all('div',class_='location_result')
    print(type(locations))
    
    for loc in locations:
        adr = loc.find(class_='address')
        print(adr.h4.get_text())
        print(adr.p.get_text())
        
    print('sleep...')
    time.sleep(2)
print('Done')