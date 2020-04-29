import random
def getValue(maxVal):
    a = maxVal *2
    return random.randrange(0,a) #make sure to describe the behavior of this line in detail!

def func(val):
    output = set()
    for i in val:
        print(i)
        num = int(i)
        if num > 0:
            rndnum = getValue(num)
            output.add(rndnum)
    return output

val=input('Please enter your 7 digit student id:')
print(func(val))
