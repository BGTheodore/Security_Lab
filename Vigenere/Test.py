import collections
with open('/home/altidor/Documents/Projects/Security_Lab-main/Vigenere/kant.txt', 'r') as file:
       s = file.read()
print( s)
print(collections.Counter(s).most_common(2))