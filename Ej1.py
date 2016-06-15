#!/usr/bin/env python
#! coding: utf-8

import os

clear = lambda: os.system('clear')

clear()

print "Bienvenido"
print "----------"

salir = 2

while salir == 2:

	num = input("\nIngrese un número: ")

	print " "

	for i in range(1,11):
		print num,"x",i,"=",(num * i)

	print "\nDesea salir?:"
	print "1.Si"
	print "2.No"
	salir = input()
	while salir != 1 and salir != 2:
		print ""
		salir = input("Error!, vuelve a introducir tu elección correctamente: ")
	if salir == 1:
		print "\nNos vemos\n"