def prStr():
    s= "num1: {0}, num2: {1}, num3: {2}".format(100, 200, 300)
    print(s)
    p= "Pi: {:.2f}".format(3.145683)
    print(p)
prStr()

def readInput():
    #python2.7 raw_input()
    #python3 input()
    line1= raw_input()
    line2= raw_input()
    line3= raw_input()
    print"Line1 is :", line1
    print"Line2 is :", line2
    print"Line3 is :", line3
    num= int(line2)
    print"Your second line",line2
    print"length is "
    print(num)
readInput()

import sys
def mysum():
    for line in sys.stdin:
        line = line.strip()
        print(line)
        tokens= line.split()
        print(tokens)
        print(len(tokens))
        total= 0
        for i in range(0, len(tokens)):
            total+= float(tokens[i])
        print(total)
mysum()