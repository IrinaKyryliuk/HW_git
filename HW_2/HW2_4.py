# 5. Масив
# Створити програму для генерації випадкового масиву чисел. 
# Масив має бути створений випадковими числами (розмір 20 елементів)
# Програма має визначати скільки елементів масиву дорівнює числу введеному користувачем
# Кожне друге число має бути від’ємне
# Визначити скільки елементів масиву дорівнюють числу введеному користувачем
'''
number: inputed number
count: count of number in the array
mas: array
'''
import random
mas = []
count=0
number = input("Input the number for finding it in the array")
try:
    number= int(number)
    for i in range(0,20):
        if i % 2 == 0:
            mas.append(random.randint(0,50))
        elif  i % 2 != 0:
            mas.append(random.randint(-50,0))
        if(mas[i]==number):
            count+=1
    print(*mas)
    if(count>0):
        print("Number ", number, " was found - ", count, " times")
    else:
        print("That number is absent in the array")
except:
    print('Please enter numeric value')

