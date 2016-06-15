#!/usr/bin/env python
#! coding: utf-8

import os

clear = lambda: os.system('clear')

clear()

print "Bienvenido"
print "----------"

salir = 2

while salir != 1:
	
	num = input("\nIngrese el número: ")

	n = input("\nHasta que número los quieres multiplicar?: ")

	print ""

	for n in range(1, n + 1):
		print num,"x",n,"=",(num * n)

	print ""
	salir = input("Desea salir?:\n1.Si\n2.No\n")
	while salir != 1 and salir != 2:
		print ""
		salir = input("Error! vuelve a introducir correctamente: ")
	if salir == 1:
		print "\nNos vemos\n"