''' 
numeric : integer
sum : sum of digits
number : number of digits
'''
numeric = int(input("enter an integer "))

sum = 0
number = 0
while (numeric != 0):
    sum = sum + numeric % 10
    numeric = numeric // 10
    number = number + 1
print('sum of digits = ', sum)
print('number of digits = ', number)

