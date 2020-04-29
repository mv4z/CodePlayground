class GroceryItem(object):
    'Class represented as a Grocery List Item'

    def __init__(self,name='',cost=0,count=0,category=''):
        'Constructor'
        self.name= name
        self.cost= cost
        self.count= count
        self.category= category

    def getName(self):
        'get the name of the item'
        return self.name

    def getCost(self):
        'get the cost of the item'
        return self.cost

    def getCount(self):
        'get the count of the item'
        return self.count

    def getCategory(self):
        'get the category name'
        return self.category

    def multiplyItemCount(self, number):
        'multiply the count of the number of items by the number passed in.  Example passing in 2 doubles the count'
        self.count = number * self.count

    def setCount(self, count):
        'set the exact count of items'
        self.count=count

    def setName(self,name):
        'set the name of the item'
        self.name = name

    def setCost(self,cost):
        'set the count of the item'
        self.cost = cost

    def setCategory(self,category):
        'set the category name'
        self.category = category

    def __repr__(self):
        'get the string representation of the item'
        if self.name == '':
            temp_name = "''"
        else:
           temp_name = self.name
        if self.category == '':
            temp ="''"
        else:
            temp= self.category
        
        return ('GroceryItems (' + str(temp_name) + "," + str(self.cost) + "," + str(self.count) +  "," + str(temp) + ')')

    def __str__(self):
        'get the python representation of the item'
        return (str(self.name) + ':' + str(self.cost) + ':' + str(self.count) + ':' + str(self.category))


 # part B
class GroceryList(object):
    'Class representing a Grocery List Collection'

    def __init__(self):
        'Initalizes an empty grocery list'
        self.lst = []

    def addGroceryItem(self,groceryItem):
        'adds a grocery list item to the collection'
        self.lst.append(groceryItem)


    def getItems(self):
        'gets a list of all the grocery list items'
        return self.lst

    def findItemsByCategory(self, category):
        'return a list of all of the grocery items that have a specific category'
        X = []
        for food in self.lst:
            if food.getCategory == category:
                 X.append(food)
        return X
                

    def getTotalCost(self):
        'get the total cost of all the items in the list'
        cost = 0 
        for food in self.lst:
            cost += food.getCost()
        return cost
            
    def multiplyAllItemsCount(self,number):
        'increase count of each item in the list by multiple'
        for food in self.lst:
            food.setCount(number * food.getCount())

    def multiplyItemCountByCategory(self,category,number):
        'increase count of each item of a specific category in the list by multiple'
        for food in self.lst:
            if category == food.getCategory():
                food.setCount(number * food.getCount())

    def __str__(self):
        'get the string representation of the grocery list'
        pass 

    #part 3
    
    def writeListToFile(self, fileName):
        'write the contents of the list to a file'
        outputfile= open(fileName, 'w')
        for food in self.lst:
            outputfile.write(str(food) + '\n')
        outputfile.close()

    def readListFromFile(self, fileName):
        'read the contents of the list from a file'
        inputfile = open(fileName, 'r')
        content = readlines()
        
    
    #part 4

    def __iter__(self):
        'return an iterator'
        pass

    #part 5a


    def __lt__(self,otherGroceryList):
        'returns true if the the cost of the local list is less than the other list'
        pass

    def __gt__(self,otherGroceryList):
        'returns true if the the cost of the local list is greater than the other list'
        pass

    def __eq__(self,otherGroceryList):
        'returns true if the total cost of the grocery list is equal to the other grocery list'
        pass

    #part 5b 
    
    def __add__(self,otherGroceryList):
        'returns a new grocery list that combines the local list and the other grocery list'
        pass

    
