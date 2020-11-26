from language_detector import detect_language
from textwrap import wrap
import re

# Driver code 
if __name__ == "__main__": 
        
        string = "SOQSSYFDFDMJORCQ"
        for size in range (1,6):
            splited = wrap(string,size)
        #ciphertext_to_int= [ord(i) for i in string]
        #splited = wrap(ciphertext_to_int,2)
        #re.findall('..?', ciphertext_to_int)
        print(splited)
                

    