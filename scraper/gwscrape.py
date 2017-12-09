# Gallery scrape test
from bs4 import BeautifulSoup
import urllib
import urllib.request
import time

url = 'http://www.gallerieswest.ca/search/location/browse-galleries-by-province/#letter_filter=all&ord=alpha'
file = open('gw-scrape.txt','w')

for page in range(1,25): # 24 pages of results...
    link = url + '&page=' + str(page)
    print('opening: '+link)
    r = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(r)
    scrapes = soup.find_all(class_="address") # returns a list
    
    file.write("Page %i\n" % page)
    for scrape in scrapes:
        name = scrape.h4.get_text()
        address = scrape.p.get_text()
        file.write(name + '\n')
        file.write(address + '\n')
        file.write('---')
        file.write('\n')
        
    print('sleep...')
    time.sleep(5)
        
file.close()
print('All done!')