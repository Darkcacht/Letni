#!/usr/bin/env python
#! coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

salir = 2

while salir != 1:
	
	cad = raw_input("Ingrese un texto: ")
	largo = len(cad)
	for i in range(1, largo):
		print(cad[:i])
	for i in range(largo, 0, -1):
		print(cad[:i])
	salir = input("Desea salir del programa?:\n1.Si\n2.No\n-->")
    
	while salir != 1 and salir != 2:
		salir = input("ERROR!\nIngrese tu elección correctamente: ")
	if salir == 1:
		print "Nos vemos"