def lastfirst(stringList):
    'takes a list of names as a parameter in the format Last, First and returns a list with 2 sublists: first names and last names'
    firstname = []
    lastname = []
    for i in stringList:
        wholeName = i.split()
        lastname.append(wholeName[0])
        firstname.append(wholeName[1])
    return [firstname] + [lastname]
#end lastfirst

def countEvens(lst):
    'returns the number of elements in the list that are even'
    counter = 0
    for i in lst:
        for k in i:
            if k % 2 == 0:
                counter += 1
    return(counter)
#end countEvens


def findMinRow(lst):
    'returns the index of the minimum row in the list'
    if len(lst) < 1:
        return -1
    else:
        minRow = 0
        count = 0
        newList = []
        for i in lst:
            sum = 0
            for k in i:
                sum = sum + k
            newList.append(sum)
            count += 1
        min = newList[0]
        count = 0
        for x in newList:
            if x <= min:
                min = x
                minRow = count
            count += 1
        print(minRow)
#end findMinRow

def findMaxDiff(lst):
    'prints the index of the row with the maximum difference between elements as well as the value of the maximum difference in that row'
    ind = 0
    res_max = -1
    for i in range(0, len(lst)):
        maxi = lst[i][0]
        mini = lst[i][0]
        for j in range(0, len(lst[i])):
            if lst[i][j] > maxi:
                maxi = lst[i][j]
            if lst[i][j] < mini:
                mini = lst[i][j]
            if (maxi-mini) > res_max:
                res_max = maxi-mini
                ind = i
    print('The maximum difference of {} is found in row {}'.format(res_max, ind))
#end findMaxDiff
        
            


