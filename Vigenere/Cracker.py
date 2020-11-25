from language_detector import detect_language

text = "Je suis en train de tester"
text =   ''.join(text.split())
language = detect_language(text)
print (language)
print (ord(""))