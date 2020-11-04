# 5. Обробка тексту
# Створити програму для обробки наступного тексту:
# - Вивести кількість речень у тексті
# - Підрахувати кількість слів «quis»
# - Підрахувати кількість символів з пробілами
# - Підрахувати кількість символів без пробілів
# - Вивести на екран перші 120 символів та додати «...» після останнього слова.
# Необхідно видалити останнє слово, якщо воно не буде виведено повністю.
''' 
sentences : number of sentences in the text
word_quis : number word «quis» in the text
symbols : number of symbols in the text
spaces_without: number of symbols without spaces in the text
shorten_text: reduction of text to 120 characters
'''
import textwrap
text = 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam,'\
' eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.'\
' Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos'\
' qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,'\
' adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.'\
' Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi'\
' consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel'\
' illum qui dolorem eum fugiat quo voluptas nulla pariatur?'

sentences1 = len(text.split('.'))-1
sentences2 = len(text.split('?'))-1
sentences3 = len(text.split('!'))-1
print ('In the text', sentences1 + sentences2 + sentences3, 'sentences')

find_world = 'quis'
word_quis = len(text.split(find_world))-1
print ('word «quis» in the text - ', word_quis, ' times')

symbols = len(text)
print ('symbols in the text = ', symbols) 
spaces_without = text.count(' ')
print ('symbols without spaces in the text = ', spaces_without)

shorten_text = textwrap.shorten(text, width=120, placeholder="...")
print (shorten_text)