class Alquiler():
	def __init__(self, matricula, nif, fecha_alquiler, fecha_retorno):
		self.matricula = matricula
		self.nif = nif
		self.fecha_alquiler = fecha_alquiler
		self.fecha_retorno = fecha_retorno
		
	def getMatricula(self):
		return self.matricula

	def getnif(self):
		return self.nif
		
	def getFechaAlquiler(self):
		return self.fecha_alquiler
    
	def getFechaRetorno(self):
		return self.fecha_retorno
		
	def altaAlquiler(self):
		registro = (self.matricula+"-"+self.nif+"-"+self.fecha_alquiler+"-"+self.fecha_retorno+"\n")
		with open('movimientos.txt', mode='a', encoding='utf-8')as archivo:
			archivo.write(registro)
			print(registro)
	
	def calcularImporte(self):
		with open('coches.txt', mode='r', encoding='utf-8')as archivo:
			for i in archivo:
				matricula,marca,modelo,precioDia,disponible = i.split('-',4);
			
		importe = precioDia*(self.fecha_retorno-self.fecha_alquiler)
		print("El importe total de los dias seleccionados es de: "+importe)
