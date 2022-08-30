# shmulik debby
# Calculate password strength using Entropy Formula
# https://generatepasswords.org/how-to-calculate-entropy/

# get password lists from :
# https://weakpass.com/

"""
Numbers (0-9)														10
Lower Case Latin Alphabet (a-z)										26
Symbols 															33
Lower Case & Upper Case Latin Alphabet (a-z, A-Z)					52
Lower Case & Upper Case Latin Alphabet and numbers (a-z, A-Z, 0-9)	62
ASCII Printable Character Set (a-z, A-Z, symbols, space)			95
"""
 
import math
import sys,getopt
import mmap
helpTXT="""HELP
      Use python PasswordCalc.py [-p pass string] [-w]
      -p [password string] (if using escape charecter use \" string \")
      -w For not searching in word list

      -h View this help"""

# Define colors
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBackRed(skk): print("\033[101m {}\033[00m" .format(skk))

#main
def main(argv):
	CheckWordListFile = True

	opts, args = getopt.getopt(argv,"whp:") # for help see https://stackabuse.com/command-line-arguments-in-python/ 

	for opt, arg in opts:
		if opt == '-h': #print help
			print (helpTXT)
			sys.exit(1)
		elif opt =='-p': #get string
			passwd = arg
			if passwd == ' ':
				print (helpTXT)
		elif opt == '-w': #dont check word list
			CheckWordListFile = False

	CheckWord(passwd,CheckWordListFile)

#calculate text for score
def CheckWord(passwd,CheckWordListFile):
	prBackRed('Word Entrphy Calculator')
	if CheckWordListFile: #check file in word list
		if CheckWithFile(passwd) :
			prRed('! String found in password list file - it is recomended to replase it')
		else:
			print('String not found in password list')
	else:
		print('Not checking word list')
	upper, lower, digit, symbol = charCheck (passwd)
	EntropyScore = digit*10+upper*26+lower*26+symbol*33
	ScoreInt = math.log2(pow(EntropyScore,len(passwd)))
	FinalScore = f'{ScoreInt:.2f}'
	print ('Score= ', end='')
	if ScoreInt >0 and ScoreInt <20:
		prRed (FinalScore)
	elif ScoreInt >20.1 and ScoreInt <40 :
		prCyan(FinalScore)
	elif ScoreInt >40.1 and ScoreInt <60 :
		prPurple(FinalScore)
	elif ScoreInt >60.1 and ScoreInt <80 :
		prYellow(FinalScore)
	else :
		prGreen(FinalScore)

#calculate charecters in text
def charCheck(text):
	upper = lower = digit = symbol = 0	
	for c in text:
			if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				upper = 1
			elif c in "abcdefghijklmnopqrstuvwxyz":
				lower = 1
			elif c in "0123456789":
				digit = 1
			else : 
				symbol = 1
	return (upper, lower, digit, symbol)

#check text agains word list
def CheckWithFile (text):
	passfile ='rockyou.txt'
	print('Testing string vs password list-', passfile)
	with open(passfile,"r") as temp_f:
		for line in temp_f:
			dataline = temp_f.readline().rstrip()
			if str(dataline) ==  str(text):
				return True # The string is found

if __name__=="__main__":

	if len(sys.argv) == 1: #no arguments
		print ('No arguments\n',helpTXT)
	else:		
		try:
			main(sys.argv[1:])
		except IndexError:
			#if index of a sequence is out of range.
			print ('Aruments error\n',helpTXT)
			sys.exit(1)
