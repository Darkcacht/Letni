#!/usr/bin/env python
# coding: utf-8

numero = 1

while numero < 10000:
	
	if numero < 10:
		print "000"+str(numero)
	elif numero < 100:
		print "00"+str(numero)
	elif numero < 1000:
		print "0"+str(numero)
	else:
		print numero
	
	numero *= 2
	