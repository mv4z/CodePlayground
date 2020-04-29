from bisect import bisect_left

def binarySearch(lst, key):
    lst.sort()
    first = 0
    last = len(lst)-1
    while(first < last):
        middle = (first + last) //2
        if(lst[middle] < key):
            first = middle+1
        elif(lst[middle] > key):
            last = middle-1
        else:
            print("Target is at %s:" %middle)
            return middle

    print("Target not found")
    return"unsuccessful"

