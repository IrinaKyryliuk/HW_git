''' 
name_inp: name which user input
name_patronomic : list of friends
'''
name_patronomic = {
    'Olya' : 'Olexsandrivna',
    'Oleg' : 'Ivanovich',
    'Marina' : 'Olegivna',
    'Igor' : 'Maximovich',
    'Vita' : 'Viktorivna'
    }
name_inp = str(input('What is your name? '))

if name_inp in name_patronomic.keys():
    print ('Hello, ' , name_inp, name_patronomic[name_inp],'.')
else: 
    print("I don't know you")