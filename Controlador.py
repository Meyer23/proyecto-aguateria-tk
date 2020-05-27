import BTrees.OOBTree
import persistent, transaction
from abc import ABCMeta, abstractmethod

from baseDatos import get_root_zodb

class Controlador(persistent.Persistent):

	'''-----------Controlador Padre---------------------------------'''
	__diccionario_objetos = None
	
	def crear(self, objeto):
		'''-----------Metodo para crear un objeto-----------'''
		self.validar_insercion(objeto)
		self.get_diccionario_objetos()[self.get_codigo_objeto(objeto)] = objeto
		transaction.commit()
	
	def modificar(self, objeto):

		self.validar_actualizacion(objeto)
		del self.get_diccionario_objetos()[self.get_codigo_objeto(objeto)]
		self.get_diccionario_objetos()[self.get_codigo_objeto(objeto)] = objeto
		transaction.commit()
	
	def borrar(self, objeto):
		self.validar_eliminacion(objeto)
		del self.get_diccionario_objetos()[self.get_codigo_objeto(objeto)]
		transaction.commit()
		
	def get_diccionario_objetos(self):
		if not self.__diccionario_objetos:
			'''----Cada clase posee su propio diccionario-----'''
			nombreDiccionario = self.__class__.__name__
			if not hasattr(get_root_zodb(), nombreDiccionario):
				'''----Atributo para root que tiene el nombre de la clase-----'''
				setattr(get_root_zodb(), nombreDiccionario, BTrees.OOBTree.BTree())
			
			self.__diccionario_objetos = getattr(get_root_zodb(), nombreDiccionario)
		return self.__diccionario_objetos

	def get_lista_objetos(self):
		return self.get_diccionario_objetos().values()

	@abstractmethod
	def get_codigo_objeto(self, objeto):
		pass

	@abstractmethod
	def validar_insercion(self, objeto):
		pass

	@abstractmethod
	def validar_actualizacion(self, objeto):
		pass
		
class ControladorUsuario(Controlador):
	
	def get_codigo_objeto(self, usuario): 
		return usuario.cedula
	
	def validar_insercion(self, usuario):
		if usuario.cedula in self.get_diccionario_objetos().keys():
			return False 
		else: 
			return True 
			
	def validar_actualizacion(self, usuario): 
		if usuario.cedula in self.get_diccionario_objetos().keys():
			return False
		else: 
			return True
	
	def buscar_usuario(self, cedula): 
		for usuario in self.get_lista_objetos():
			if usuario.cedula == cedula:
				return usuario

class ControladorEmpleado(Controlador):
	
	def get_codigo_objeto(self, empleado):
		return empleado.cedula 
		
	def validar_insercion(self, empleado):
		if empleado.cedula in self.get_diccionario_objetos().keys():
			return False
		else:
			return True
			
	def validar_actualizacion(self, empleado): 
		if empleado.cedula in self.get_diccionario_objetos().keys():
			return False
		else: 
			return True
			
	def buscar_empleado(self, cedula):
		for empleado in self.get_lista_objetos():
			if empleado.cedula == cedula:
				return empleado
				
class ControladorSolicitud(Controlador):
	
	def get_codigo_objeto(self, solicitud):
		return solicitud.cedula 
		
	def validar_insercion(self, solicitud):
		if solicitud.cedula in self.get_diccionario_objetos().keys():
			return False
		else: 
			return True
			
	def validar_actualizacion(self, solicitud): 
		if solicitud.cedula in self.get_diccionario_objetos().keys():
			return False
		else: 
			return True
	
	def buscar_solicitud(self, cedula): 
		for solicitud in self.get_lista_objetos(): 
			if solicitud.cedula == cedula: 
				return solicitud
			
class ControladorOrden(Controlador):
	
	def get_codigo_objeto(self, orden):
		return orden.cedula
	
	def validar_insercion(self, orden):
		if orden.cedula in self.get_diccionario_objetos().keys():
			return False
		else:
			return True
			
	def validar_actualizacion(self, cedula):
		for orden in self.get_lista_objetos():
			if orden.estado_terminado == 'Sin ejecutar':
				orden.estado_terminado = 'Ejecutado'
				return True
			
	def buscar_orden(self, cedula): 
		for orden in self.get_lista_objetos(): 
			if orden.cedula == cedula: 
				return orden
		 
			

			
			
	
