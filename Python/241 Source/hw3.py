def printMultiples(n, m):
    'Takes two positive integers (m and n) and prints the first m multiples of n'
    for i in range(n,(m+1)*n,n):
        print(i, end = ' ')

def customSpam(name, money, email):
    'Create a spam message to a specific person, with a specific dollar amount, and a specific email address'
    print('Dear', name.title()+',')
    print('We would like to let you know about a great opportunity.')
    print('You can make', *money.upper(), 'dollars in just a few short weeks!')
    print('This is a limited-time offer.')
    print('Please contact us at', email, 'for more information.')


def ion2e(word):
    'Inspects a string to see if it ends in -ion. If it does it removes the suffix and adds -e'
    if word.endswith('ion'):
        print(word[:-3] + 'e')
    else:
        print(word)

def numLen(s, n):
    'Returns the number of words in the string that has length n'
    word = 0
    for i in s.split():
        if len(i) == n:
            word += 1
    return word

def makeNeg(numlist, int):
    'Changes the sign of the object at the specific index int'
    if int > len(numlist) or int < -len(numlist):
        print('That index is invalid. The list was not changed.')
    else:
        if numlist[int] < 0:
            pass
        else:
            numlist[int] = -numlist[int]
    print(numlist)
