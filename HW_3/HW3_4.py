# 4. У заданому тексті знищити всі слова з парними порядковими номерами.
#(вивести слова з парними порядковими номерами)
'''
array - array of words in the text
arr - array of words with odd numbers
'''
try:
    file = open("D:/HW_Git/HW_3/text.txt")
    fileN = file.read()
    array = []
    for line in fileN.split():
        array.append(line)
    
    count = len(array)
    print('word =', count)
    arr = []
    for i in range(0,count-1):
        if i % 2 == 0:
            arr.append(array[i])
    print('words with odd numbers :')
    print(*arr)
finally:
    file.close()