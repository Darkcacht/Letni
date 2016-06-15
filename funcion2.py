#! /usr/bin/python
#! coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

salir = 2

while salir != 1:
	def bisiesto():
	
		a = input("Dime el año: ")
		if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
			print "El año",a,"es bisiesto."
		else:
			print "El año",a,"no es bisiesto."

		salir = input("Desea salir del programa?:\n1.Si\n2.No\n-->")
			
bisiesto()