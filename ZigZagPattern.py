import time
from os import system, name

patternLen = int(input("Enter length of the pattern: "))
pattern = "*" * patternLen

def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def halfPattern(indentInc=True):
	if indentInc == True:
		indent = 0
		indentIncrement = 1
	else:
		indent = (patternLen - 2)
		indentIncrement = -1

	for i in range(patternLen-1):
		print(" " * indent, pattern, sep="")
		indent += indentIncrement

def fullPattern():
	halfPattern()
	halfPattern(False)

def fullPatternReverse():
	halfPattern(False)
	halfPattern()


#Clear the screen before starting animation
clear()
time.sleep(0.5)

#Animation
while True:
	fullPattern()
	time.sleep(1)
	clear()

	fullPatternReverse()
	time.sleep(1)
	clear()