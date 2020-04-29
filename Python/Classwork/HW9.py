import os

def findAllDirectories(root,dirName):
    'returns a list containing the full pathname of all occurrences of directories with the directory name specified'
    lst = []
    dirLst = os.listdir(root)

    for i in dirLst:
        path = os.path.join(root, i)
        if path.split('/')[-1] == dirName:
            lst.append(path)

        if os.path.isdir(path):
            lst = findAllDirectories(path, dirName) + lst

    return lst

def crawl(filename,indent):
    'opens the file filename and reads each link in the file'
    try:
        file = open(filename, 'r')
        content = file.readlines()
        file.close()
        print(' ' * indent + 'Entering {}'.format(filename))

        for f in content:
            crawl(f.strip('\n'), indent + 5)

    except:
        print('"{}" not found.'.format(filename))
        pass
        

    

def nestingCount(pathname):
    'computes and returns the number of levels of subdirectories found in a path'
    temp = []
    lst = os.listdir(pathname)

    for i in lst:
        p = os.path.join(pathname, i)
        if os.path.isdir(p):
            a = nestingCount(p)
            temp.append(a)
            
    if len(temp) == 0:
        return 1

    return max(temp) + 1


from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

def testParser(url):
    content = urlopen(url).read().decode()
    parser = AnchorParser()
    parser.feed(content)
    return parser.getLabels()


class AnchorParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.lst = []
        self.check = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.check = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.check = False
            
    def handle_data(self, data):
        if self.check == True:
            self.lst.append(data)
        
    def getLabels(self):
        return self.lst

def testHParser(url):
    content = urlopen(url).read().decode()
    parser = HeaderParser()
    parser.feed(content)
    return parser.getHeadings()


class HeaderParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.lst = []
        self.check = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            self.check = True

    def handle_endtag(self, tag):
        if tag == 'li':
            self.check = False
            
    def handle_data(self, data):
        if self.check == True:
            self.lst.append(data)
        
    def getHeadings(self):
        return self.lst 
