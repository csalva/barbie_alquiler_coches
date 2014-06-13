__author__ = 'cristina'

from coches import Coche
from transacciones import Alquiler

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
	print("----------------------------------")
	with open('coches.txt', mode='r', encoding='utf-8')as archivo:
		for i in archivo:
			matricula,marca,modelo,precioDia,disponible = i.split('-',4);
			print(matricula,marca,modelo,precioDia,disponible)
	print("Elige un modelo y introduce la matricula del coche")
	matricula2 = str(input())
	if matricula2 == matricula and disponible == "si":
		print("Introduce el nif del cliente")
		nif = str(input())
		print("Introduce la fecha de alquiler")
		fecha_alquiler = str(input())
		print("Introduce la fecha de retorno")
		fecha_retorno = str(input())
		
		transacciones = Alquiler(matricula,nif,fecha_alquiler,fecha_retorno)
		transacciones.altaAlquiler()
		transacciones.calcularImporte()
	
	else:
		print("Matricula mal introducida")
		

if opcion == "2":
	print("Has seleccionado ver los coches disponibles")
	print("-------------------------------------------")
	with open('coches.txt', mode='r', encoding='utf-8')as archivo:
		for i in archivo:
			matricula,marca,modelo,precioDia,disponible = i.split('-',5);
			if disponible == "SI":
				print(matricula,marca,modelo,precioDia,disponible)
			else:
				print(disponible+'z')
					
if opcion == "3":
	print("Has seleccionado listar los coches alquilados en este momento")
	print("-------------------------------------------------------------")
	with open('coches.txt', mode='r', encoding='utf-8')as archivo:
		for i in archivo:
			matricula,marca,modelo,precioDia,disponible = i.split('-',5);
			if disponible == "NO":
				print(matricula,marca,modelo,precioDia,disponible)
			else:
				print("Error")

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
	print("---------------------------------------------------------------------")
	print("Introduce la fecha 1")
	fecha1 = str(input()) 
	print("Introduce la fecha 2")
	fecha2 = str(input())
    
if opcion == "6":
		print("Adios")
