#text = 'Всю, Первую половину, 2022 - года'


#word = text.split()
#words = list(word)
#text = text.split()
#text = text.replace(',',"")
#text = text.replace('-',"")
#text = text.lower()
#text = text.split()
#text = text.lower()
#text = [x.lower() for x in text]



#b = text.capitalize()

#print(text)




value = 'Всю, Первую половину, 2022 - года'

stopwords = ['стало', 'истории', 'заявку', 'заявке', 'первую', 'стабильные', 'старт', 'чтобы', 'бяка']
word = value.replace(',', "")
word = word.replace('-', "")
word = word.lower()
words= word.split()
print(words)
if type(value) is str:
    for words in stopwords:
        value = value.replace(words, words[0] + "*" * (len(words) - 1))
#        value = value.replace(word.capitalize(), word[0] + "*" * (len(word) - 1))

else:
    raise ValueError('Ошибка, это не переменная строкого типа')

print(value)







