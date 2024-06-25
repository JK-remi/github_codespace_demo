# class
class Line:
    length = 0
    
    def __init__(self, len):
        self.length = len
        print(self.length, ' length line is created')

    def __del__(self):
        print(self.length, ' length line is deleted')

    def __repr__(self):
        return 'legth: ' + str(self.length)

    def __add__(self, other):
        return self.length + other.length
    
    def __lt__(self, other):
        return self.length < other.length
    
    def __eq__(self, other):
        return self.length == other.length
    
# main
myLine1 = Line(100)
myLine2 = Line(200)

print(myLine1)

print('sum of two lines: ', myLine1+myLine2)

if myLine1 < myLine2:
    print('Line2 is longer')
elif myLine1 == myLine2:
    print ('Line legths are same')
else:
    print ('I don\'t know which one is long')

del(myLine1)