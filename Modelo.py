#modelo.py

import persistent 
from abc import ABC, ABCMeta, abstractmethod
from Controlador import Controlador 


class Persona(persistent.Persistent, metaclass = ABCMeta): 
	
	'''Clase que define a una persona'''
	
	def __init__(self, cedula, nombre, apellido, direccion, contactos): 
		persistent.Persistent.__init__(self)
		self.cedula = cedula 
		self.nombre = nombre
		self.apellido = apellido
		self.direccion = direccion 
		self.contactos = contactos
		pass
		
	def mostrar_contactos(self, Contacto): 
		lista_contactos = [] 
		'''Retorna una lista de contactos'''
		for contacto in Contacto: 
			 lista_contactos = lista_contactos.append(Contacto)
		return (lista_contactos)
		
	def __str__(self): 
		
		'''Retorna los datos de la persona'''
		return "\nNombre: " +str(self.nombre)+ "\nApellido: " +str(self.apellido) +\
				"\nCedula: " +str(self.cedula)+ "\nDirección: " +str(self.direccion) +\
				"\nContactos: " +str(self.contactos) 
				
class Usuario(persistent.Persistent): 
	
	'''Clase que representa a los usuarios de la aguatería''' 
	
	def __init__(self, Persona): #Usuario se compone de Persona 
		persistent.Persistent.__init__(self)
		self.Persona = Persona
		
	def mostrar_usuario(self, Persona):
		return Persona.__str__()
		
class Empleado(persistent.Persistent): 
	
	'''Clase que representa a los empleados de la aguatería'''
	
	def __init__(self, Persona): #Empleado se compone de Persona
		persistent.Persistent.__init__(self)
		self.Persona = Persona
		
	def mostrar_empleado(self, Persona):
		return Persona.__str__()
		
class Contacto(persistent.Persistent, metaclass = ABCMeta): 
	
	'''Clase que representa a los contactos de los usuarios y empleados'''
	
	def __init__(self): 
		persistent.Persistent.__init__(self)
		pass 
	
	def __str__(self):
		pass 
		
		
class Telefono(Contacto): #Telefono hereda de la clase Contacto
	
	'''Clase que contiene los numeros telefónicos de los usuarios y empleados'''
	
	def __init__(self, nroTelefono):
		persistent.Persistent.__init__(self)
		self.nroTelefono = nroTelefono
		pass
	
	def __str__(self): 
		return "Número telefónico: " +str(self.nroTelefono) 
		
class CorreoElectronico(Contacto): 
	
	'''Clase que contiene las direcciones de correo de los usuarios y empleados'''
	
	def __init__(self, email): 
		persistent.Persistent.__init__(self)
		self.email = email 
		pass 
		
	def __str__(self): 
		return "Dirección de e-mail: " +str(self.email)
		
class Solicitud(persistent.Persistent, metaclass = ABCMeta): 
	
	'''Clase que representa las solicitudes de los usuarios de la aguatería''' 
	
	def __init__(self, cedula, descripcion, fecha): 
		persistent.Persistent.__init__(self)
		self.cedula = cedula
		self.descripcion = descripcion
		self.fecha = fecha
		pass 
		
	def __str__(self):
		return '\nNro. C.i Cliente: ' +str(self.cedula) +'\nDescripción: ' +str(self.descripcion) +'\nFecha ingresada: ' +str(self.fecha) +' '
		
class Reparacion(Solicitud): 
	
	'''La clase reparacion hereda de Solicitud'''
	
	def __init__(self, detalles, fecha):
		persistent.Persistent.__init__(self)
		self.detalles = detalles 
		self.fecha = fecha 
		pass
		
	def __str__(self):
		return("Detalles :" +str(self.detalles) +" Fecha: " +str(self.fecha) +' ')
		
class Desconexion(Solicitud):
	
	'''La clase Desconexion hereda de Solicitud'''
	
	def __init__(self, detalles, fecha): 
		persistent.Persistent.__init__(self)
		self.detalles = detalles
		self.fecha = fecha 
		pass
	
	def __str__(self):
		return("Detalles: " +str(self.detalles) +" Fecha: " +str(self.fecha) +' ')
		
class Conexion(Solicitud): 
	
	'''La clase Conexion hereda de Solicitud''' 
	
	def __init__(self, fecha): 
		persistent.Persistent.__init__(self)
		self.fecha = fecha 
		pass
		
	def __str__(self): 
		return("Fecha: " +str(self.fecha) +' ')
		
class Orden(persistent.Persistent): 
	
	'''Método que representa las ordenes de trabajo que puede generar la aguatería'''
	
	def __init__(self, cedula, descripcion, fecha, direccion, estado_terminado):
		 persistent.Persistent.__init__(self)
		 self.cedula = cedula 
		 self.descripcion = descripcion
		 self.fecha = fecha 
		 self.direccion = direccion
		 self.estado_terminado = estado_terminado
		 
	def __str__(self): 
		return("\nFecha a ejecutarse la orden: " +str(self.fecha)+ "\nDescripcion: " +str(self.descripcion) +"\nDirección del cliente: "+str(self.direccion) +"\nNro C.i Empleado a cargo: " +str(self.cedula) +"\nEstado de la orden: " +str(self.estado_terminado))
		
class Ong(persistent.Persistent, metaclass=ABCMeta):
    """NULL"""

    def __init__(self, denominacion):
        persistent.Persistent.__init__(self)
        self.denominacion = denominacion
        pass

    def __str__(self):
        return "\nOrganización.\n" + super().__str__() + "\n"

"""Clase Aguatería hereda de Organizacion"""

class Aguateria(Ong):
    def __init__(self, empleados, usuarios, solicitudes, ordenes):
        persistent.Persistent.__init__(self)
        super().__init__(**kwargs)
        self.empleados = empleados
        self.usuarios = usuarios
        self.soliticudes = solicitudes
        self.ordenes = ordenes
        pass

    def __str__(self):
        return "\nOrganizacion - Aguatería Vecinal.\n" + super().__str__() + "\n"
