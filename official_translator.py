#Challange is to make a tool that will read a text file and translate it to Japanese
#using a translation library so install that using pip install command  $ pip install translate

my_file = open('translations.txt')

read_file = my_file.read()
from translate import Translator
translator = Translator(to_lang="ja")
translation = translator.translate(read_file)
print(translation)
my_file.close()

