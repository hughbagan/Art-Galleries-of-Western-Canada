# Beautiful Soup test
from bs4 import BeautifulSoup
import requests
import time

url = "http://the-big-bang-theory.com/quotes/character/Sheldon/"
file = open('bbtQuotes3', 'w')

for k in range(1, 3):
    
    link = url + str(k) + "/"
    print("opening: " + link)
    r = requests.get(link) # retrieves the HTML code from page
    # Create a BeautifulSoup instance from the HTML
    # data is represented in a nested structure
    # use "print(soup.prettify())" to view the structure
    soup = BeautifulSoup(r.content, "lxml")
    # find all instances in the soup with the parameter
    # (in this case, the class name quotesBody)
    samples = soup.find_all(class_= "quotesBody") # returns a list
    
    for j in samples:
        file.write(j.p.get_text())
        file.write("\n")
        file.write('---')
        file.write("\n")
        
    print("sleep...")
    time.sleep(5)

file.close()
print("All done!")