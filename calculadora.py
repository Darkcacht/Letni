#! coding: utf-8

import os

clear = lambda: os.system('clear')
clear()

def Calculadora():
	op()	
	 
def Num1():
	global num1
	num1 = input()

def Num2():
	global num2
	num2 = input()

def Sumar():
	global suma
	suma = float(num1 + num2)
	print "\n-------------------------------------------"
	print "El reultado es:",suma
	print "-------------------------------------------"

def Restar():
	global resta
	resta = float(num1 - num2)
	print "\n-------------------------------------------"
	print "El resultado es:",resta
	print "-------------------------------------------"

def Multiplicar():
	global multiplo
	multiplo = float(num1 * num2)
	print "\n-------------------------------------------"
	print "El resultado es:",multiplo
	print "-------------------------------------------"

def Dividir():
	global divisor
	divisor = float(num1 / num2)
	print "\n-------------------------------------------"
	print "El resultado es:",divisor
	print "-------------------------------------------"

def op():
	op = 1
	
	while op != 0:
		
		print "\nElige que operación deseas realizar:"
		print "\n0.Salir"
		print "1.Sumar"
		print "2.Restar"
		print "3.Multiplicar"
		print "4.Dividir"
		op = input()
	
		if op != 0:
			
			print "\nIngrese el número 1:"
			global num1
			Num1()
			
			print "\nIngrese el número 2:"
			Num2()
			
			if op == 1:
				Sumar()
			elif op == 2:
				Restar()
			elif op == 3:
				Multiplicar()
			elif op == 4:
				Dividir()
		elif op != 0 and op != 1 and op != 2 and op != 3 and op != 4:
			op = input("Elije correctamente la operación a realizar")
Calculadora()