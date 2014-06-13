class Coche():
	def __init__(self, matricula, marca, modelo, precioDia, disponible):
		self.matricula = matricula
		self.marca = marca
		self.modelo = modelo
		self.precioDia = precioDia
		self.disponible = disponible
				
	def getMatricula(self):
		return self.matricula

	def getMarca(self):
		return self.marca
		
	def getModelo(self):
		return self.modelo
    
	def getPrecioDia(self):
		return self.precioDia
		
	def getDisponible(self):
		return self.disponible
		
	def altaCoche(self):
		registro = (self.matricula+"-"+self.marca+"-"+self.modelo+"-"+self.precioDia+"-"+self.disponible+"\n")
		with open('coches.txt', mode='a', encoding='utf-8')as archivo:
			archivo.write(registro)
			print(registro)
