''' 
letterL : the letter of the Latin alphabet
letterNum : number of Unicod
'''
letterL = input("enter the letter of the Latin alphabet ")
letterNum = ord(letterL)

if letterL != 'A' and letterL != 'a':
    if letterL != 'Z'and letterL != 'z':
        print('entered symbol', letterL)
        print('previous symbol', chr(letterNum -1))
        print('next symbol', chr(letterNum + 1))
    else:
        print('entered symbol', letterL)
        print('previous symbol', chr(letterNum -1))
        print(letterL, '- last symbol of the Latin alphabet')
else:
    print('entered symbol', letterL)
    print(letterL, '- first symbol of the Latin alphabet')
    print('next symbol', chr(letterNum + 1))
