#! /usr/bin/python
#! coding: utf-8}

import os 
clear = lambda: os.system('clear')
clear()

def palindromo(pal):

	if pal == pal[::-1]:
		print("True")
	else:
		print("False")

palindromo("neuquen")
