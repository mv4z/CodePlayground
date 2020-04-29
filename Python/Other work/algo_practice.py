def swap(lst, fi, si):
    tmp = lst[fi]
    lst[fi] = lst[si]
    lst[si] = tmp

    return lst

def minIndex(lst, startIndex):
    minValue = lst[startIndex]
    minIndex = startIndex

    for i in range(minIndex, len(lst)):
        if lst[i] < minValue:
            minValue = lst[i]
            minIndex = i
    return minIndex

def selectionSort(lst):
    starting = 0
    for i in range(0, len(lst)):
        starting = minIndex(lst, i)
        swap(lst, i, starting)
    return lst

def insert(lst, rightIndex, value):
    for i in range(rightIndex, -1, -1):
        if(value < lst[i]):
            lst[i + 1] = lst[i] #copy
            lst[i] = value

    return lst

def insertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and  (key < lst[j]):
            lst[j + 1] = lst[j]
            j -=1
        lst[j + 1] = key
    return lst

def iterFact(n):
    res = 1
    if (n==0):
        return res
    else:
        for i in range(1, n+1):
            res *= i
    return res

def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)

def palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return palindrome(string[1:-1])

def power(x, n):
    if(n == 0):
        return 1
    elif(n < 0):
        return 1/(power(x, -n))

    else:
        return x * power(x, n-1)

def mergeSort(arr, p, r):
    if p < r:
        q = (p+r) // 2
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
    return arr

def reverse(arr):
    return arr[::-1]

def reverseVowels(s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        newWord =''
        
        i, j = 0, (len(s)-1)
        while(i < j):
            
def intersection(arr1, arr2):
    res = []
    for i in range(0, len(arr1)):
        if arr1[i] in arr2:
            res.append(arr1[i])
    return set(res)

def intersection2(nums1, nums2):
    result = []
    if(len(nums1) < len(nums2)):
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.append(nums1[i])
    return result

def firstUnique(word):
    i = 0
    while(i < len(word)):
        if word[i] in word[i+1::]:
            i +=1
        else:
            return i
    return -1

def findDifference(s, t):
    for letter in t:
        if letter not in s:
            return letter


def firstNonRepeatingChar(string):
    hm = dict()
    for i in string:
        if( i in hm):
            hm[i] += 1
        else:
            hm[i] = 1
    for i in string:
        if hm[i] == 1:
            return i
    return '_'

def rotateImage(a):
    n = len(a)

    for i in xrange(n):
        for j in xrange( n):
                a[i][j] = a[j][i]
                a[j][i] = a[i][j]
    for l in a:
        l.reverse()

    return a

