import collections
import gcld3
detector = gcld3.NNetLanguageIdentifier(min_num_bytes=0, 
                                        max_num_bytes=1000)
def key_finder(cipher , level):
    most_occuring_charater = collections.Counter(cipher).most_common(level)[0] #Find the most occuring letter
    print ("The key is probably: ",most_occuring_charater[0])
    shift = (ord(most_occuring_charater[0]) - ord ('e')) % 95 #Maps it to "e" and gets the shift 
    return shift

def CesarDecoder(cipher,shift):    
    #decodes it
    ciphertext_to_int= [ord(i) for i in cipher]    
    plain = ''
    for i in range (len(ciphertext_to_int)):  #Goes through all the cypher
        plain_int = (ciphertext_to_int[i] - 32 - shift ) % 95 
        plain +=chr (plain_int + 32)
    return plain

def CesarCrack(cipher):
    result = detector.FindLanguage(text=CesarDecoder(cipher,key_finder (cipher,1)))
    if (result.language == 'fr' and result.is_reliable == True):
        print (text)
    else :
       print (CesarDecoder(cipher,key_finder(cipher,2)))


CesarCrack("Ni$xiwxi$p+epksvmxlqi$0xiwx$56$xiwx%")
