#Crack that works for VignereCypher.py
import collections
import gcld3
detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0, 
                                        max_num_bytes=1000)

def CesarCrack(cipher):
    most_occuring_charater = collections.Counter(cipher).most_common(1)[0] #Find the most occuring letter
    shift = (ord(most_occuring_charater[0]) - ord ('e')) % 95 #Maps it to "e" and gets the shift 
    print ("The key is probably:",chr(95+shift))
    
    #decodes it
    ciphertext_to_int= [ord(i) for i in cipher]    
    plain = ''
    for i in range (len(ciphertext_to_int)):  #Goes through all the cypher
        plain_int = (ciphertext_to_int[i] - 32 - shift ) % 95 
        plain +=chr (plain_int + 32)
    return plain

def CesarKeyFinder(cypher):
    most_occuring_charater = collections.Counter(cypher).most_common(1)[0] #Find the most occuring letter
    shift = (ord(most_occuring_charater[0]) - ord ('e'))  #Maps it to "e" and gets the shift 
    return chr(shift% 95)

def Validate(plaintext):
    result = detector.FindLanguage(text=plaintext)  
    if result.is_reliable and result.language == 'fr':
        print ("Le resultat du dechiffrement est fiable a {:.2f} % .".format(result.probability*100))
    else :
        print("Le resultat du dechiffrement est peu fiable ({:.2f} %).".format(result.probability*100))
    return result.is_reliable 

def TextSlicer(cypher,step): 
    C={}
    for i in range (0,step):
        C[i]=cypher[i::step]
    return C

def decryption(ciphertext,key):
   # ciphertext =  ''.join(ciphertext.split()) #To remove all white spaces
    ciphertext_to_int= [ord(i) for i in ciphertext] #Converts the plaintext to an array of numeric values of the characters (Unicode)
                                               #Easier to manipulate 
    key_to_int = [ord(i) for i in key] #Same thing
    plain = ''
    for i in range (len(ciphertext_to_int)):  #Goes through all the cypher
        plain_int = (ciphertext_to_int[i] - 32 - key_to_int[i% len(key)]) % 95 #Applies the key to the plaintext.modulo 26 cause of the alphabet length .
                                                                        #modulo len(key) cause the key is used as much time need to meet the cyphertext length.
        plain +=chr (plain_int + 32)
        
    return plain


# Driver code 
if __name__ == "__main__":    
    cypher= """XNZI`RVZdXi[ZJZRV\^RaKVZiGf[Z"""
    # resultat = CesarCrack(cypher)
    # print ("Plaintext : ",resultat)
    # Validate(resultat)
   
    for size in range(2,10): #Size of the key
        Sliced = TextSlicer(cypher,size)
        key = ''
        for i in Sliced.keys():
            key +=CesarKeyFinder(Sliced[i])        
        print ("Possible Key with size",size,"is :",key)
        resultat = decryption(cypher,key)
        print(resultat)
    