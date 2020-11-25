
#Function to do the encryption
#Takes the plaintext and key as parameter and returns the cypher

def encryption(plaintext,key):
    plaintext =  ''.join(plaintext.split()) #To remove all white spaces
    plaintext_to_int= [ord(i) for i in plaintext.upper()] #Converts the plaintext to an array of numeric values of the characters (Unicode)
                                               #Easier to manipulate 
    key_to_int = [ord(i) for i in key] #Same thing
    cipher = ''

    for i in range (len(plaintext_to_int)):  #Goes through all the plaintext
        cipher_int = (plaintext_to_int[i] + key_to_int[i% len(key)]) % 26 #Applies the key to the plaintext.modulo 26 cause of the alphabet length .
                                                                        #modulo len(key) cause the key is used as much time need to meet the plaintext length.
        cipher +=chr (cipher_int + 65) #Converts unicode back to character
        
    return cipher

def decryption(ciphertext,key):
    ciphertext =  ''.join(ciphertext.split()) #To remove all white spaces
    ciphertext_to_int= [ord(i) for i in ciphertext.upper()] #Converts the plaintext to an array of numeric values of the characters (Unicode)
                                               #Easier to manipulate 
    key_to_int = [ord(i) for i in key] #Same thing
    plain = ''
    for i in range (len(ciphertext_to_int)):  #Goes through all the cypher
        plain_int = (ciphertext_to_int[i] - key_to_int[i% len(key)]) % 26 #Applies the key to the plaintext.modulo 26 cause of the alphabet length .
                                                                        #modulo len(key) cause the key is used as much time need to meet the cyphertext length.
        plain +=chr (plain_int + 65)
        
    return plain


# Driver code 
if __name__ == "__main__": 
    string = "Testing the cypher"
    key = "test12" 
    cipher_text = encryption(string,key) 
    print("Ciphertext :", cipher_text) 
    plain_text = decryption(cipher_text,key) 
    print("Plaintext :", plain_text) 
    