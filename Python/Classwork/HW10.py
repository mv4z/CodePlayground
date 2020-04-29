from tkinter import Button, Entry, Label,Tk, TOP, LEFT, RIGHT, END
from tkinter.messagebox import showinfo
import random

class ShellGame(object):
    def __init__(self,shellCount=3,winningPiece='X', losingPiece=''):
        self.shellCount = shellCount
        self.winningPiece = winningPiece
        self.losingPiece = losingPiece
        self.board = []

    def resetShells(self):
        self.winningIndex = random.randrange(0, self.shellCount-1)
        self.board = [self.losingPiece]*self.shellCount
        self.board[self.winningIndex] = self.winningPiece

    def checkWin(self,index):
        if index == self.winningIndex:
            return True
        else:
            return False

    def getBoard(self):
        print(self.board)
        
class ShellGameGUI(Tk):
    'Shell Game'
    def __init__(self,game=ShellGame(),parent=None):
        'constructor'
        Tk.__init__(self, parent)
        self.game = game
        self.title('Shell Game')
        self.make_widgets()
        self.game.resetShells()
        print(self.game.winningIndex)

    def checkShell(self, index):
        'checks to see if the ball is under the shell'
        if index == 0:
            if self.game.checkWin(0) == True:
                showinfo(title = 'Shell Game', message = "You got it!")
                self.shellOneGuess.config(text = "{}".format(self.game.winningPiece))
            else:
                showinfo(title = 'Shell Game', message = "Sorry Wrong Guess")
                
        if index == 1:
            if self.game.checkWin(1) == True:
                showinfo(title = 'Shell Game', message = "You got it!")
                self.shellTwoGuess.config(text = "{}".format(self.game.winningPiece))
            else:
                showinfo(title = 'Shell Game', message = "Sorry Wrong Guess")
        
        if index == 2:
            if self.game.checkWin(2) == True:
                showinfo(title = 'Shell Game', message = "You got it!")
                self.shellThreeGuess.config(text = "{}".format(self.game.winningPiece))
            else:
                showinfo(title = 'Shell Game', message = "Sorry Wrong Guess")

    def newGame(self):
        self.shellOneGuess.config(text = '')
        self.shellTwoGuess.config(text = '')
        self.shellThreeGuess.config(text = '')
        self.game.resetShells()
        print(self.game.winningIndex)


        
    def make_widgets(self):
        'add widgets to the UI'
        Label(self, text = "Shell Game").grid(row = 0, column = 0)
    
        Button(self, text = 'Look Under First Shell', command = lambda:self.checkShell(0)).grid(row = 1, column = 0)
        self.shellOneGuess = Label(self, text = "")
        self.shellOneGuess.grid(row = 2, column = 0)
    
        Button(self, text = 'Look Under Second Shell', command = lambda:self.checkShell(1)).grid(row = 1, column = 1)
        self.shellTwoGuess = Label(self, text = "")
        self.shellTwoGuess.grid(row = 2, column = 1)
    
        Button(self, text = 'Look Under Third Shell', command = lambda:self.checkShell(2)).grid(row = 1, column = 2)
        self.shellThreeGuess = Label(self, text = "")
        self.shellThreeGuess.grid(row = 2, column = 2)
        
        Button(self, text = 'New Game', command = lambda:self.newGame()).grid(row = 3, column = 0)
ShellGameGUI().mainloop()


import os
def frequency(folder):
    temp = dict()
    for i in os.listdir(folder):
        n = os.path.join(folder, i)

        if os.path.isdir(n):
            d = frequency(n)
            for j in d:
                if j in temp:
                    temp[j] += 1
                else:
                    temp[j] = 1
        else:
            try:
                infile = open(n, 'r')
                files = infile.readlines()
                infile.close()
                for f in files:
                    print(f)
                    lst = f.strip('\n').split()
                    for word in lst:
                        if word in temp:
                            temp[word] += 1
                        else:
                            temp[word] = 1
                print(temp)
            except:
                print('Could not open file.')
        return temp
    

def fileNameCount(folder,name):
    total = 0
    for i in os.listdir(folder):
        n=os.path.join(folder,i)
        if os.path.isdir(n):
            dirs =fileNameCount(n, name)
            total += dirs

        elif item == name:
            total += 1
            
    return total
    

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

#PAGES TO TEST PARSER WITH
#https://www.cdm.depaul.edu/academics/Pages/Current/Requirements-BS-In-Computer-Science-Software-Development.aspx
#https://www.cdm.depaul.edu/academics/Pages/Current/Requirements-BS-In-Computer-Science-Game-Systems.aspx
def testParser(url):
    content = urlopen(url).read().decode()
    parser = CourseParser()
    parser.feed(content)
    return parser.getData()

class CourseParser(HTMLParser):
    def __init__(self):
       self.lst = []
       self.check = False
        
    def handle_starttag(self, tag, attrs):
       if tag == '':
           for i in attrs:
               if i =='a':
                   self.check = True
                   
    def handle_endtag(self, tag):
       if tag == 'a':
            self.check = False 

    def handle_data(self, data):
        if self.check == True:
            self.lst.append(data)
        
    def getData(self):
        return self.lst
