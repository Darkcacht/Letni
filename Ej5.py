#! /usr/bin/python
#! coding: utf-8

import os

clear = lambda: os.system ('clear')
clear()

salir = 2

while salir != 1:
	ruedas = 1
	motos = 0
	totalCobrado = 0

	#Monto mayor cobrado por cabina
	mmcCab1 = 0
	
	#Los vehiculos pasados por cabina
	vehiculos1 = 0
	vehiculos2 = 0
	vehiculos3 = 0
	vehiculos4 = 0
	vehiculos5 = 0
	vehiculos = [0, 0, 0, 0, 0]


	#Las cabinas
	cab1 = 1  
	cab2 = 2
	cab3 = 3
	cab4 = 4
	cab5 = 5

	#Cuanto cobra cada cabina
	cab1Cobro = 0
	cab2Cobro = 0
	cab3Cobro = 0
	cab4Cobro = 0 
	cab5Cobro = 0

	print "\nBievenido"
	print "---------"
	valorxRueda = int(raw_input("\nIngrese el costo por rueda: "))

	#Mientras que el usuario no ingrese que el veículo tenga 0 ruedas se produce el bucle
	while ruedas != 0:
		ruedas = int(raw_input("\nIngrese la cantidad de ruedas que tiene el vehículo: "))
		if ruedas != 0:
			pase = True
		
		while pase == True:
			
			cab = int(raw_input("\nA que número de cabina se dirigió el vehículo?: "))
			
			coeficiente =  valorxRueda * ruedas
			
			if cab == cab1:
				if ruedas == 2:
					motos = motos + 1 
					vehiculos1 = vehiculos1 + 1
					totalCobrado = totalCobrado + coeficiente
					cab1Cobro = cab1Cobro + coeficiente
					if cab1Cobro > mmcCab1:
						mmcCab1 = cab1Cobro
					pase = False
				else: 
					vehiculos1 = vehiculos1 + 1
					totalCobrado = totalCobrado + coeficiente
					cab1Cobro = cab1Cobro + coeficiente
					if cab1Cobro > mmcCab1:
						mmcCab1 = cab1Cobro
					pase = False
			
			elif cab == cab2:
				if ruedas == 2:
					motos = motos + 1 
					vehiculos2 = vehiculos2 + 1
					totalCobrado = totalCobrado + coeficiente
					cab2Cobro = cab1Cobro + coeficiente
					if cab2Cobro > mmcCab1:
						mmcCab1 = cab2Cobro
					pase = False
				else: 
					vehiculos2 = vehiculos2 + 1
					totalCobrado = totalCobrado + coeficiente
					cab2Cobro = cab2Cobro + coeficiente
					if cab2Cobro > mmcCab1:
						mmcCab1 = cab2Cobro
					pase = False
			
			elif cab == cab3:
				if ruedas == 2:
					motos = motos + 1 
					vehiculos3 = vehiculos3 + 1
					totalCobrado = totalCobrado + coeficiente
					cab3Cobro = cab3Cobro + coeficiente
					if cab3Cobro > mmcCab1:
						mmcCab1 = cab3Cobro
					pase = False	
				else: 
					vehiculos3 = vehiculos3 + 1
					totalCobrado = totalCobrado + coeficiente
					cab3Cobro = cab3Cobro + coeficiente
					if cab3Cobro > mmcCab1:
						mmcCab1 = cab3Cobro
					pase = False

			elif cab == cab4:
				if ruedas == 2:
					motos = motos + 1 
					vehiculos4 = vehiculos4 + 1
					totalCobrado = totalCobrado + coeficiente
					cab4Cobro = cab4Cobro + coeficiente
					if cab4Cobro > mmcCab1:
						mmcCab1 = cab4Cobro
					pase = False
				else: 
					vehiculos4 = vehiculos4 + 1
					totalCobrado = totalCobrado + coeficiente
					cab4Cobro = cab4Cobro + coeficiente
					if cab4Cobro > mmcCab1:
						mmcCab1 = cab4Cobro
					pase = False
			
			elif cab == cab5:
				if ruedas == 2:
					motos = motos + 1 
					vehiculos4 = vehiculos4 + 1
					totalCobrado = totalCobrado + coeficiente
					cab5Cobro = cab5Cobro + coeficiente
					if cab5Cobro > mmcCab1:
						mmcCab1 = cab5Cobro
					pase = False
				else: 
					vehiculos4 = vehiculos4 + 1
					totalCobrado = totalCobrado + coeficiente
					cab5Cobro = cab5Cobro + coeficiente
					if cab5Cobro > mmcCab1:
						mmcCab1 = cab5Cobro
					pase = False
			
			else:
				print "\nError!, vuelve a elegir la cabina correctamente."
		
	txt = open("informeRAC.txt","w")

	#Resultados mostrados en pantalla
	print>> txt, "\nLa cabina 1: \nCobró:",cab1Cobro,"\nPasaron",vehiculos1,"vehículos"
	print>> txt, "\nLa cabina 2: \nCobró:",cab2Cobro,"\nPasaron",vehiculos2,"vehículos"
	print>> txt, "\nLa cabina 3: \nCobró:",cab3Cobro,"\nPasaron",vehiculos3,"vehículos"
	print>> txt, "\nLa cabina 4: \nCobró:",cab4Cobro,"\nPasaron",vehiculos4,"vehículos"
	print>> txt, "\nLa cabina 5: \nCobró:",cab5Cobro,"\nPasaron",vehiculos5,"vehículos"

	print>> txt, "\n-------------------------------------------------"

	print>> txt, "Se cobró",totalCobrado,"en total."
	print>> txt, "\nEl monto cobrado más alto es:",mmcCab1
	print>> txt, "\nPasaron",motos,"motos."
	vehiculos = vehiculos1 + vehiculos2 + vehiculos3 + vehiculos4 + vehiculos5
	print>> txt, "\nY el promedio es:",(totalCobrado / vehiculos)

	txt.close()
	
	print ""
	salir = input("Deseas salir del programa?:\n1.Si\n2.No\n")
	
	while salir != 1 and salir != 2:
		salir = input('Error! vuelve a introducir tu elección correctamente: ')
	if salir == 1:
		print "\nNos vemos"
#Final del programa