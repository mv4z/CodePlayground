def recLessThan(n):
    'create a less than symbol shape'
    if n == 0:
        return
    else:
        print(n*' ' + '*')
        recLessThan(n-1)
        print(n*' ' + '*')
        
def recHourGlassShape(c,n,i):
    'c is the character to display, n is number of characters on each line and i is indentation'
    if n <= 0:
        return
    else:
        print(i*' ' + c*n)
        recHourGlassShape(c, n-2, i+1)
        print(i*' ' + c*n)
    
  
def recMultiplier(val):
    'Multiply each digit in an integer in the sequence right to left'
    if val == 0:
        return 0
    if val < 10:
        return val
    res = 1
    t = val % 10
    res = res*t
    output = recMultiplier(val//10)
    
    if output == 0:
        return res
    else:
        return output * res


def recStringCombiner(lst):
    'concatinate all the strings in a list into one string'
    if len(lst) == 0:
        return ''
    if type(lst[0]) == str:
        return lst[0] + recStringCombiner(lst[1:])
    else:
        return recStringCombiner(lst[1:])

def recNumberCount(lst,n):
    counter = 0
    'get a count of  with a number in a flat list'
    if lst == []:
        return 0
    elif lst[0] == n:
        return recNumberCount(lst[1:], n)+1
    else:
        return recNumberCount(lst[1:], n)

class Automobile(object):
    'Automobile class. Only way to initialize values is through the constructor'
    def __init__(self,make='Unknown', model='Unknown',year='1900',color='Unknown'):
        'Constructor'
        self.make=make
        self.color=color
        self.year=year
        self.model=model

    def getMake(self):
        'Get the Make of the Car'
        return self.make

    def getColor(self):
        'Get the color of the car'
        return self.color

    def getYear(self):
        'Get the year of the car'
        return self.year

    def getModel(self):
        'get the model of the car'
        return self.model

    def __repr__(self):
        return "Automobile('{}','{}','{}','{}')".format(self.make,self.model,self.year,self.color)

    def __str__(self):
        'get the string representation of the automobile'
        return 'A {}, {}, {} model year {}'.format(self.color,self.make,self.model,self.year)

class AutomobileInventoryManager(object):
    'Class to manage adding / removing inventory from the inventory file'

    def __init__(self, filename='inventory.txt'):
        'Initialize the Inventory Manager'
        self.filename = filename
        self.newlst = []
        self.newcarlst = []
        
    def loadInventory(self):
        'load cars from the inventory file'
        file = open(self.filename, 'r')
        self.contents = file.readlines()
        file.close()
        for i in self.contents:
            self.newlst.append(i.rstrip().split(','))
        try:
            for j in self.newlst:
                self.make = j[0]
                self.model = j[1]
                self.year = j[2]
                self.color = j[3]
                self.newcarlst.append((Automobile(self.make, self.model, self.year, self.color)))
        except:
            return False
        print(self.newcarlst)
        return True
           
    def saveInventory(self):
        'save the inventory to the file and overwrite the old data.'
        try:
            outfile = open(filename, 'w')
            for i in self.contents:
                outfile.write(repr(Automobile(i)))
                return True
        except:
            return False

    def addInventory(self, auto):
        'add a new auto to inventory'
        self.newcarlst.append(auto)

    def removeInventory(self, index):
        'remove inventory from the internal collection'
        try:
            self.newcarlst.pop(index)
        except:
            return False

    def __len__(self):
        'get the count of cars in inventory'
        try:
            return len(self.newcarlst)
        except:
            print('List is empty')

    def __contains__(self, make):
        'true to if a make of car in inventory'
        for i in self.newcarlst:
            if make == i.getMake():
                return True

    def __getitem__(self,index):
        'get an automobile from inventory'
        return self.newcarlst[index]

    def __iter__(self):
        'get an iterator to loop through the automobile objects'
        return iter(self.newlst)

    def __str__(self):
        'string represention of the inventory'
        return ('There are {} cars in the inventory'.format(len(self.newcarlst)))



