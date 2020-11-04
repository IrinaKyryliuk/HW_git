''' 
beginInterval : beginning of the interval
endInterval: the end of the interval
numberInterval: number from the interval
evenNum: even numbers
oddNum: odd numbers
'''
beginInterval = int(input("Input the beginning of the interval "))
endInterval = int(input("Input the end of the interval "))

print('interval [', beginInterval, ';', endInterval, ']')

evenNum = []
oddNum = []

for numberInterval in range(beginInterval, endInterval+1):
    if numberInterval % 2 == 0:
        evenNum.append(numberInterval)
    else:
        oddNum.append(numberInterval)
print('even numbers', evenNum)
print('odd numbers', oddNum)
