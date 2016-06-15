#! /usr/bin/python
#! coding: utf-8

import os	
clear = lambda: os.system('clear')
clear()

salir = 2

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
cobro = [0, 0, 0, 0, 0, 0]
cantVentas = [0, 0, 0, 0, 0, 0]
mmcDia = [0, 0, 0, 0, 0, 0]
v_max = 0
dia_max = 0

while salir != 1:

	for i in range (6):
		
		importe = 1
		acu = 0
		cant = 0
		print "--------------------------------"
		print "Día",dias[i]
		
		while importe != 0:
			
			importe = input("Ingrese cuanto cobro en esta venta: ")
			acu += importe
			cant += 1
			cobro[i] = acu
			cantVentas[i] = cant - 1
			if importe > mmcDia[i]:
				mmcDia[i] = importe
			if importe > v_max:
				v_max = importe			
				dia_max = dias[i]

		print "\nEn el", dias[i], "cobraste:", acu
		print "Vendiste",cantVentas[i],"unidades."
		print "El monto mayor cobrado del día es de:",  mmcDia[i]
		if dias[i] == "Sábado":
			monto = cobro[0] + cobro[1] + cobro[2] + cobro[3] + cobro[4] + cobro[5]
			prom = monto / 5
			print"\n---------------------------------"
			print "El monto total es:",monto
			print "El promedio del monto es de",prom
			print "La venta máxima es de",v_max,"el día",dia_max
			salir = input("\nDesea salir del programa?:\n1.Si\n2.No\n")
			while salir != 1 and salir != 2:
				print ""
				input("Error! Vuelve a introducir tu elección correctamente: ")
			if salir == 1:
				print "Nos vemos"