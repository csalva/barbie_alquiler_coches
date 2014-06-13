__author__ = 'cristina'

from coches import Coche

def menu():
	print("Barbie alquiler de coches")
	print("-------------------------")
	print("1. Alquilar coche")
	print("2. Ver los coches disponibles")
	print("3. Listar los coches alquilados en este momento")
	print("4. Añadir nuevo coche")
	print("5. Conocer ingresos totales obtenidos en un periodo de fechas")
	print("6. Salir")

menu()
opcion = str(input())

if opcion == "1":
	print("Has seleccionado alquilar un coche")
	

if opcion == "2":
	print("Has seleccionado ver los coches disponibles")
	print("-------------------------------------------")
	with open('coches.txt', mode='r', encoding='utf-8')as archivo:
		for i in archivo:
			matricula,marca,modelo,precioDia,disponible = i.split('-',4);
			if disponible == "si":
				print(matricula,marca,modelo,precioDia,disponible)
			else:
				print("Error")
					
if opcion == "3":
	print("Has seleccionado listar los coches alquilados en este momento")
	print("-------------------------------------------------------------")
	

if opcion == "4":
	print("Has seleccionado añadir un coche")
	print("--------------------------------")
	print("Introduce la matricula del coche")
	matricula = str(input())
	print("Introduce la marca del coche")
	marca = str(input())
	print("Introduce el modelo del coche")
	modelo = str(input())
	print("Introduce el precio por dia")
	precioDia = str(input())
	print("Introduce si esta disponible (SI/NO)")
	disponible = str(input())
	coches = Coche(matricula,marca,modelo,precioDia,disponible)
	coches.altaCoche()
		
if opcion == "5": 
	print("Has seleccionado conocer los ingresos totales en un periodo de fechas")  
    
if opcion == "6":
		print("Adios")
