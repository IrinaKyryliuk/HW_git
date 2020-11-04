# 1. Визначити, який відсоток слів у тексті починається з букви “z”.
'''
count_word - count of words in the text
letter - inputed letter
array_l - count of words witch start from inputed letter
'''
try:
    file = open("D:/HW_Git/HW_3/text.txt")
    fileN = file.read()
    array = []
    for line in fileN.split():
        array.append(line)
    print('words in the text = ', len(array))
    letter = str(input('Input letter? '))
    array_l = []
    for word in array:
        if word[0] == letter:
            array_l.append(word)
    print('words witch start from "', letter, '" = ', len(array_l))
    percentage = (len(array_l))/(len(array))*100
    print ('percentage of words witch start from "', letter, '" = ', percentage, "%")
finally: 
    file.close()
