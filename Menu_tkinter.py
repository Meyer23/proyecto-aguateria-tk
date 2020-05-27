from Metodos_tk import *
from tkinter import *
import tkinter.messagebox as tk

class Aplicacion:

	def __init__(self,ventana):
		self.ventana = ventana
		self.ventana.title('Aguateria Vecinal')
		self.ventana.geometry("640x480+0+0")
		self.windows()
		self.metodos=AguateriaVecinal()

	def windows(self):
		
		'''Se crea la barra de menu que contiene todas 
		las opciones del programa'''
		
		barraMenu = Menu(self.ventana,bg = 'white')
		self.ventana.config(menu=barraMenu)
		
		'''Se crean los menues principales'''
		menu_usuario=Menu(barraMenu, tearoff=0)
		barraMenu.add_cascade(label='Usuario',menu=menu_usuario)
		menu_empleado=Menu(barraMenu, tearoff=0)
		barraMenu.add_cascade(label='Empleado',menu=menu_empleado)
		menu_solicitud=Menu(barraMenu, tearoff=0)
		barraMenu.add_cascade(label='Solicitud',menu=menu_solicitud)
		menu_orden=Menu(barraMenu, tearoff=0)
		barraMenu.add_cascade(label='Orden',menu=menu_orden)
		menu_salir=Menu(barraMenu, tearoff=0)
		barraMenu.add_cascade(label='Salir',menu=menu_salir)
	



		'''Se agregan todas las opciones del menu Usuario'''

		menu_usuario.add_command(label='Agregar Usuario', command=self.agregar_usuario)
		menu_usuario.add_command(label='Buscar Usuario', command=self.buscar_usuario)
	
		'''Se agregan todas las opciones del menu Empleado'''
		
		menu_empleado.add_command(label='Agregar Empleado', command=self.agregar_empleado)
		menu_empleado.add_command(label='Buscar Empleado', command=self.buscar_empleado)

		'''Se agregan las opciones del menu Solicitud'''
		menu_solicitud.add_command(label='Solicitar Conexión', command=self.agregar_solicitud_conexion)
		menu_solicitud.add_command(label='Solicitar Desconexión', command=self.agregar_solicitud_desconexion)
		menu_solicitud.add_command(label='Solicitar Reparación', command=self.agregar_solicitud_reparacion)
		menu_solicitud.add_command(label='Buscar Solicitud', command=self.buscar_solicitud)

		'''Se agregan las opciones del menu Orden'''
		menu_orden.add_command(label='Generar Orden', command=self.generar_orden)
		menu_orden.add_command(label='Buscar Orden', command=self.buscar_orden)
		menu_orden.add_command(label='Modificar Orden', command=self.modificar_orden)



		'''Se agrega la opcion de Salir al menu Salir'''
		menu_salir.add_command(label='Salir',command=self.ventana.destroy)

	def agregar_usuario(self):

		self.metodos.agregar_usuario(self.ventana)

	def buscar_usuario(self):

		self.metodos.buscar_usuario(self.ventana)

	def agregar_empleado(self):

		self.metodos.agregar_empleado(self.ventana)

	def buscar_empleado(self):

		self.metodos.buscar_empleado(self.ventana)

	def agregar_solicitud_conexion(self):
		self.metodos.agregar_solicitud_conexion(self.ventana)

	def agregar_solicitud_desconexion(self):
		self.metodos.agregar_solicitud_desconexion(self.ventana)

	def agregar_solicitud_reparacion(self):
		self.metodos.agregar_solicitud_reparacion(self.ventana)

	def buscar_solicitud(self):
		self.metodos.buscar_solicitud(self.ventana)

	def generar_orden(self):
		self.metodos.generar_orden(self.ventana)

	def buscar_orden(self):
		self.metodos.buscar_orden(self.ventana)

	def modificar_orden(self):
		self.metodos.modificar_orden(self.ventana)
		
class Principal:
	def __init__(self): 
		'''Se crea la ventana principal'''
		self.raiz = Tk()
		'''Se carga la imagen principal a la ventana'''
		imgFondo=PhotoImage(file= "aguateria.png")
		lblFondo = Label(self.raiz, image=imgFondo).pack()
		aplicacion = Aplicacion(self.raiz)
		self.raiz.protocol("WM_DELETE_WINDOW", self.callback)
		self.raiz.resizable(0,0)
		self.raiz.mainloop()

	def callback(self):
	
		self.raiz.destroy()

if __name__ == '__main__':
	Principal()



