#Ex1
word= ['a', 'b']
print(word)
first= word[-2]
print("The first word is "+ first+ ".\n")

a= [2, 3, 4]
tmp= []
for i in a:
    tmp.append(i)
tmp[-1]= 'last'
print(a, tmp)

#Ex2
num= list(range(9, 15, 2))
print(num)

num[0]=12
print('change the first num')
print(num)

add= sum(num)
print('\nSum is')
print(add)
print('Only first num changed')

#Ex3
new_num= list(range(5, 0, -1))
print(new_num)

print(list(range(9, -6, -2)))