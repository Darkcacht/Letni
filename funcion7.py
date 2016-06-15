#! /usr/bin/python
#! coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

def contarVocales(palabra):

	contador = 0
	for letra in palabra:
		if letra == "A" or letra == "a":
			contador += 1
		elif letra == "E" or letra == "e":
			contador += 1
		elif letra == "I" or letra == "i":
			contador += 1
		elif letra == "O" or letra == "o":
			contador += 1
		elif letra == "U" or letra == "o":
			contador += 1

	return(contador)

print contarVocales("murcielago")