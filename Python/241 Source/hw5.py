def test(i):    'Takes an integer as input and prints its value as Negative, Positive, or Zero'
    if i < 0:
        print('Negative')
    elif i== 0:
        print('Zero')
    else:
        print('Positive')
#end test
        
def vowel_indices(s):
    'Takes a string as a parameter and prints the indices of all the vowels in the string'
    for i in range(0, len(s)):
        if(s[i] in 'aieouAEIOU'):
            print(i)
#end vowel_indices
            
def mult5(lst, number):
    'Takes a list of numbers and a single integer, prints only the n integers in the list'
    for i in lst:
        if i % number == 0:
            print(i)
#end mult5

def n_letter(wordList, wordLen):
    'Returns a new list containing all of the strings in lst that have length n'
    newList = []
    for i in wordList:
        if len(i) == wordLen:
            newList.append(i)
    print(newList)
#end n_letter

def findDigits(string):
    'Takes a string as a parameter and returns a list containing all of the digits that appear in the string'
    newList = []
    for i in string:
        if i.isdigit():
            newList.append(int(i))
    print(newList)
    #end findDigits

