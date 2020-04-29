class Storm(object): 
    'a class that abstracts a storm'
    xrain = 0
    xwind = 0
    xyear = 0
    def __init__(self, rain=0, wind=0 , year=1900):
        self.xrain = rain
        self.xwind = wind
        self.xyear = year

    def getWindSpeed(self):
        'get max wind speed as MPH'
        return self.xwind

    def getRainFall(self):
        'get rainfall in inches per hour'
        return self.xrain

    def getYear(self):
        'get year storm recorded'
        return self.xyear

    def setYear(self,year):
        'set year recorded'
        self.xyear = year

    def setRainFall(self,rain):
        'set rainfall inches per hour'
        self.xrain = rain

    def setWindSpeed(self,speed):
        'set windspeed MPH'
        self.xspeed = speed


    def __repr__(self):
        'get canoncial representation of Storm'
        return 'Storm(' + str(self.xrain) + ' , ' + str(self.xwind) + ' , ' + str(self.xyear) + ')'

    def __str__(self):
        'get string represetation of Storm'
        return 'I am a storm with peak winds of {} mph, peak rainfall of {} inches per hour in the year {}'.format(self.xwind, self.xrain, self.xyear)


class TropicalStorm(Storm):
    'a class that abstracts a tropical storm'
    xname = 'default'
    
    def __init__(self, rain=0, wind=0 , year=1900, name='default'):
        'initalize Tropical Storm.  '
        self.xrain = rain
        self.xwind = wind
        self.xyear = year
        self.xname = name
        
    def setName(self, name):
        'set storm name'
        self.xname = name
        
    def getName(self):
        'Get storm name'
        return self.xname

    def __repr__(self):
        'get canoncial representation of TropicalStorm'
        return 'TropicalStorm({}, {}, {}, {})'.format(self.xrain, self.xwind, self.xyear, self.xname)

    def __str__(self):
        'get string representation of TropicalStorm'
        return 'I am a tropical storm named {} with peak winds of {} mph, peak rainfall of {} inches per hour in the year {}'.format(self.xname, self.xwind, self.xrain, self.xyear)


class Hurricane(TropicalStorm):
    'a class that abstracts a Hurricane'
    xcategory = 0
    
    def __init__(self, rain=0, wind=0 , year=1900, name='default', category=0):
        'Initialize a Hurricane'
        self.xrain = rain
        self.xwind = wind
        self.xyear = year
        self.xname = name
        self.xcategory = category

    def getCategory(self):
        'get category'
        return self.xcategory

    def setCategory(self,category):
        'set category'
        self.xcategory = category

    def __repr__(self):
        'get canoncial representation of Hurricane'
        return "Hurricane({}, {}, {}, {}, {})".format(self.xrain, self.xwind, self.xyear, self.xname, self.xcategory)

    def __str__(self):
        'get string representation of TropicalStorm'
        return 'I am a category {} Hurricane named {} with peak winds of {} mph, peak rainfall of {} inches per hour in the year {}.'.format(self.xcategory, self.xname, self.xwind, self.xrain, self.xyear)

def processTropicalStorms(filename):
    infile = open(filename, 'r')
    content = infile.readlines()
    newStorms = []
    for a in content:
        if a != '':
            b = a.split(',')
            name = b[0]
            rainfall = b[2]
            wind = b[1]
            year = b[3]
            newStorm = TropicalStorm(rain, wind, year, name)
            newStorms.append(newAtorm)
            print (newStorm)
        elif a == '':
            print(list(content))
    infile.close()
    return newStorms
    print('The file {} could not be found. Exiting...'.format(filename))
