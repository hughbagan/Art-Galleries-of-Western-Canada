from bs4 import BeautifulSoup
import urllib
import urllib.request

url = 'http://www.gallerieswest.ca/search/location/browse-galleries-by-province/#letter_filter=all&ord=alpha&page=1'
file = open('gw-prettify.txt','w')

r = urllib.request.urlopen(url)
soup = BeautifulSoup(r)
file.write(soup.prettify())
file.close()

#for k in range(1,3):
    #link = url + str(k) + '/'
    #print('opening: ' + link)
    #r = urllib.request.urlopen(link).read()
    #soup = BeautifulSoup(r)

    ## find all instances in the soup with the parameter
    ## (in this case, the class name quotesBody)
    #samples = soup.find_all(class_= "quotesBody") # returns a list
    #for j in samples:
        #file.write(j.p.get_text())
        #file.write("\n")
        #file.write('---')
        #file.write("\n")

#file.close()
#print('done')