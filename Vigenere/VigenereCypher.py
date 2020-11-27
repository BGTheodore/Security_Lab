# from language_detector import detect_language
#Function to do the encryption
#Takes the plaintext and key as parameter and returns the cypher

def encryption(plaintext,key):
    #plaintext =  ''.join(plaintext.split()) #To remove all white spaces
    plaintext_to_int= [ord(i) for i in plaintext] #Converts the plaintext to an array of numeric values of the characters (Unicode)
                                               #Easier to manipulate 
    key_to_int = [ord(i) for i in key] #Same thing
    cipher = ''

    for i in range (len(plaintext_to_int)):  #Goes through all the plaintext
        cipher_int = (plaintext_to_int[i] - 32 + key_to_int[i% len(key)]) % 95 #Applies the key to the plaintext.modulo 95 cause of all ASCII character .
                                                                        #modulo len(key) cause the key is used as much time need to meet the plaintext length.
        cipher +=chr (cipher_int + 32) #Converts ASCII back to character
        
    return cipher

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

def TextCleanup(message): 
    message = ''.join(message.split())
    message = message.replace ("\n", "").replace ("\r", "").replace ("\t", "").replace (" ", "").replace (",", "")
    message = message.replace (";", "").replace (":", "").replace (".", "").replace ("'", "").replace ("\"", "")
    message = message.replace ("-", "").replace ("!", "").replace ("?", "").replace ("(", "").replace (")", "")
    message = message.upper ()
    return message

# Driver code 
if __name__ == "__main__": 
    string = "check la tortue de la ville attaque"
    string = TextCleanup(string) 
    # with open('/home/altidor/Documents/Projects/Security_Lab-main/Vigenere/Betes.txt', 'r') as file:
    #     string = file.read().replace('\n', '')
    key = "te" 
    cipher_text = encryption(string,key) 
    print("Ciphertext :", cipher_text) 
    plain_text = decryption(cipher_text,key) 
    print("Plaintext :", plain_text) 
    # print (detect_language(plain_text))
    