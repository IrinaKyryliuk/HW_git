# 2. Знайти довжину самого короткого слова.
'''
array - array of words in the text
array_len - array of lens words
len_shot - lenght of the shortest word
'''
try:
    file = open("D:/HW_Git/HW_3/text.txt")
    fileN = file.read()
    array = []
    for line in fileN.split():
        array.append(line)
    array_len = []
    print(array)
    for word in array:
        array_len.append(len(word))
    len_shot = min(array_len)
    print(array_len)
    print('lenght of the shortest word = ', len_shot)
finally:
     file.close()