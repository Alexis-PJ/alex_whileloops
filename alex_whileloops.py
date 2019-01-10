'''
1) swap two variables
'''
#a = 5
#b = 10
#print('a =', a,'b =', b)

# create a temporary variable temp
#temp = a # save the value of a in the temp variable
#a = b # a is getting the value in b
#b = temp

#print('the new variables a =',a,'b =',b)

# write all integers between 1 and 9 using while loop

#x = 1
#while x < 10:
    #print(x,' ',end='')
    #x =x +1
row = 1
col = 1

while row < 10:
    while col < 5:
        print(row,col,' ',end='')
        col = col + 1
    print()
    row = row + 1
    co1 = 1

# fibonacci sequence
# 1,,2,3,5,8,13,21,34,...

x = 1
y = 1
cont = 'c'

while cont == 'c':
    print('a fibon number is:', x+y)

    temp = x
    x = y
    y = y + temp
    cont = input('if want more fibon numbs press c, else any key')