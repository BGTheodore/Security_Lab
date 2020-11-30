import math,fractions
from operator import itemgetter

class Coding:

	def encode(self, chars):
		nums = []
		for char in chars:
			char = char.upper()
			nums.append(ord(char) - ord('A'))
		return nums
		
	def decode(self, nums):
		chars = []
		for num in nums:
			chars.append(chr(num + ord('A')))
		return chars

	def diff(self,a,b):
		if ord(a) > ord(b):
			return ord(a)-ord(b)
		else:
			return ord(b)-ord(a)

class Vigenere:

	def __init__(self,filenameenc="/home/altidor/Documents/Projects/Security_Lab-main/Vigenere/enc.txt",filenamedec="/home/altidor/Documents/Projects/Security_Lab-main/Vigenere/dec.txt"):
		self.msg = self.getText(filenameenc)
		self.ciph = self.getText(filenamedec)
		self.ce = Coding()
		self.setup()
				

	def getText(self,filename):
		result_f = open(filename)
		ciph = ""	
		for line in result_f:
			ciph = ciph + line.strip("\n")
		ciph.upper()
		return ciph

	def setup(self):
		self.setAlphabet()
		self.setAlphabetFreq()
		self.setDigrams()
		self.setTrigrams()
		self.count = self.makecount()
		self.makeTrigramCount()

	def cryptAnalysis(self):
		print ("Results of kasiski test:")
		self.kasiski()
		print("")
		print ("Results of Index of Coincidence test")
		self.ioc(self.keylen)

	def setAlphabet(self):
		self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	def setAlphabetFreq(self):
		self.alphabetFreq =  {'A':0.082, 'B':0.015,'C':0.028, 'D':0.043, 'E':0.127, 'F':0.022, 'G':0.020, 'H':0.061, 'I':0.070, 'J':0.002, 'K':0.008, 'L':0.040, 'M':0.024, 'N':0.067, 'O':0.075, 'P':0.019, 'Q':0.001, 'R':0.060, 'S':0.063, 'T':0.091, 'U':0.028, 'V':0.010, 'W':0.023, 'X':0.001, 'Y':0.020, 'Z':0.001}
		self.freq = []
		for char, freq in self.alphabetFreq.iteritems():
			self.freq.append(freq) 
		
	def checkAlphFreq(self):
		sum = 0
		for char,freq in self.alphabetFreq.iteritems():
			sum = float(float(sum) + freq)
		print (sum)

	def setDigrams(self):
		self.digrams = []
		for i in range((len(self.ciph)-2)):
			if self.ciph[i:(i+2)] not in self.digrams:
				self.digrams.append(self.ciph[i:(i+2)])
			
	def setTrigrams(self):
		self.trigrams = []
		for i in range((len(self.ciph)-3)):
			if self.ciph[i:(i+3)] not in self.trigrams:
				self.trigrams.append(self.ciph[i:(i+3)])

	def gcdOfNumbers(self,matrix):
		gcdNumber = matrix[0]
		for i in range(1, len(matrix)):
			gcdNumber = fractions.gcd(gcdNumber, matrix[i])
		return gcdNumber

	def IsNumber(self,number):
		try:
			int(number)
			return True
		except ValueError:
			return False

	# number of instances of a letter or small phrase (th, the, etc...) in a text
	def numberOfInstances(self,ciph, phrase):
	    num = 0
	    lenarray = len(ciph)-len(phrase) # to not end up outside array
	    for i in range(lenarray):
	        if(ciph[i:(i+len(phrase))]) == phrase:
	            num = num + 1
	    return num

	def makecount(self,text = ""):
		if(text == ""):
			text = self.ciph
		count = []
		for char in self.alphabet:
			count.append([char,self.numberOfInstances(text,char)])
		count.sort(key=itemgetter(1), reverse=True)
		return count

	def makeTrigramCount(self):
		self.trigramcount = self.countPhrase(self.trigrams)
		self.trigramcount.sort(key=itemgetter(1), reverse=True)

	def countPhrase(self,phrases):
		phraseCount = []
		for phrase in phrases:
			phraseCount.append([phrase,self.numberOfInstances(self.ciph,phrase)])
		return phraseCount

	def kasiski(self):
		self.makeTrigramCount()
		lengths = []
		for i in range(len(self.ciph)):
			if self.ciph[i:(i+len(self.trigramcount[0][0]))] == self.trigramcount[0][0]:
				for j in range((i+1),len(self.ciph)):
					if self.trigramcount[0][0] == self.ciph[j:(j+len(self.trigramcount[0][0]))]:
						lengths.append((j-i))					
				break	
		self.keylen = self.gcdOfNumbers(lengths)
		print ("Most occuring trigram: " + self.trigramcount[0][0] + ", with " + str(self.trigramcount[0][1]) + " occurences.")
		print ("Lengths for " + self.trigramcount[0][0] + ": " + ''.join(str(lengths)))
		print ("Gcd of lengths: " + str(self.keylen))

	def ioc(self,guess):
		self.makeSubstrings(guess)
		print ("Substrings: ") 
		print (", ".join(self.substrings))
		print ("Index of coincidences: ")
		for i in range(guess):
			self.iocCalc(self.substrings[i])
		
	def makeSubstrings(self,guess):
		self.substrings = ['']*guess
		for i in range(len(self.ciph)):
			self.substrings[(i%guess)] = self.substrings[(i%guess)] + self.ciph[i]

	def iocCalc(self,text):
		count = self.makecount(text)
		strLength = len(text)
		result = 0
		for letter,nr in count:
			result = result + (nr*(nr-1))
		divisor = (strLength*(strLength-1))
		result = float(float(result)/float(divisor))
		print (result)

	def findDecryptionKeys(self,guess):
		self.makeSubstrings(guess)
		self.decKeys = []
		for i in range(guess):
			print ("Substring: " + self.substrings[i])
			print ("Values g: M_g")
			self.decKeys.append(self.calcMg(self.substrings[i]))
		print ("Proposed keys: " )
		print (", ".join(str(x) for x in self.decKeys))

	def calcMg(self,text):
		count = self.makecount(text)
		count.sort(key=itemgetter(0))
		cand = float(0)
		strLength = len(text)
		M_g = []
		dist = 1
		res = -1
		for g in range(26):
			cand = 0
			for char, freq in count:
				coding = (self.ce.encode(char)[0] + g)%26
				relFreq = float(count[coding][1])/float(strLength)
				prod = float(relFreq*self.alphabetFreq[char])
				cand = float(cand + prod)
				if char == "0":
					print (char)
					print (g)
					print (coding)
					print (relFreq)
					print( prod)
					print (cand)
			M_g.append(str(g) + ": " + str(cand))

			if abs(float(cand - 0.065)) < dist:
				dist = abs(float(cand-0.065))
				res = g
		print (",	".join(M_g[0:9]))
		print (",	".join(M_g[9:18]))
		print (",	".join(M_g[18:26]))
		return res



	def decrypt(self,keys):		
		nums = self.ce.encode(list(self.ciph))
		for i in range(len(nums)):
			nums[i] = (nums[i] - keys[(i%len(keys))])%26
		plaintext = self.ce.decode(nums)	
		print( ''.join(plaintext))

	def encrypt(self,keys):
		nums = self.ce.encode(list(self.msg))
		for i in range(len(nums)):
			nums[i] = (nums[i] + keys[(i%len(keys))])%26
		cipher = self.ce.decode(nums)
		print (''.join(cipher))
		
	# Print contents of the table sorted by keys with k rows.
	def printTable(self,lst, k):
		output = []
		for i in range(k):
			output.append([])
		for i in range(len(lst)):
			item = lst[i][0] + ": " + str(lst[i][1]) + "	"
			output[(i%k)].append(item)
		for i in range(k):
			print (''.join(output[i]))
		print(" ")

	def printCount(self):
		self.printTable(self.count,3)

	def printTrigramCount(self):
		self.printTable(self.trigramcount,int((math.floor((len(self.trigramcount)+1)/35))))

print ("")

cs = Vigenere()
cs.cryptAnalysis()