#!/usr/bin/env python

#returns the count of lines that have no 
#words that are anagrams of each other

def main():
	input = """sayndz zfxlkl attjtww cti sokkmty brx fhh suelqbp
xmuf znkhaes pggrlp zia znkhaes znkhaes
nti rxr bogebb zdwrin
sryookh unrudn zrkz jxhrdo gctlyz
bssqn wbmdc rigc zketu ketichh enkixg bmdwc stnsdf jnz mqovwg ixgken
flawt cpott xth ucwgg xce jcubx wvl qsysa nlg
qovcqn zxcz vojsno nqoqvc hnf gqewlkd uevax vuna fxjkbll vfge"""
	
	input_array = str(input).split('\n')
	result = 0
	for line in input_array:
		word_array = str(line).split(' ')
		if validate(word_array):
			result += 1
	print(result)

def anagramValidation(word0, word1):
	c0 = list(word0)
	d0 = list(word1)
	for c in c0:
		if c in d0:
			d0.remove(c)
	if len(d0) == 0:
		return True 
	return False
	

def validate(word_array):
	for word in word_array:
		count = 0
		for other_word in word_array:
			if len(word) == len(other_word):
				if anagramValidation(word, other_word):
					count += 1
		if count > 1:
			return False
	return True

if __name__ == "__main__":
    main()
