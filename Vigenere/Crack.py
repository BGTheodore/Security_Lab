#Crack that works for VignereCypher.py
import collections 
import gcld3
detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0, 
                                        max_num_bytes=1000)
def CesarKeyFinder(cypher):
    most_occuring_charater = collections.Counter(cypher).most_common(1)[0] #Find the most occuring letter
    shift = (ord(most_occuring_charater[0]) - ord ('e')) %240 #Maps it to "e" and gets the shift 
    return chr(shift)

def Validate(plaintext):
    result = detector.FindLanguage(text=plaintext)  
    if result.probability > 0.50 and result.language == 'fr':
        print ("Le resultat du dechiffrement est fiable a {:.2f} % .".format(result.probability*100))
        return True
    else:
        print("Le resultat du dechiffrement est peu fiable ({:.2f} %).".format(result.probability*100))
        return False
    

def TextSlicer(cypher,step): 
    C={}
    for i in range (0,step):
        C[i]=cypher[i::step]
    return C

def decryption(txt,key):
    key_to_int = [ord(i) for i in key]
    txt_to_int = [ord(i) for i in txt]
    resultat = ''
    for i in range(len(txt_to_int)):
        shift =key_to_int[i % len(key)]
        v = (txt_to_int[i] - shift) % 255

        resultat += chr(v)

    return (resultat)
# Driver code 
if __name__ == "__main__":    
    with open('/home/altidor/Documents/Projects/Security_Lab-main/Vigenere/coded.txt', 'r') as file:
       cypher = file.read()
    
    for size in range(1,10): #Size of the key
        Sliced = TextSlicer(cypher,size)
        key = ''
        for i in Sliced.keys():
            key +=CesarKeyFinder(Sliced[i])        
        print ("Possible Key with size",size,"is :",key)
        resultat = decryption(cypher,key)
        if Validate(resultat):
            test=input(">Entrez T pour terminer ou une autre touche pour continuer. : ")
            if (test.upper() == 'T'):
                print("Resultat de la decryption :")
                print(resultat)
                break
        
    