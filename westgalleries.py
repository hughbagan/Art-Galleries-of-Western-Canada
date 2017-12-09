# This program takes an input file, reads the contents,
# and sorts the input into Galleries.
# Then the information can be outputted in various formats
# using the terminal interface.

# Just run the program in the same directory as the input ("abgalleries.txt")

# Hugh Bagan

#--- DEFINED CLASSES ---#

class Gallery:
    
    def __init__(self):
        self.name = "Gallery"
        self.manager = "manager"
        self.address = "address"
        self.location = "location" # City, Province (a list; do this later)
        self.post = "post"
        self.ph = "phone"
        self.email = "email"
        self.url = "url"
        self.fax = "fax"
        self.desc = "description"
        
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def getMan(self):
        return self.manager
    def setMan(self, new_man):
        self.manager = new_man
    def getAddress(self):
        return self.address
    def setAddress(self,new_addr):
        self.address = new_addr
    def getLocation(self):
        return self.location
    def setLocation(self,new_loc):
        self.location = new_loc
    def getPost(self):
        return self.post
    def setPost(self,new_code):
        self.post = new_code
    def getPhone(self):
        return self.ph
    def setPhone(self,new_ph):
        self.ph = new_ph
    def getEmail(self):
        return self.email
    def setEmail(self,new_em):
        self.email = new_em
    def getWebsite(self):
        return self.url
    def setWebsite(self,new_url):
        self.url = new_url
    def getFax(self):
        return self.fax
    def setFax(self,new_fax):
        self.fax = new_fax
    def getDescription(self):
        return self.desc
    def setDescription(self, new_desc):
        self.desc = new_desc
    
class GalleryList:
    
    def __init__(self):
        self.glist = []
    
    def getList(self):
        return self.glist
    
    def addGallery(self, g):
        # g - an instance of the Gallery class
        self.glist.append(g)
    
    def printList(self):
        for g in self.glist:
            print(g)#print(g.getName(),g.getMan(),g.getAddress(),g.getLocation(),g.getPost(),g.getPhone(),g.getEmail(),g.getWebsite())
    
    # -- Output Methods -- #
    
    def getNames(self):
        out = "\n-- West Galleries --\n"
        for g in self.glist:
            out += "%s\n" % g.getName()
        return out
    def getContacts(self):
        out = ''
        out += "\n-- West Galleries full profiles --\n\n"
        for g in self.glist:
            out += g.getName() + '\n'
            if g.getMan() != 'na': 
                out += "Contact: %s" % g.getMan() + '\n'
            out += g.getAddress() + '\n'
            out += "%s %s" % (g.getLocation(), g.getPost()) + '\n'
            if g.getWebsite() != 'na':
                out += 'WEB: %s' % g.getWebsite() + '\n'
            if g.getEmail() != 'na':
                out += 'EML: %s' % g.getEmail() + '\n'
            if g.getPhone() != 'na' and g.getFax() != 'na':
                out += 'PHO: %s   FAX: %s\n' % (g.getPhone(),g.getFax())
            elif g.getPhone() != 'na':
                out += 'PHO: %s\n' % g.getPhone()
            elif g.getFax() != 'na':
                out += 'FAX: %s\n' % g.getFax()
            out += g.getDescription() +'\n'
            out += '\n'
        return out
    def getWebContacts(self):
        out = ''
        out += "\n-- West Galleries Online --\n\n"
        for g in self.glist:
            out += g.getName() + '\n'
            out += g.getWebsite() + '\n'
            out += g.getEmail() +'\n'
            out += '\n'
        return out
    def getLetterMailing(self):
        # Prints a combination of address, location, post
        out = ''
        out += "\n-- West Galleries mailing information --\n\n"
        for g in self.glist:
            out += g.getName() + '\n'
            out += g.getAddress() + '\n'
            out += "%s %s\n\n" % (g.getLocation(), g.getPost())
        return out
    def getEmailList(self):
        out = ''
        for g in self.glist:
            if g.getEmail() != 'na' and g.getEmail() != '' and g.getEmail() != " ":
                out += g.getEmail() + "; "
        return out
    def getEmails(self):
        out = "--- West Galleries' Emails ---\n\n"
        for g in self.glist:
            if g.getEmail() != "na" and g.getEmail() != "" and g.getEmail() != " ":
                out += g.getName() + '\n'
                out += g.getEmail() + '\n\n'
        return out
    def getPhones(self):
        out = ''
        out += "\n-- West Galleries Phone Numbers --\n"
        for g in self.glist:
            out += g.getName()+'\n'
            out += g.getPhone()+"\n\n"
        return out
    def getWebsites(self):
        out = ''
        out += "\n-- West Galleries websites --\n"
        for g in self.glist:
            out += g.getName()+"\n"
            out += g.getWebsite()+"\n\n"
        return out
    def getFaxes(self):
        out = ''
        out += "\n-- West Galleries fax --\n"
        for g in self.glist:
            out += g.getName()+'\n'
            out += g.getFax()+'\n\n'
        return out
            
#--- DEFINED FUNCTIONS --#

def isGreaterAlpha(str1, str2, descending=True):
    # Compares two strings alphabetically
    # returns True if string1 is greater than string2
    for i in range(len(min(str1, str2))):
        if str1[i] != str2[i]:
            if descending:
                return ord(str1[i]) < ord(str2[i])
            else:
                return ord(str1[i]) > ord(str2[i])
    return None # for some reason the strings are identical

def sortAlpha(alist, descending=True):
    # Sort the gallery list by name, alphabetically.
    # This is a merge sort.
    if len(alist)>1: # base case
        # Split the list in half until base case is reached
        mid = len(alist)//2
        lefthalf = alist[:mid]  # slicing costs more here
        righthalf = alist[mid:]
        sortAlpha(lefthalf)
        sortAlpha(righthalf)
        # Merging
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            # Take the smaller value (letters)
            leftname = lefthalf[i].getName().lower()
            rightname = righthalf[j].getName().lower()
            if isGreaterAlpha(leftname, rightname, descending):
                alist[k] = lefthalf[i]
                i=i+1
            else:
                alist[k] = righthalf[j]
                j=j+1
            k=k+1
        # Collect the extras on each half
        while i<len(lefthalf):
            alist[k] = lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j=j+1
            k=k+1
            
def importGalleriesFromFile(directory):
    # directory - a string of the directory of the input text file
    # Returns an instance of GalleryList.
    print('Importing Galleries from text file: %s' % directory)
    infile = open(directory,'r')
    lines = infile.read().splitlines() # Returns a list.
    infile.close()
    if lines[len(lines)-1] != '': lines.append('')
    ##print(lines)
    # Parse the information from the text file and place it into "raw".
    raw = []    # list of lists
    raw_e = []
    for i in range(0,len(lines)):
        ##print(i, lines[i])
        if lines[i] == '' or lines[i] == "$":
            raw.append(raw_e)
            raw_e = []
            ##print('done entry')
        else:
            raw_e.append(lines[i])
    ##print(raw_e)
    ##print(raw)
    # Use the data to create instances of Gallery, and place those instances
    # in a list (ie. an instance of GalleryList)
    newGalleryList = GalleryList()
    for entry in raw:
        # Add entry to GalleryList
        if len(entry) < 10:
            raise Exception("%s was entered incorrectly." % entry[0])
        name = entry[0]
        address = entry[1]
        location = entry[2]
        postcode = entry[3]
        ph = entry[4]
        email = entry[5]
        url = entry[6]
        fax = entry[7]
        manager = entry[8]
        description = entry[9]
        
        newg = Gallery()
        newg.setName(name)
        newg.setAddress(address)
        newg.setLocation(location)
        newg.setPost(postcode)
        newg.setPhone(ph)
        newg.setEmail(email)
        newg.setWebsite(url)
        newg.setMan(manager)
        newg.setFax(fax)
        newg.setDescription(description)
        newGalleryList.addGallery(newg)
    print("%i results found." % len(newGalleryList.getList()))
    return newGalleryList

#--- MAIN PROGRAM ---#

def main():
    print('--- ART GALLERY DATA ---')
    print('This program imports information on art galleries\n in western Canada. It then sorts the galleries and outputs\n them in a desired format.')
    
    # Import gallery information.
    filename = input('Please specify filename: ')
    if filename == 'abgalleries.txt':
        select = 'alberta'
    else:
        print('Error: invalid filename.')
    
    wGalleries = importGalleriesFromFile(filename)
    print('Successfully imported gallery entries from %s' % select)
    
    print('Sorting galleries alphabetically based on gallery name.')
    sortAlpha(wGalleries.getList())
    
    while (True):
        print('What do you want to do?')
        print('[e] Exit')
        print('[1] Output full profile information')
        print('[2] Output web information')
        print('[3] Output email mailing list')
        print('[4] Output mailing information')
        do = input()
        if do.lower() == 'e':
            break
        print('Outputting entries to text files...')
        if int(do) == 1: # Output full profile information
            out_full = open('GalleriesWest %s full.txt' % select,'w')
            out_full.write('Province: %s\n' % select)
            out_full.write('%i results' % len(wGalleries.getList()))
            out_full.write(wGalleries.getContacts())
            out_full.close()        
        elif int(do) == 2: # Output web contact
            out_web = open('GalleriesWest %s web.txt' % select,'w')
            out_web.write('Province: %s\n' % select)
            out_web.write('%i results' % len(wGalleries.getList()))
            out_web.write(wGalleries.getWebContacts())
            out_web.close()        
        elif int(do) == 3: # Output email list
            out_em = open('GalleriesWest %s email.txt' % select,'w')
            out_em.write('Province: %s\n' % select)
            out_em.write('%i results\n' % len(wGalleries.getList()))
            out_em.write(wGalleries.getEmailList())
            out_em.close()        
        elif int(do) == 4: # Output mailing info
            out_mail = open('GalleriesWest %s mailing.txt' % select, 'w')
            out_mail.write('Province: %s\n' % select)
            out_mail.write('%i results' % len(wGalleries.getList()))
            out_mail.write(wGalleries.getLetterMailing())
            out_mail.close()
        print('Done.')
    print('Goodbye.')
main()
