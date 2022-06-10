from Nepali_nlp import Unicode, Corrector
text = 'ma ghar jaanchhu'
print(Corrector().spell_correct(Unicode().unicode_word(text)))
