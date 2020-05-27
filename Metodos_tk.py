from tkinter import *
import tkinter.messagebox as tk
from Modelo import *
from Controlador import *

class AguateriaVecinal():

        #Agregar adoptante para Perros

        def agregar_usuario(self, ventana):
                
                cedula = IntVar()
                nombre = StringVar()
                apellido = StringVar()
                direccion = StringVar()
                nrotelefono = StringVar()
                descripcion = StringVar()
                
                popup4=Toplevel(ventana)
                popup4.title('Datos de Usuario')
                popup4.geometry('400x200+0+0')
                
                                



                lblcedula = Label(popup4,text= 'Cedula:')
                lblcedula.grid(row=2,column=1,sticky=W)
                
                edtcedula = Entry(popup4, textvariable = cedula)
                edtcedula.grid(row=2,column=2,sticky=W)

                lblnombre = Label(popup4,text= 'Nombre ')
                lblnombre.grid(row=3,column=1,sticky=W)
                
                edtnombre = Entry(popup4, textvariable = nombre)
                edtnombre.grid(row=3,column=2,sticky=W)
                
                lblapellido = Label(popup4,text= 'Apellido:')
                lblapellido.grid(row=4,column=1,sticky=W)
                
                edtapellido = Entry(popup4, textvariable = apellido)
                edtapellido.grid(row=4,column=2,sticky=W)

                lbldireccion = Label(popup4,text= 'Direccion:')
                lbldireccion.grid(row=5,column=1,sticky=W)
                
                edtdireccion = Entry(popup4, textvariable = direccion)
                edtdireccion.grid(row=5,column=2,sticky=W)

                lblnrotelefono = Label(popup4,text= 'Nro Teléfono:')
                lblnrotelefono.grid(row=6,column=1,sticky=W)
                
                edtnrotelefono = Entry(popup4, textvariable = nrotelefono)
                edtnrotelefono.grid(row=6,column=2,sticky=W)

                lbldescripcion = Label(popup4,text= 'Correo:')
                lbldescripcion.grid(row=7,column=1,sticky=W)
                
                edtdescripcion = Entry(popup4, textvariable=descripcion)
                edtdescripcion.grid(row=7,column=2,sticky=W)
                        
                
                btnGuardar = Button(popup4, text = 'Guardar', 
                command=lambda: self.confirmar_agregar_usuario(popup4, nombre.get(), apellido.get(), cedula.get(), direccion.get(), nrotelefono.get(), descripcion.get(), ) )
                btnGuardar.grid(row=11, column=1)
                btnCancelar = Button(popup4, text = 'Cancelar', command=lambda: popup4.destroy())
                btnCancelar.grid(row=11, column=2)


        def confirmar_agregar_usuario(self, popup, nombre, apellido, cedula, direccion, nrotelefono, descripcion):

                controladorUsuario = ControladorUsuario()
                usuario_buscado = controladorUsuario.buscar_usuario(cedula)

                if usuario_buscado is None:
                        contactos = [str(nrotelefono), str(descripcion)]
                        usuario_controlador = ControladorUsuario()
                        nuevo_usuario = Persona(nombre=nombre, apellido=apellido, cedula=cedula, direccion=direccion, contactos=contactos)
                        usuario_controlador.crear(nuevo_usuario)
                        popup.destroy()
                        tk.showinfo("Aviso","Se ha agregdo un nuevo usuario!")
                else:
                        tk.showwarning("Alerta","Ya existe un usuario con la cedula ingresada!")


        def buscar_usuario(self, ventana):
               
                cedula = IntVar()
                popup2=Toplevel(ventana)
                popup2.title('Busqueda de Usuario')
                popup2.geometry('400x200+0+0')
        
                lblCedula = Label(popup2,text= 'Inserte el número de cedula:')
                lblCedula.grid(row=2,column=1,sticky=W)
                
                edtCedula = Entry(popup2, textvariable = cedula)
                edtCedula.grid(row=2,column=2,sticky=W)

                
                controlador_usuario = ControladorUsuario()
                btnConsultar = Button(popup2, text = 'Consultar', 
                command= lambda: self.confirmar_busqueda_usuario(popup2,
                controlador_usuario, cedula.get(), ventana))
                btnConsultar.grid(row=4, column=1)
                btnCancelar = Button(popup2, text = 'Cancelar', command=lambda: popup2.destroy())
                btnCancelar.grid(row=4, column=2)


        def confirmar_busqueda_usuario(self, popup, controlador, cedula, ventana):
                
                usuario_buscado = controlador.buscar_usuario(cedula)

                if usuario_buscado is None:
                        tk.showwarning("Alerta","No existe ningún usuario con la cedula ingresada!")
                else:
                        popup3=Toplevel(ventana)
                        popup3.title('Resultado de busqueda')
                        popup3.geometry('640x480+0+0')
                        lblDatosCliente = Label(popup3,text= 'Datos del usuario encontrado')
                        lblDatosCliente.grid(row=0,column=2)
                        lblCliente = Label(popup3,text= usuario_buscado)
                        lblCliente.grid(row=1,column=2)

        def agregar_empleado(self, ventana):
                cedula = IntVar()
                nombre = StringVar()
                apellido = StringVar()
                direccion = StringVar()
                nrotelefono = StringVar()
                descripcion = StringVar()
                popup4 = Toplevel(ventana)
                popup4.title('Datos de Empleado ')
                popup4.geometry('400x200+0+0')

                lblcedula = Label(popup4, text='Cedula:')
                lblcedula.grid(row=2, column=1, sticky=W)

                edtcedula = Entry(popup4, textvariable=cedula)
                edtcedula.grid(row=2, column=2, sticky=W)

                lblnombre = Label(popup4, text='Nombre ')
                lblnombre.grid(row=3, column=1, sticky=W)

                edtnombre = Entry(popup4, textvariable=nombre)
                edtnombre.grid(row=3, column=2, sticky=W)

                lblapellido = Label(popup4, text='Apellido:')
                lblapellido.grid(row=4, column=1, sticky=W)

                edtapellido = Entry(popup4, textvariable=apellido)
                edtapellido.grid(row=4, column=2, sticky=W)

                lbldireccion = Label(popup4, text='Direccion:')
                lbldireccion.grid(row=5, column=1, sticky=W)

                edtdireccion = Entry(popup4, textvariable=direccion)
                edtdireccion.grid(row=5, column=2, sticky=W)

                lblnrotelefono = Label(popup4, text='Nro Telefono:')
                lblnrotelefono.grid(row=6, column=1, sticky=W)

                edtnrotelefono = Entry(popup4, textvariable=nrotelefono)
                edtnrotelefono.grid(row=6, column=2, sticky=W)

                lbldescripcion = Label(popup4, text='Correo:')
                lbldescripcion.grid(row=7, column=1, sticky=W)

                edtdescripcion = Entry(popup4, textvariable=descripcion)
                edtdescripcion.grid(row=7, column=2, sticky=W)

                btnGuardar = Button(popup4, text='Guardar', command=lambda: self.confirmar_agregar_empleado(popup4, nombre.get(), apellido.get(), cedula.get(), direccion.get(), nrotelefono.get(), descripcion.get()))
                btnGuardar.grid(row=11, column=1)
                btnCancelar = Button(popup4, text='Cancelar', command=lambda: popup4.destroy())
                btnCancelar.grid(row=11, column=2)

        def confirmar_agregar_empleado(self, popup, nombre, apellido, cedula, direccion, nrotelefono, descripcion):

                empleadoControlador = ControladorEmpleado()
                empleado_buscado = empleadoControlador.buscar_empleado(cedula)

                if empleado_buscado is None:
                        contactos = [str(nrotelefono), str(descripcion)]
                        nuevo_empleado = Persona(nombre=nombre, apellido=apellido, cedula=cedula, direccion=direccion,
                                                 contactos=contactos)
                        empleado_controlador = ControladorEmpleado()
                        empleado_controlador.crear(nuevo_empleado)
                        popup.destroy()
                        tk.showinfo("Mensaje", "Se ha agregado un nuevo empleado!")
                else:
                        tk.showwarning("Alerta", "Ya existe un empleado con la cedula ingresada!")

        def buscar_empleado(self, ventana):

                cedula = IntVar()
                popup2 = Toplevel(ventana)
                popup2.title('Busqueda de Empleado')
                popup2.geometry('400x200+0+0')

                lblCedula = Label(popup2, text='Inserte el número de cedula:')
                lblCedula.grid(row=2, column=1, sticky=W)

                edtCedula = Entry(popup2, textvariable=cedula)
                edtCedula.grid(row=2, column=2, sticky=W)

                controlador_empleado = ControladorEmpleado()
                btnConsultar = Button(popup2, text='Consultar', command=lambda: self.confirmar_busqueda_empleado(popup2, controlador_empleado, cedula.get(), ventana))
                btnConsultar.grid(row=4, column=1)
                btnCancelar = Button(popup2, text='Cancelar', command=lambda: popup2.destroy())
                btnCancelar.grid(row=4, column=2)

        def confirmar_busqueda_empleado(self, popup, controlador, cedula, ventana):

                empleado_buscado = controlador.buscar_empleado(cedula)

                if empleado_buscado is None:
                        tk.showwarning("Alerta", "No existe ningún empleado con la cedula ingresada!")
                else:
                        popup3 = Toplevel(ventana)
                        popup3.title('Resultado de busqueda')
                        popup3.geometry('640x480+0+0')
                        lblDatosCliente = Label(popup3, text='Datos del empleado encontrado')
                        lblDatosCliente.grid(row=0, column=2)
                        lblCliente = Label(popup3, text=empleado_buscado)
                        lblCliente.grid(row=1, column=2)

        def agregar_solicitud_conexion(self, ventana):
                cedula = IntVar()
                descripcion_solicitud = StringVar()
                fecha = StringVar()
                popup4 = Toplevel(ventana)
                popup4.title('Formulario de Solicitud')
                popup4.geometry('400x200+0+0')

                lblcedula = Label(popup4, text='Cedula:')
                lblcedula.grid(row=2, column=1, sticky=W)

                edtcedula = Entry(popup4, textvariable=cedula)
                edtcedula.grid(row=2, column=2, sticky=W)

                lblnombre = Label(popup4, text='Descripcion Solicitud')
                lblnombre.grid(row=3, column=1, sticky=W)

                edtnombre = Entry(popup4, textvariable=descripcion_solicitud)
                edtnombre.grid(row=3, column=2, sticky=W)

                lblfecha = Label(popup4, text='Fecha:')
                lblfecha.grid(row=4, column=1, sticky=W)

                edtfecha = Entry(popup4, textvariable=fecha)
                edtfecha.grid(row=4, column=2, sticky=W)

                btnGuardar = Button(popup4, text = 'Guardar',command=lambda: self.confirmar_agregar_solicitud_conexion(popup4, cedula.get(), descripcion_solicitud.get(), fecha.get()) )
                btnGuardar.grid(row=11, column=1)
                btnCancelar = Button(popup4, text = 'Cancelar', command=lambda: popup4.destroy())
                btnCancelar.grid(row=11, column=2)

        def confirmar_agregar_solicitud_conexion(self, popup, cedula, descripcion_solicitud, fecha):

                usuario_controlador = ControladorUsuario()
                usuario_buscado = usuario_controlador.buscar_usuario(cedula)

                if usuario_buscado is None:
                        tk.showwarning("Alerta", "No existe un usuario con la cedula ingresada!\nPara crear una solicitud, el usuario debe estar registrado.")

                else:
                        controlador_solicitud = ControladorSolicitud()
                        nueva_solicitud = Solicitud(cedula=cedula, descripcion=descripcion_solicitud, fecha=fecha)
                        controlador_solicitud.crear(nueva_solicitud)
                        popup.destroy()
                        tk.showinfo("Mensaje","Se ha creado una nueva solicitud de conexión!")

        def buscar_solicitud(self, ventana):

                cedula = IntVar()
                popup2 = Toplevel(ventana)
                popup2.title('Busqueda de Solicitud')
                popup2.geometry('400x200+0+0')

                lblCedula = Label(popup2, text='Inserte el número de cedula:')
                lblCedula.grid(row=2, column=1, sticky=W)

                edtCedula = Entry(popup2, textvariable=cedula)
                edtCedula.grid(row=2, column=2, sticky=W)

                controlador_solicitud = ControladorSolicitud()
                btnConsultar = Button(popup2, text='Consultar', command=lambda: self.confirmar_busqueda_solicitud(popup2, controlador_solicitud, cedula.get(), ventana))
                btnConsultar.grid(row=4, column=1)
                btnCancelar = Button(popup2, text='Cancelar', command=lambda: popup2.destroy())
                btnCancelar.grid(row=4, column=2)

        def confirmar_busqueda_solicitud(self, popup, controlador, cedula, ventana):

                solicitud_buscada = controlador.buscar_solicitud(cedula)

                if solicitud_buscada is None:
                        tk.showwarning("Alerta", "No existe ninguna solicitud con la cedula ingresada!")
                else:
                        popup3 = Toplevel(ventana)
                        popup3.title('Resultado de busqueda')
                        popup3.geometry('640x480+0+0')
                        lblDatosCliente = Label(popup3, text='Datos de la Solicitud')
                        lblDatosCliente.grid(row=0, column=2)
                        lblCliente = Label(popup3, text=solicitud_buscada)
                        lblCliente.grid(row=1, column=2)

        def agregar_solicitud_desconexion(self, ventana):
                cedula = IntVar()
                descripcion_solicitud = StringVar()
                fecha = StringVar()
                popup4 = Toplevel(ventana)
                popup4.title('Formulario de Solicitud')
                popup4.geometry('400x200+0+0')

                lblcedula = Label(popup4, text='Cedula:')
                lblcedula.grid(row=2, column=1, sticky=W)

                edtcedula = Entry(popup4, textvariable=cedula)
                edtcedula.grid(row=2, column=2, sticky=W)

                lblnombre = Label(popup4, text='Razón de la desconexión')
                lblnombre.grid(row=3, column=1, sticky=W)

                edtnombre = Entry(popup4, textvariable=descripcion_solicitud)
                edtnombre.grid(row=3, column=2, sticky=W)

                lblfecha = Label(popup4, text='Fecha:')
                lblfecha.grid(row=4, column=1, sticky=W)

                edtfecha = Entry(popup4, textvariable=fecha)
                edtfecha.grid(row=4, column=2, sticky=W)

                btnGuardar = Button(popup4, text = 'Guardar',command=lambda: self.confirmar_agregar_solicitud_desconexion(popup4, cedula.get(), descripcion_solicitud.get(), fecha.get()) )
                btnGuardar.grid(row=11, column=1)
                btnCancelar = Button(popup4, text = 'Cancelar', command=lambda: popup4.destroy())
                btnCancelar.grid(row=11, column=2)

        def confirmar_agregar_solicitud_desconexion(self, popup, cedula, descripcion_solicitud, fecha):

                usuario_controlador = ControladorUsuario()
                usuario_buscado = usuario_controlador.buscar_usuario(cedula)

                if usuario_buscado is None:
                        tk.showwarning("Alerta", "No existe un usuario con la cedula ingresada!\nPara crear una solicitud, el usuario debe estar registrado.")

                else:
                        controlador_solicitud = ControladorSolicitud()
                        nueva_solicitud = Solicitud(cedula=cedula, descripcion=descripcion_solicitud, fecha=fecha)
                        controlador_solicitud.crear(nueva_solicitud)
                        popup.destroy()
                        tk.showinfo("Mensaje","Se ha creado una nueva solicitud de desconexión!")

        def agregar_solicitud_reparacion(self, ventana):
                cedula = IntVar()
                descripcion_solicitud = StringVar()
                fecha = StringVar()
                popup4 = Toplevel(ventana)
                popup4.title('Formulario de Solicitud')
                popup4.geometry('400x200+0+0')

                lblcedula = Label(popup4, text='Cedula:')
                lblcedula.grid(row=2, column=1, sticky=W)

                edtcedula = Entry(popup4, textvariable=cedula)
                edtcedula.grid(row=2, column=2, sticky=W)

                lblnombre = Label(popup4, text='Descripción de reparación')
                lblnombre.grid(row=3, column=1, sticky=W)

                edtnombre = Entry(popup4, textvariable=descripcion_solicitud)
                edtnombre.grid(row=3, column=2, sticky=W)

                lblfecha = Label(popup4, text='Fecha:')
                lblfecha.grid(row=4, column=1, sticky=W)

                edtfecha = Entry(popup4, textvariable=fecha)
                edtfecha.grid(row=4, column=2, sticky=W)

                btnGuardar = Button(popup4, text = 'Guardar',command=lambda: self.confirmar_agregar_solicitud_reparacion(popup4, cedula.get(), descripcion_solicitud.get(), fecha.get()) )
                btnGuardar.grid(row=11, column=1)
                btnCancelar = Button(popup4, text = 'Cancelar', command=lambda: popup4.destroy())
                btnCancelar.grid(row=11, column=2)

        def confirmar_agregar_solicitud_reparacion(self, popup, cedula, descripcion_solicitud, fecha):

                usuario_controlador = ControladorUsuario()
                usuario_buscado = usuario_controlador.buscar_usuario(cedula)

                if usuario_buscado is None:
                        tk.showwarning("Alerta", "No existe un usuario con la cedula ingresada!\nPara crear una solicitud, el usuario debe estar registrado.")

                else:
                        controlador_solicitud = ControladorSolicitud()
                        nueva_solicitud = Solicitud(cedula=cedula, descripcion=descripcion_solicitud, fecha=fecha)
                        controlador_solicitud.crear(nueva_solicitud)
                        popup.destroy()
                        tk.showinfo("Mensaje","Se ha creado una nueva solicitud de reparación!")

        def generar_orden(self, ventana):
                cedula = IntVar()
                cedula2 = IntVar()
                descripcion_orden = StringVar()
                fecha = StringVar()
                direccion = StringVar()
                estado_terminado = 'Sin ejecutar'
                popup4 = Toplevel(ventana)
                popup4.title("Generar una orden de trabajo")
                popup4.geometry('400x200+0+0')

                lblcedula = Label(popup4, text='Cedula del usuario:')
                lblcedula.grid(row=2, column=1, sticky=W)

                edtcedula = Entry(popup4, textvariable=cedula)
                edtcedula.grid(row=2, column=2, sticky=W)

                lblcedula2 = Label(popup4, text='Cedula del empleado a cargo:')
                lblcedula2.grid(row=3, column=1, sticky=W)

                edtcedula2 = Entry(popup4, textvariable=cedula2)
                edtcedula2.grid(row=3, column=2, sticky=W)

                lblnombre = Label(popup4, text='Descripción de la orden de trabajo')
                lblnombre.grid(row=4, column=1, sticky=W)

                edtnombre = Entry(popup4, textvariable=descripcion_orden)
                edtnombre.grid(row=4, column=2, sticky=W)

                lblfecha = Label(popup4, text='Fecha a ejecutarse la orden:')
                lblfecha.grid(row=5, column=1, sticky=W)

                edtfecha = Entry(popup4, textvariable=fecha)
                edtfecha.grid(row=5, column=2, sticky=W)

                lbldireccion = Label(popup4, text='Dirección del usuario solicitante:')
                lbldireccion.grid(row=6, column=1, sticky=W)

                edtdireccion = Entry(popup4, textvariable=direccion)
                edtdireccion.grid(row=6, column=2, sticky=W)

                btnGuardar = Button(popup4, text = 'Guardar',command=lambda: self.confirmar_agregar_orden(popup4, cedula.get(), cedula2.get(), descripcion_orden.get(), fecha.get() , direccion.get(), estado_terminado=estado_terminado))
                btnGuardar.grid(row=11, column=1)
                btnCancelar = Button(popup4, text = 'Cancelar', command=lambda: popup4.destroy())
                btnCancelar.grid(row=11, column=2)

        def confirmar_agregar_orden(self, popup, cedula, cedula2, descripcion_orden, fecha, direccion, estado_terminado):

                solicitud_controlador = ControladorSolicitud()
                solicitud_buscada = solicitud_controlador.buscar_solicitud(cedula)
                controlador_empleado = ControladorEmpleado()
                empleado_buscado = controlador_empleado.buscar_empleado(cedula2)

                if solicitud_buscada is None:
                        popup.destroy()
                        tk.showwarning("Alerta", "Para generar una orden de trabajo\ndebe existir una solicitud por parte del usuario!")

                elif empleado_buscado is None:
                        popup.destroy()
                        tk.showwarning("Alerta","Debe asignar un empleado para generar la orden!")

                else:
                        controlador_orden = ControladorOrden()
                        nueva_orden = Orden(cedula=cedula2, descripcion=descripcion_orden, fecha=fecha, direccion=direccion, estado_terminado=estado_terminado)
                        controlador_orden.crear(nueva_orden)
                        popup.destroy()
                        tk.showinfo("Mensaje","Se ha creado una nueva orden de trabajo!")

        def buscar_orden(self, ventana):

                cedula2 = IntVar()
                popup2 = Toplevel(ventana)
                popup2.title('Busqueda de Orden')
                popup2.geometry('640x480+0+0')

                lblCedula2 = Label(popup2, text='Inserte el número de cedula del empleado\nasignado a la orden:')
                lblCedula2.grid(row=2, column=1, sticky=W)

                edtCedula2 = Entry(popup2, textvariable=cedula2)
                edtCedula2.grid(row=2, column=2, sticky=W)

                controlador_orden = ControladorOrden()
                btnConsultar = Button(popup2, text='Consultar', command=lambda: self.confirmar_busqueda_orden(popup2, controlador_orden, cedula2.get(), ventana))
                btnConsultar.grid(row=4, column=1)
                btnCancelar = Button(popup2, text='Cancelar', command=lambda: popup2.destroy())
                btnCancelar.grid(row=4, column=2)

        def confirmar_busqueda_orden(self, popup, controlador, cedula2, ventana):

                orden_buscada = controlador.buscar_orden(cedula2)

                if orden_buscada is None:
                        tk.showwarning("Alerta", "No existe ninguna orden!")
                else:
                        popup3 = Toplevel(ventana)
                        popup3.title('Resultado de busqueda')
                        popup3.geometry('640x480+0+0')
                        lblDatosCliente = Label(popup3, text='Datos de la Orden')
                        lblDatosCliente.grid(row=0, column=2)
                        lblCliente = Label(popup3, text=orden_buscada)
                        lblCliente.grid(row=1, column=2)

        def modificar_orden(self, ventana):

                cedula2 = IntVar()
                popup2 = Toplevel(ventana)
                popup2.title('Busqueda de Orden')
                popup2.geometry('640x480+0+0')

                lblCedula2 = Label(popup2, text='Inserte el número de cedula del empleado\nasignado a la orden:')
                lblCedula2.grid(row=2, column=1, sticky=W)

                edtCedula2 = Entry(popup2, textvariable=cedula2)
                edtCedula2.grid(row=2, column=2, sticky=W)

                controlador_orden = ControladorOrden()
                btnConsultar = Button(popup2, text='Consultar', command=lambda: self.confirmar_modificar_orden(popup2, controlador_orden, cedula2.get(), ventana))
                btnConsultar.grid(row=4, column=1)
                btnCancelar = Button(popup2, text='Cancelar', command=lambda: popup2.destroy())
                btnCancelar.grid(row=4, column=2)

        def confirmar_modificar_orden(self, popup, controlador, cedula2, ventana):

                orden_buscada = controlador.buscar_orden(cedula2)

                if orden_buscada is None:
                        tk.showwarning("Alerta", "No existe ninguna orden!")
                else:
                        popup3 = Toplevel(ventana)
                        popup3.title('Resultado de busqueda')
                        popup3.geometry('640x480+0+0')
                        lblDatosCliente = Label(popup3, text='Datos de la Orden')
                        lblDatosCliente.grid(row=0, column=2)
                        lblCliente = Label(popup3, text=orden_buscada)
                        lblCliente.grid(row=1, column=2)
                        btnModificar = Button(popup3, text='Modificar', command=lambda: self.editar_una_orden(popup3, orden_buscada, controlador, cedula2))
                        btnModificar.grid(row=10, column=1)
                        btnCancelar = Button(popup3, text='Cancelar', command=lambda:popup3.destroy())
                        btnCancelar.grid(row=10, column=2)

        def editar_una_orden(self, popup, orden_buscada, controlador, cedula2):
                modificado = controlador.validar_actualizacion(cedula2)

                if modificado == True:
                        tk.showinfo("Mensaje", "La orden ha sido modificada!")







