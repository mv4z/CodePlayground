def unique(lst):
    'takes a 2D list and returns the number of entries in the list that are unique'
    newLst = []
    for i in lst:
        for j in i:
            if j not in newLst:
                newLst.append(j)
    return len(newLst)
#end unique

def vote(candidate_list):
    'the function prints for every name on the ballot the number of votes that the candidate received.'
    vote_count={}
    vote_count['unknown']=0
    for name in candidate_list:
        vote_count[name]=0
    t_list=vote_count.keys()
    t_list=[candidate.lower() for candidate in candidate_list]
    while True:
        name=input("Enter a vote: ")
        if name=="":
            break
        if name.lower() not in t_list:
                vote_count['unknown']+=1
        else:
            for cand_name in candidate_list:
                if name.lower() == cand_name.lower():
                    vote_count[cand_name]+=1                 
    for k,v in vote_count.items():
        if v == 1 :
            print("There was " + str(v) +" vote for "+ k+".")
        if v > 1:
            print("There were " + str(v) +" votes for "+ k+".")
#end vote

def game(num):
    'take an integer n as a parameter and ask the child to answer n single-digit addition questions.'
    import random
    total = 0
    correct = 0
    while total < num:
        x = random.randrange(0,10)
        y = random.randrange(0,10)
        Sum = x + y
        print (x, "+", y, "=")
        answer = input("Enter answer: ")
        while answer.isnumeric()==False:
            print("Please enter your answer using digits (0-9).")
            print (x, "+", y, "=")
            answer = input("Enter answer: ")
        if int(answer) == Sum:
            correct += 1
            print("Correct.")
        else:
            print("Incorrect.")
        total += 1
    print("You got {} correct out of {}".format(correct, total))
#end game

def ticker(fname):
    'reads the file and stores the company names and stock symbols in a dictionary. It then provides an interface to the user so that he/she can obtain the stock symbol for a given company.'
    newList1 = []
    newList2 = []
    dictionario = {}
    infile = open(fname, 'r')
    line1 = infile.readline()
    newList1.append(line1)
    line2 = infile.readline()
    newList2.append(line2)
    print( newList1)
    print( newList2)
    
##    try:
##        dictionario[line1.rstrip()] = line2.rstrip()
##        lowerName =  input('Enter a company name: ')
##        name = lowerName.upper()
##        print('Ticker symbol: ', dictionario[name])
##    except:
##        print('{} is not in the ticker system.'.format(name.upper()))
##    ticker2(fname)
##    if lowerName == '':
##        infile.close()
##        exit()
    

    

