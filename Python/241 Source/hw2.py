def sequences():
    for num in range(27,36):
        print(num, end = " ")
    print()
    for num in range(21,71,7):
        print(num, end = " ")
    print()
    for num in range(35,0,-2):
        print(num, end = " ")
    print()

        
def returnFour(str):
    if len(str) >= 4:
        return(str[0:4])
    return(' ')

def returnN(str,int):
    if len(str) >= (int):
        return(str[0:(int)])
    return(' ')

def multiplesN(int):
    for i in range(4):
        print((int)*(i))

def printLess(lst,int):
    for num in lst:
        if num <int:
            print(num, end = ' ')
    
