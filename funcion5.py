#! /usr/bin/python
#! coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

def ordenar(x, y):
	pares = sorted(x)
	impares = sorted(y)
	print pares
	print impares

def lista():
	
	num = 0
	pares = []
	impares = []

	while num != "":
		
		num = raw_input("Ingrese un número: ")
		if num != "":
			if int(num) % 2 == 0:
				pares.append(num)
			else:
				impares.append(num)

			ordenar(pares,impares)
	if num == "":
		print "Nos vemos"
lista()