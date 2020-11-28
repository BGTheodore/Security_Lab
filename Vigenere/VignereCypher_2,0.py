#Vignere code 2.0 ,can handle all ASCII symbol
import os

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

        v = (txt_to_int[i] - 32 + shift) % 223

        resultat += chr(v + 32)

    return (resultat)
# Driver code 
if __name__ == "__main__": 
    # texte = input("Veuillez choisir le fichier a encrypter: ")
   
    # try :
    #     dirname = os.path.dirname(__file__)
    #     filename = os.path.join(dirname, texte)
        
    #     with open(filename, 'r') as file:
    #         string = file.read().replace('\n', ' ')
    # except FileNotFoundError:
    #     print ("Erreur d'ouverture de fichier.")
    #     quit()
       
    string = "Les hommes et les femmes politiques, qu’ils soient de droite comme de gauche, s’accordent tous sur ce point : ils veulent protéger la laïcité."
    key = input("Veuillez entrer la cle : ")
    q = vignere(string,  key, 'e')
    with open('/home/altidor/Documents/Projects/Security_Lab-main/Vigenere/Cypher.txt', 'w') as file:
        string = file.write(q)
   
    print("Votre message a ete encrypte avec succes! Veuillez verifier le fichier Cypher.txt")
    