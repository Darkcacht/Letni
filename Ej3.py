#!/usr/bin/env python
#! coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

salir = 2

while salir != 1:
	
	ventas = 0
	monto_mayor_cobrado = 0

	Lunes = 0
	Martes = 0
	Miercoles = 0
	Jueves = 0
	Viernes = 0

	importeLunes = 1
	importeMartes = 1
	importeMiercoles = 1
	importeJueves = 1
	importeViernes = 1

	print "\n----------"
	print "Día Lunes:"
	while importeLunes != 0:
		
		importeLunes = int(raw_input("\nCuanto cobraste en la venta: "))
		Lunes = Lunes + importeLunes
		if importeLunes != 0: 
			ventas = ventas + 1
		if importeLunes > monto_mayor_cobrado:
			monto_mayor_cobrado = importeLunes

	print "\n-----------"
	print "Día Martes:"
	while importeMartes != 0:
		
		importeMartes = int(raw_input("\nCuanto cobraste en la venta: "))
		Martes = Martes + importeMartes
		if importeMartes != 0: 
			ventas = ventas + 1
		if importeMartes > monto_mayor_cobrado:
			monto_mayor_cobrado = importeMartes

	print "\n--------------"
	print "Día Míercoles:"
	while importeMiercoles != 0:
		
		importeMiercoles = int(raw_input("\nCuanto cobraste en la venta: "))
		Miercoles = Miercoles + importeMiercoles
		if importeMiercoles != 0: 
			ventas = ventas + 1
		if importeMiercoles > monto_mayor_cobrado:
			monto_mayor_cobrado = importeMiercoles

	print "\n-----------"
	print "Día Jueves:"
	while importeJueves != 0:	
		
		importeJueves = int(raw_input("\nCuanto cobraste en la venta: "))
		Jueves = Jueves + importeJueves
		if importeJueves != 0: 
			ventas = ventas + 1
		if importeJueves > monto_mayor_cobrado:
			monto_mayor_cobrado = importeJueves

	print "\n------------"
	print "Día Viernes:"
	while importeViernes != 0:
		
		importeViernes = int(raw_input("\nCuanto cobraste en la venta: "))
		Viernes = Viernes + importeViernes
		if importeViernes != 0: 
			ventas = ventas + 1
		if importeViernes > monto_mayor_cobrado:
			monto_mayor_cobrado = importeViernes


	print "\n-----------------------------"
	print "Los resultados son los siguientes:"

	total = Lunes + Martes + Miercoles + Jueves + Viernes
	print "\nEl monto total cobrado es:",total

	prom = (Lunes + Martes + Miercoles + Jueves + Viernes) / 5
	print "\nTienes un promedio de",prom,"cobrado por día."

	print "\nEl mondo mayor cobrado en la semana fue:",monto_mayor_cobrado

	if Lunes > Martes and Lunes > Miercoles and Lunes > Jueves and Lunes > Viernes:
		print "\nEl día mayor cobrado es el Lunes."

	if Martes > Lunes and Martes > Miercoles and Martes > Jueves and Martes > Viernes:
		print "\nEl día mayor cobrado es el Martes."

	if Miercoles > Lunes and Miercoles > Martes and Miercoles > Jueves and Miercoles > Viernes:
		print "\nEl día mayor cobrado es el Miercoles."

	if Jueves > Lunes and Jueves > Martes and Jueves > Miercoles and Jueves > Viernes:
		print "\nEl día mayor cobrado es el Jueves."

	if Viernes > Lunes and Viernes > Martes and Viernes > Miercoles and Viernes > Jueves:
		print "\nEl día mayor cobrado es el Viernes."

	print "\nHiciste un total de",ventas,"ventas."

	print "\n------------------------------"
	
	salir = input("Desea salir?:\n1.Si\n2.No\n")
	
	while salir != 1 and salir != 2:
		salir = input("Error!, vuelve a introducir su elección correctamente: ")
	
	if salir == 1:
		print "\nNos vemos\n"