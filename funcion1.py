#! /usr/bin/python
#! coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

salir = 2

while salir != 1:
	
	def buscar(lista, elemento):
		indice = None
		posicionFor = 0
		for elementolista in lista:
			if elementolista == elemento:
				indice = posicionFor
			posicionFor += 1
		return indice
	print buscar([8,9,12,45], 12) #Se puede poner lista o directamente el vector [8, 9, 12, 45]

	while salir != 1 and salir != 2:
		salir = input("Deseas salir del programa?\n1.Si\n2.No\n-->")
	if salir == 1:
		print "Nos vemos"
