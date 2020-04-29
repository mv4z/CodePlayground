def even(filename):
    'that takes in as a parameter a file name, The function will return a list of all of the even numbers found in the file'
    evenNum = []
    invalid = []
    try:
        inFile = open(filename)
        content = inFile.read()
        content = content.split()
        for i in content:
            try:
                if eval(i) % 2 == 0:
                    evenNum.append(eval(i))
            except:
                invalid.append(i)
                print('The value \'{}\' could not be returned'.format((invalid[0])))
        return(evenNum)
    except:
        print('File {} could not be found. Please enter valid file name.'.format(filename))
##end even()
     
def survey(filename):
    'the function asks the user for 3 pieces of information: full name, city they were born in and age and appends that information to a file and keeps track of the survey' 
    with open(filename, 'a') as f:
        try:
            fname = input('Please enter your full name: ')
            city = input('Please enter the city you were born in: ')
            age = input('Please enter your age: ')
            f.write('{}:{}:{}\n'.format(fname, city, age))
            f.close()
            print('Thank you for participating! Summary: ')
            print('\nName: {} \nCity: {} \nAge: {}'.format(fname, city, age))
        except:
            print('File access error. Try again')
##end survey()
  
    
print(even('test.txt'))
survey('log.txt')


    
