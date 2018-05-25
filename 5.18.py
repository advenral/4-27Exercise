#Problem 1
from math import pi
def squareList(nums):
    return [x**2 for x in nums]
def absList(nums, x):
    return [abs(i) for i in nums if abs(i)<x]
def piList(n):
    return [round(pi, i) for i in range(1, n+1)]

print("Q1", squareList([1, 2, 3]))
print("Q2", absList([1, 2, 3, 4, 5, -1, -2, 0], 3))
print("Q3", piList(5))

#Problem 2
def result(answer, guess):
    a=0
    b=0
    for a_idx, a_val in enumerate(answer):
        for g_idx, g_val in enumerate(guess):
            if a_val== g_val:
                if a_idx== g_idx:
                    a= a+1
                else:
                    b= b+1
    return str(a)+ 'A'+ str(b)+ 'B'

print(result('1234', '4321'))
print(result('5678', '1234'))
print(result('2345', '5342'))

#Problem 3
ages={}
def prAge(name):
    if (ages.get(name)):
        print(name, ages.get(name))
    else:
        print('N/A')
def test():
    num = int(input())
    #print num
    
    for i in range(0, num):
        line= input()
        #print line
        tokens= line.split()
        #print tokens

        ages[tokens[0]]= int(tokens[1])
    print(ages)
    num = int(input())
    for i in range(0, num):
        line= input()
        prAge(line)
test()

#Test
num= [0, 1, 2]
square= []
for x in num:
    square.append(x** 2)
print(square)

square2 = [x ** 2 for x in num]
print(square2)

num2= [-1, -2, -3, 5]
new_abs= [abs(x) for x in num2 if x<-1]
print(new_abs)