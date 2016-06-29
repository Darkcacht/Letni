#! /usr/bin/python
#! coding: utf-8

import os
clear = lambda: os.system('clear')
clear()


def contarVocales(x):

	contador = 0
	for letra in x:
		if letra == "A" or letra == "a":
			contador += 1
		elif letra == "E" or letra == "e":
			contador += 1
		elif letra == "I" or letra == "i":
			contador += 1
		elif letra == "O" or letra == "o":
			contador += 1
		elif letra == "U" or letra == "u":
			contador += 1

	if contador == 1:
		print "Esta palabra tiene", contador, "vocal"
	else:
		print "Esta palabra tiene", contador, "vocales"

pal = raw_input("Ingresa la palabra: ")
contarVocales(pal)
