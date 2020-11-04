# 3.Визначити на яку букву починається більшість слів у заданому тексті
'''
data: dictionary with initial letter and number of words
key :  array of key
values : key of values
values_max: maximum with values
'''
try:
    file = open("D:/HW_Git/HW_3/text.txt")
    fileN = file.read()
    data = {}
    for word in fileN.split():
        letter = word[0].lower()
        element = data.setdefault(letter,0)
        data[letter]+=1
    print(data)
    key = data.keys()
    values = data.values()
    print(key)
    print(values)
    values_max = max(values)
    print('max = ', values_max)
    for key_1, values_1 in data.items():
        if values_1 == values_max:
            print('Most words start with the letter - ','"',key_1,'"')
finally:
    file.close()