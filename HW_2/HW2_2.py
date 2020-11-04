# 2. Числа прописом
# Написати програму для виведення цілих чисел прописом.
'''
Klas_od: клас одиниць
Klas_des: 
Klas_n
Klas_sot
'''

def number_w(n):
    Klas_od = {0 : 'нуль', 1 : 'один', 2 : 'два', 3 : 'три', 4 : 'чотири', 5 : 'пять',
    6 : 'шість', 7 : 'сім', 8 : 'вісім', 9 : 'девять'}
    Klas_des = {10 : 'десять', 20 : 'двадцать', 30 : 'тридцать', 40 : 'сорок',
    50 : 'пятдесят', 60 : 'шістдесят', 70 : 'сімьдесят', 80 : 'вісімдесят', 90 : 'девяносто'}
    Klas_n = {11 : 'одинадцять', 12 : 'дванадцять', 13 : 'тринадцять', 14 : 'чотирнадцять',
    15 : 'пятнадцять', 16 : 'шістнадцять',
    17 : 'сімнадцять', 18 : 'вісімнадцять', 19 : 'девятнадцять'}
    Klas_sot =  {100 : 'сто', 200 : 'двісті', 300 : 'триста', 400 : 'чотириста',
    500 : 'пятсот', 600 : 'шістсот', 700 : 'сімсот', 800 : 'вісімсот', 900 : 'девятсот'}

    n1 = n % 10
    n2 = n - n1
    n3 = n % 100
    n4 = n - n3
    n5 = n3 - n1
    n6 = n3 - n1
    if (n < 10):
        return Klas_od.get(n)
    elif (n > 10  and n < 20):
        return Klas_n.get(n)
    elif (n >= 10 and n < 100 and n1 == 0 ):
        return Klas_des.get(n)
    elif (n > 20 and  n < 100 and n1 != 0 ):
        return Klas_des.get(n2) + ' ' + Klas_od.get(n1)
    elif (n >= 100 and n < 1000 and n3 == 0):
        return Klas_sot.get(n)
    elif (n >= 100 and n < 1000 and n3 != 0 and n6 == 0 and n1 != 0):
        return Klas_sot.get(n4) + ' ' + Klas_od.get(n1)
    elif (n >= 100 and n < 1000 and n3 != 0 and n6 != 0 and n1 == 0):
        return Klas_sot.get(n4) + ' ' + Klas_des.get(n5)
    elif (n >= 100 and n < 1000 and n3 != 0 and n6 != 0 and n1 != 0):
        return Klas_sot.get(n4) + ' ' + Klas_des.get(n5)+ ' ' + Klas_od.get(n1)
    else:
        return 'Некоректно введене число'
n = int(input("ВВедіть ціле число менше 1000 :  "))
print(number_w(n))
