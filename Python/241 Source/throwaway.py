def acronym(phrase):
    words = phrase.split()
    res = ''
    for w in words:
        res = res + w[0].upper()
    return res
def divisors(n):
    res = []
    for num in range(1, n+1):
        if n % num == 0:
            res.append(num)
    return res
        
def nested(n):
    for j in range(n):
        for i in range(1, n+1):
            print(i, end = ' ')
        print('')
        
def nested2(n):
    for j in range(n):
        for i in range(j+1):
            print(i, end = ' ')
        print('')
