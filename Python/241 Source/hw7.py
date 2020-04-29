def doubles(numList):
    'takes as input a list of integers and outputs the integers in the lsit that are exaclty twice the previous integer in the list, one per line.'
    for num in range (0, len(numList)):
        if numList[num] == (2*numList[num-1]):
            print (numList[num])
#end doubles
        
def inversions(s):
    'takes a sequence of uppercase letters and returns the number of inversions in the sequence'
    if s is '':
        return 0
    else:
        counter = 0
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i] > s[j]:
                    counter +=  1
        return counter
#end inversions

def letter2number(grade):
    'takes a string representing a letter grade as a parameter and returns the grade point associated with that grade'
    grades = {'A': 4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-': 2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'D-':0.7, 'F+':0.3, 'F':0.0}
    upGrade = grade.upper()
    if upGrade in grades:
        return(grades.get(upGrade))
    else:
        return('unknown grade')
#end letter2number

def printTwoLargest():
    'inputs an arbitrary number of positive numbers from the use, The function then prints the two largest values entered by the user'
    try:
        number = int(input("Please enter a number: "))
        biggest = number
        if number > 0:
            number = int(input("Please enter a number: "))
            if biggest < number:
                secBiggest = biggest
                biggest = number
            else:
                secBiggest = number
        count = 1
        while number > 0:
            count = count + 1
            number = int(input("Please enter a number: "))
            if number > biggest:
                secBiggest = biggest
                biggest = number
            elif biggest > number > secBiggest:
                secBiggest = number
        if count < 2:  
            print("Fewer than two positive numbers were entered.")
        else:
            print("The largest is ", biggest)
            print("The second largest is ", secBiggest)
    except ValueError:
        print("That was not a valid number. Please try again.")
        printTwoLargest()
