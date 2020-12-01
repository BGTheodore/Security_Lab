#Vignere encryption with only upper case characters
def vignere(txt='', key='', typ=''):
    if not txt:
        print ("Veuillez entrer un text.")
        return
    if not key:
        print ("Veuillez fournir une cle.")
        return
    if typ not in ('d', 'e'):
        print ("""Veullez choisir "d" pour decryption ou "e" pour encryption""")
        return

    
    key_to_int = [ord(i) for i in key]
    txt_to_int = [ord(i) for i in txt]
    resultat = ''
    for i in range(len(txt_to_int)):
        shift =key_to_int[i % len(key)]
        if typ == 'd':
            shift *= -1

        v = (txt_to_int[i] + shift) % 255

        resultat += chr(v )

    return (resultat)
# Driver code 
if __name__ == "__main__": 
    with open('/home/altidor/Documents/Projects/Security_Lab-main/Vigenere/Betes.txt', 'r') as file:
       string = file.read().replace('\n', ' ').replace ("""’""", " ")
    key = "ti"
    q = vignere(string,  key, 'e')
    with open('/home/altidor/Documents/Projects/Security_Lab-main/Vigenere/coded.txt', 'w') as file:
        string = file.write(q)
    print (vignere(q, key, 'd'))