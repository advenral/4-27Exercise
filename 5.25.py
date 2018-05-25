book1 = ("#010", "Stone Programming", 330)
(id1, title1, price1) = book1

print(book1, book1[2])

#problem 2
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 3, 20)
# y = np.linspace(0, 9, 20)
# plt.plot(x, y)
# plt.show()

#problem 1
students={}

def test():
    num= int(input())
    for i in range(0, num):
        line= input()
        tokens= line.split()
        print(tokens)
        
        for j in range(1, 5):
            students[tokens[0]+ "-"+ str(j)]= int(tokens[j])
    num= int(input())
    for i in range(0, num):
        line= input()
        print(line, students[line])
        #print(line, students.get(line))
test()
#C:\\Windows\\System32\\cmd.exe
#C:\\Program Files\\Git\\bin\\bash.exe