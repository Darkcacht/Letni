#! /usr/bin/python
#! coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

def ordenar(x):
	lista = sorted(x,reverse = True)
	print lista

def ingresar():
	aux = 0
	lista = []
	while (aux != ""):
		aux = raw_input("Ingrese un número: ")
		if (aux != ""):
			lista.append(int(aux))
	ordenar(lista)

ingresar() 