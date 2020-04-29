from tkinter import Tk, Label, Frame, Entry, Button, END
from tkinter.messagebox import showinfo
from random import randrange
class NegativeNumberError(Exception):
        pass
    
class Game(Frame):
    'Number guessing app'
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)
        self.pack()
        self.guesses = 0
        self.numGames = 0
        self.number = int(randrange(0,10))
        self.make_widgets()

    def make_widgets(self):
        'defines Game widgets'
        self.main = Label(self, text="You have made {} guesses. You have completed {} games".format(self.guesses, self.numGames))
        self.main.pack()
        Label(self, text="Enter your guess...").pack()
        self.e = Entry(self, width=30)
        self.e.pack()
        self.guess = Button(self, text="Enter", command=self.reply)
        self.guess.pack()

    def updateLabel(self):
        'updates the label with game info'
        self.main.config(text = "You have made {} guesses. You have completed {} games".format(self.guesses, self.numGames))

    def new_game(self):
        self.e.delete(0, END)
        
    def reply(self):
        'handles button clicks'
        self.guesses += 1
        self.numGuess = int(self.e.get())
        if self.numGuess == self.number:
            showinfo('Winner',message='You got it right! Run it back, TURBO...')
            self.numGames += 1
            self.guesses = 0
            self.number = randrange(0,10)
            print(self.number)
        self.new_game()
        self.updateLabel()


class MortgageCalculator(Tk):
    'Mortgage calculator GUI'
    
    def __init__(self,parent=None):
        'The constructor'
        Tk.__init__(self, parent)
        self.title('Mortgage Calculator')
        self.make_widgets()

    def calculateMortgage(self):
        'Calculate monthly payment and show pop-ups'
        try:
            self.P = float(self.principal.get())
        except ValueError:
            showinfo('Monthly Payment', message='Error. Incorrect value entered for principal. Please enter an integer and try again')


        try:
            self.IR = float(self.interest.get())/100
        except ValueError:
            showinfo('Monthly Payment', message='Error. Incorrect value entered for interest rate. Please enter a valid Interest Rate')

        try:
            self.T = int(self.time.get())
        except ValueError:
            showinfo('Monthly Payment', message='Error. Incorrect value entered for time. Please enter a different value.')

        self.numerator = ((self.P * self.IR)/1200.00)
        self.denominator = 1 - ((1.0+(self.IR/1200.00))**(-12.0*self.T))
        try:
            self.MonthlyMortgage = self.numerator / self.denominator
            showinfo('Monthly Payment', message='Your monthly payment is $%2.2f' %(self.MonthlyMortgage))
        except ZeroDivisionError:
            showinfo('Monthly Payment', message='Error. Unable to calculate payment.')
            
        print(self.MonthlyMortgage)

    def make_widgets(self):
        'Create UI'
        Label(self, text = 'Principal').grid(row=0, column = 0)
        self.principal = Entry(self, width = 20)
        self.principal.grid(row = 0, column = 1)
    
        Label(self, text = 'Interest Rate').grid(row=1, column = 0)
        self.interest = Entry(self, width = 20)
        self.interest.grid(row=1, column=1)
                          
        Label(self, text = 'Term in Years').grid(row=2, column = 0)
        self.time = Entry(self, width = 20)
        self.time.grid(row=2, column=1)
        
        Button(self,text='Calculate Payment', command=self.calculateMortgage).grid(row=4,column = 1)
        


class PositivePriorityQueue(object):
    'Positive Priority queue class'

    def __init__(self):
        'constructor initializes empty priority queue'
        self.q = []


    def insert(self, item):
        'inserts item into priority queue'
        self.num = item
        if self.num >= 0:
            self.q.append(self.num)
            print(self.q)
        else:
            raise NegativeNumberError
        
    def min(self):
        'returns minimum item in positive priority queue'
        return min(self.q)

    def removeMin(self):
        'removes minimum item in positive priority queue'
        self.min = min(self.q)
        self.q.remove(self.min)

    def removeMax(self):
        'removes maximum item in positive priority queue'
        self.max = max(self.q)
        self.q.remove(self.max)
        
    def __len__(self):
        'returns size of positive priority queue'
        return len(self.q)

    def isEmpty(self):
        'checks whether positive priority queue is empty'
        if len(self.q) == 0:
            return True
        else:
            return False

    def clear(self):
        'remove all items from the queue'
        self.lst = self.q.clear()
        
    def __iter__(self):
        'Returns an iterator'
        return iter(self.q)
