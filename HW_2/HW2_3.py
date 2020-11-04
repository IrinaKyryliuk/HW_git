# 3.Календар
# Необхідно створити програму для підрахунку
# днів увказаному місяці та зазначити чи день є вихідним.
# Input data: Дата у вигляді: 02-07-2019 (день-місяць-рік)
'''
data, my_data: inputed date
my_monht = inputed month
my_year = my_data year
'''
import datetime
import calendar
date = input("Input data in format day-month-year : ")
try:
    my_data = datetime.datetime.strptime(date, "%d-%m-%Y")

    print("inputed date", my_data.date().strftime("%d-%m-%Y"))
    my_monht = my_data.month
    my_year = my_data.year
    print("month", my_monht)
    print("year", my_year)

    print('In', my_data.date().strftime("%B"), my_year, calendar.monthrange(my_year, my_monht)[1], '- days')

    print( my_data.date().strftime("%d.%m.%Y"), my_data.date().strftime("%A"))
except:
    print('Please enter correct data value')