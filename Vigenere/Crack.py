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

def Validate(plaintext):
    result = detector.FindLanguage(text=plaintext)  
    if result.is_reliable :
        print ("Le resultat du dechiffrement est fiable a {:.2f} % .".format(result.probability*100))
    else :
        print("Le resultat du dechiffrement est peu fiable ({:.2f} %).Veuillez essayer avec un block de texte plus long.".format(result.probability*100))
    return result.is_reliable 
resultat = CesarCrack("Ni$xiwxi$qe$gpi$ix$ni$glerxi$zsmpe$pe$vitsrwiNi$xiwxi$p+epksvmxlqi$0xiwx$56$xiwx%")
print ("Plaintext : ",resultat)
Validate(resultat)