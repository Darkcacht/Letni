#! /usr/bin/python
#! coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

def dibujo(x,y):
	
	matriz = [[carac for i in range(x)] for j in range(y)]
	for d in range(y):
		print ("".join(str(x) for x in matriz[d]))

alto = input("Ingrese la cantidad de caracteres que tendrá su figura de alto\n--> ")
ancho = input("Ingrese la cantidad de caracteres que'tendrá su figura de ancho\n--> ")
carac = raw_input("Ingrese el caracter de la figura\n-->")
dibujo(ancho, alto)