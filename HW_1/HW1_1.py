''' 
sumDeposit : the amount of the deposit
sumCurrent: Сurrent deposit amount
rate: deposit rate
profit: profit 
duration: duration of the deposit
percentage: percentage increase in the deposit
'''
duration = int(input("Input the duration of the deposit "))

sumDeposit = int(input("Input the sum of the deposit "))

rate = int(input("Input the rate(%) of the deposit "))
rateVs = rate / 100

sumCurrent = sumDeposit

print('Year\t', 'Sum\t', 'Profit')
for i in range(1, duration+1):
    profit = sumCurrent * rateVs
    print(i, '\t' ,round(sumCurrent, 2), '\t',  round(profit, 2))
    percentage = (sumCurrent - sumDeposit) / sumDeposit * 100
    sumCurrent = sumCurrent + profit
    
print('Deposit amount for', duration, 'years', 'will grow on ', round(percentage, 2), '%')