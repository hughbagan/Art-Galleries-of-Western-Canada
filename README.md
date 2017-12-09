# Art-Galleries-of-Western-Canada
This Python program processes and outputs contact information for art galleries. It requires an input text file containing the Name and Address of each gallery (at minimum). The program stores each chunk of information in a "Gallery" object and sorts the list of Galleries alphabetically using a merge sort algorithm. Then specific information about the galleries (eg. Mailing addresses, online presences) can be retrieved and outputted to text files using the terminal interface.

# The problem
I created this program for my Dad who owns a small framing and fine art business in Edmonton. He regularly mails out flyers and other promotional material to galleries in western Canada that might need framing work done. However, it's difficult to keep track of all of these businesses and their contact information. This led to me creating this program that outputs contacts in specific formats including mailing information, phone/fax numbers, addresses, websites, emails, and even specific people associated with the business.

# How to use
Simply download the main python program "westgalleries.py". You will also need a sample input file: place "abgalleries.txt" in the same directory as the python file and run it. The other directories in this repo are just for viewing purposes.
After running, you can select output options in the terminal. The program will output information in your selected format to a text file in the running directory.

# Web scraping?
A sample input file "abgalleries.txt" is provided, which contains information on Albertan art galleries (obtained from http://www.gallerieswest.ca/). I originally wanted the program to scrape that website for galleries -- that way I would not have to manually update any input text files for accuracy. Unfortunately, I could not get my web-spider version of the program to get past the pagination on gallerieswest.ca. Look into the ../scraper directory of this repo to see how far I got.
However, the text file does contain a complete record of the Albertan galleries from August 2017, which is pretty good considering that the information doesn't get changed very often.
