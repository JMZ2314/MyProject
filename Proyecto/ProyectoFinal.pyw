# JHONMAIKER ZERPA
# AIMARA GUERRA
# JOSE PEREDA

import sys,re
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore

class Cuenta():
	def __init__(self):
		self.nick = ""
		self.correo = ""
		self.contra = ""

class Cliente(Cuenta):
	def __init__ (self):
		self.libros = []
		self.estado = []
class Empleado(Cuenta):
	def __init__(self):
		self.cedula = ""
		self.nombre = ""
		self.apellido = ""
		self.edad = ""


class Ventana(QDialog): 
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("Libreria.ui",self)

		self.usuarios = []
		self.empleados = []
		self.Niños = []
		self.Ficcion = []      # CREACION DE LAS LISTAS
		self.Romance = []
		self.Terror = []
		self.Ciencias = []

		self.Ficcion.append("Farenheit 451")
		self.Ficcion.append("Cazadores de Sombras")

		self.Niños.append("Los Tres Mosqueteros")
		self.Niños.append("Peter Pan")

		self.Romance.append("100 Años de Soledad")
		self.Romance.append("Diario de una Pasion")
		self.Romance.append("Bajo la misma estrella")

		self.Terror.append("IT")
		self.Terror.append("Carrie")

		self.Ciencias.append("Calculo y geometria analitica")
		self.Ciencias.append("Atlas del cielo")
		self.SigInButton.clicked.connect(self.CambiarSigIn)
		self.AtrasButton.clicked.connect(self.RegresarMenu)
		self.MenuButtonUno.clicked.connect(self.RegresarMenu)
		self.MenuButtonDos.clicked.connect(self.RegresarMenu)
		self.RentarButton.clicked.connect(self.MenuCategorias)
		self.VerListaButton.clicked.connect(self.MostrarLista)
		self.MenuButtonTres.clicked.connect(self.RegresarMenu)
		self.CerrarButtonUno.clicked.connect(self.RegresarMenu)
		self.CerrarButtonDos.clicked.connect(self.RegresarMenu)
		self.CerrarButtonTres.clicked.connect(self.RegresarMenu)
		self.LogInButton.clicked.connect(self.CambiarLogIn)
		self.IngresarButton.clicked.connect(self.IniciarSesion)
		self.Nombre.textChanged.connect(self.ValidarNombreEmpleado)
		self.Apellido.textChanged.connect(self.ValidarApellidoEmpleado)
		self.LineCedula.textChanged.connect(self.ValidarCedulaEmpleado)
		self.CorreoEmpleado.textChanged.connect(self.ValidarCorreoEmpleado)           # METODOS DE LA VENTANA DE DIALOGO
		self.CorreoCliente.textChanged.connect(self.ValidarCorreoCliente)
		self.CorreoEmpleado.textChanged.connect(self.ValidarCorreoEmpleado)
		self.RegistroUsuario.clicked.connect(self.ValidarRegistroCliente)
		self.RegistroTrabajador.clicked.connect(self.ValidarRegistroEmpleado)
		self.AceptarButton.clicked.connect(self.SeleccionarTipo)
		self.AgregarButton.clicked.connect(self.RentarLibros)
		self.DeshacerButton.clicked.connect(self.DeshacerLibros)
		self.RegresarButton.clicked.connect(self.RegresarMenuUsuario)
		self.CategoriaButton.clicked.connect(self.MenuCategorias)
		self.CerrarButtonCuatro.clicked.connect(self.RegresarMenu)
		self.CerrarButtonCinco.clicked.connect(self.RegresarMenu)
		self.CerrarButtonSeis.clicked.connect(self.RegresarMenu)
		self.CerrarSesionSiete.clicked.connect(self.RegresarMenu)
		self.RegresarDosButton.clicked.connect(self.RegresarMenuUsuario)
		self.DevolverButton.clicked.connect(self.MostrarMisLibros)
		self.DevolverLibroButton.clicked.connect(self.DevolverLibros)
		self.AddButton.clicked.connect(self.Add)
		self.NuevoButton.clicked.connect(self.IrAdd)
		self.ModificarButton.clicked.connect(self.MostrarListaEmpleado)
		self.MenuEmpleado.clicked.connect(self.RegresarMenuEmpleado)
		self.EliminarButton.clicked.connect(self.EliminarLibros)
		self.CambiarLibroButton.clicked.connect(self.ModificarLibros)
		self.RegresarEmpleado.clicked.connect(self.RegresarMenuEmpleado)

	def RegresarMenu(self):
		self.AdvertenciaLabel.setText("")
		self.NombreUsuario.setText("")
		self.UsuarioEmpleado.setText("")
		self.CargarUsuario.setText("")
		self.CargarContra.setText("")
		self.MyList.clear()
		self.MyBooks.clear()
		self.stackedWidget.setCurrentIndex(0)

	def  RegresarMenuUsuario(self):
		self.AdvertenciaLabel.setText("")
		if self.Cantidad() == 15 :
			self.AdvertenciaLabel.setText("NOTA: tienes 15 libros,devuelve uno para adquirir otro")
		self.MyBooks.clear()
		self.stackedWidget.setCurrentIndex(4)
	def RegresarMenuEmpleado(self):
		self.WorkList.clear()
		self.stackedWidget.setCurrentIndex(8)

	def CambiarSigIn(self):
		self.stackedWidget.setCurrentIndex(1)
	def CambiarLogIn(self):
		self.stackedWidget.setCurrentIndex(7)

	def SeleccionarTipo(self):
		if self.TrabajadorButton.isChecked() :
			self.stackedWidget.setCurrentIndex(2)
		elif self.ClienteButton.isChecked() :
			self.stackedWidget.setCurrentIndex(3)

			# METODOS PARA LOS CLIENTES
	
	def MostrarMisLibros(self):
		self.AdvertenciaLabel.setText("")
		for i in self.usuarios:
			if i.nick == self.CargarUsuario.text() and i.contra == self.CargarContra.text():
				for i in i.libros:
					self.MyBooks.addItem(i)
				break
		self.stackedWidget.setCurrentIndex(9)

	def DevolverLibros(self):
		if self.MyBooks.currentRow() == -1 :
			QMessageBox.warning(self,"Estado","No has seleccionado ningun libro",QMessageBox.Discard)
		else:
			for i in self.usuarios:
				if i.nick == self.CargarUsuario.text() and i.contra == self.CargarContra.text():
					i.libros.remove(self.MyBooks.selectedItems()[0].text())

			self.MyBooks.takeItem(self.MyBooks.currentRow())
	
	def MostrarLista(self):
		if self.FiccionButton.isChecked():
			for i in self.Ficcion:
				self.LabelCategoria.setText("Ficcion")
				self.BookList.addItem(i)
			self.stackedWidget.setCurrentIndex(6)
		elif self.RomanceButton.isChecked():
			self.LabelCategoria.setText("Romance")
			for i in self.Romance:
				self.BookList.addItem(i)
			self.stackedWidget.setCurrentIndex(6)
		elif self.NinosButton.isChecked():
			self.LabelCategoria.setText("Niños")
			for i in self.Niños:
				self.BookList.addItem(i)
			self.stackedWidget.setCurrentIndex(6)
		elif self.CienciasButton.isChecked():
			self.LabelCategoria.setText("Ciencias")
			for i in self.Ciencias:
				self.BookList.addItem(i)
			self.stackedWidget.setCurrentIndex(6)
		elif self.TerrorButton.isChecked():
			self.LabelCategoria.setText("Terror")
			for i in self.Terror:
				self.BookList.addItem(i)
			self.stackedWidget.setCurrentIndex(6)

	def LlenarListaUsuario(self): # AGREGAR LOS LIBROS SELECCIONADOS A LA LISTA DEL USUARIO ACTUAL
		for j in self.usuarios:
				if j.nick == self.CargarUsuario.text() and j.contra == self.CargarContra.text():
					if len(j.libros) < 15:
						j.libros.append(self.BookList.selectedItems()[0].text())
					break
	

	def Cantidad(self):
		cantidad = 0
		for i in self.usuarios:
			if self.CargarContra.text() == i.contra and self.CargarUsuario.text() == i.nick:
				cantidad = len(i.libros)
				break
		return cantidad

	def MenuCategorias(self):
		self.AdvertenciaLabel.setText("")
		self.stackedWidget.setCurrentIndex(5)
		self.MyList.clear()
		self.BookList.clear()
	
	def ConfirmarButton(self):
		if len(self.MyList) == 0:
			QMessageBox.warning(self,"Estado","No has seleccionado ningun libro",QMessageBox.Discard)	
		else:
			QMessageBox.information(self,"Estado","Libros Añadidos exitosamente",QMessageBox.Discard)
			self.BookList.clear()
			self.stackedWidget.setCurrentIndex(4)
	
	def RentarLibros(self):
		seleccionado  = self.BookList.selectedItems()
		if len(seleccionado) == 0:
			QMessageBox.warning(self,"Estado","No has seleccionado ningun libro",QMessageBox.Discard)
		else:
			if self.Cantidad() == 15:
				QMessageBox.warning(self,"Estado","No ´puedes rentar mas de 15 libros",QMessageBox.Discard)
			else: 
				for i in self.usuarios:
					if i.nick == self.CargarUsuario.text() and i.contra == self.CargarContra.text() :
						if self.BookList.selectedItems()[0].text() in i.libros:
							QMessageBox.warning(self,"Estado","Ya rentaste este libro",QMessageBox.Discard)
						else:
							self.LlenarListaUsuario()
							self.MyList.addItem(self.BookList.selectedItems()[0].text())
						break

	def DeshacerLibros(self):
		if self.MyList.currentRow() == -1 :
			QMessageBox.warning(self,"Estado","No hay nada para deshacer",QMessageBox.Discard)
		for i in self.usuarios:
			if i.nick == self.CargarUsuario.text() and i.contra == self.CargarContra.text():
				i.libros.remove(self.MyList.selectedItems()[0].text())
		self.MyList.takeItem(self.MyList.currentRow())


	# METODOS PARA LOS EMPLEADOS
			
	def MostrarListaEmpleado(self):
		self.AdvertenciaLabel.setText("")
		for i in self.Terror:
			self.WorkList.addItem(i)
		for i in self.Ficcion:
			self.WorkList.addItem(i)
		for i in self.Niños:
			self.WorkList.addItem(i)
		for i in self.Romance:
			self.WorkList.addItem(i)
		for i in self.Ciencias:
			self.WorkList.addItem(i)
		self.stackedWidget.setCurrentIndex(10)

	def IrAdd(self):
		self.NuevoLibroLine.setText("")
		self.stackedWidget.setCurrentIndex(11)


	def EliminarLibros(self):
		if self.WorkList.selectedItems()[0].text() in self.Terror:
			self.Terror.remove(self.WorkList.selectedItems()[0].text())
		elif self.WorkList.selectedItems()[0].text() in self.Romance:
			self.Romance.remove(self.WorkList.selectedItems()[0].text())
		elif self.WorkList.selectedItems()[0].text() in self.Ficcion:
			self.Ficcion.remove(self.WorkList.selectedItems()[0].text())
		elif self.WorkList.selectedItems()[0].text() in self.Ciencias:
			self.Ciencias.remove(self.WorkList.selectedItems()[0].text())
		elif self.WorkList.selectedItems()[0].text() in self.Niños:
			self.Niños.remove(self.WorkList.selectedItems()[0].text())
		self.WorkList.takeItem(self.WorkList.currentRow())

	def ModificarLibros(self):
		Index = self.WorkList.currentRow()
		recogido, ok =QInputDialog.getText(self,"Nuevo Titulo","Nuevo:")
		# BORRARLO DE LAS LISTAS

		if self.WorkList.selectedItems()[0].text() in self.Terror:
			self.Terror.remove(self.WorkList.selectedItems()[0].text())
			self.Terror.append(recogido)
		elif self.WorkList.selectedItems()[0].text() in self.Romance:
			self.Romance.remove(self.WorkList.selectedItems()[0].text())
			self.Romance.append(recogido)
		elif self.WorkList.selectedItems()[0].text() in self.Ficcion:
			self.Ficcion.remove(self.WorkList.selectedItems()[0].text())
			self.Ficcion.append(recogido)
		elif self.WorkList.selectedItems()[0].text() in self.Ciencias:
			self.Ciencias.remove(self.WorkList.selectedItems()[0].text())
			self.Ciencias.append(recogido)
		elif self.WorkList.selectedItems()[0].text() in self.Niños:
			self.Niños.remove(self.WorkList.selectedItems()[0].text())
			self.Niños.append(recogido)
		# HACER EL CAMBIO
		if ok and recogido != "":
			self.WorkList.takeItem(self.WorkList.currentRow())
			self.WorkList.insertItem(Index,recogido)

	def Add(self):
		Nuevo = self.NuevoLibroLine.text()
		if len(Nuevo) == 0:
			QMessageBox.warning(self,"Estado","No se ha escrito ningun titulo",QMessageBox.Discard)

		elif (Nuevo.lower().capitalize() in self.Terror) or (Nuevo.lower().capitalize() in self.Romance) or (Nuevo.lower().capitalize() in self.Ficcion) or (Nuevo.lower().capitalize() in self.Niños) or (Nuevo.lower().capitalize() in self.Ciencias):
			QMessageBox.warning(self,"Estado","Este titulo ya esta en el sistema",QMessageBox.Discard)
		else:
			categoria = self.CategoriasComboBox.currentText()
			if categoria == "Terror":
				self.Terror.append(self.NuevoLibroLine.text())
			elif categoria == "Romance":
				self.Romance.append(self.NuevoLibroLine.text())
			elif categoria == "Ficcion":
				self.Ficcion.append(self.NuevoLibroLine.text())
			elif categoria == "Niños":
				self.Niños.append(self.NuevoLibroLine.text())
			elif categoria == "Ciencias":
				self.Ciencias.append(self.NuevoLibroLine.text())
			QMessageBox.information(self,"Estado","Libro Añadido",QMessageBox.Discard)
			self.NuevoLibroLine.setText("")
			self.stackedWidget.setCurrentIndex(8)
		

	
		# METODOS PARA VALIDAR LOS REGISTROS DE DATOS Y AMBOS TIPOS DE USUARIO  

	def ValidarNombreEmpleado(self):
		nombre = self.Nombre.text()
		validar = re.match('[a-z\sáéíóúñ]+$',nombre,re.I)
		if nombre == "":
			self.Nombre.setStyleSheet("border : 1px solid yelow;")
			return False
		elif not validar:
			self.Nombre.setStyleSheet("border: 1px solid red; ")
			return False
		else:
			self.Nombre.setStyleSheet("border : 1px solid green;")
			return True
	
	def ValidarApellidoEmpleado(self):
		apellido = self.Apellido.text()
		validar = re.match('[a-z\sáéíóúñ]+$',apellido,re.I)
		if apellido == "":
			self.Apellido.setStyleSheet("border : 1px solid yelow;")
			return False
		elif not validar:
			self.Apellido.setStyleSheet("border: 1px solid red; ")
			return False
		else:
			self.Apellido.setStyleSheet("border : 1px solid green;")
			return True

	def ValidarCorreoEmpleado(self):
		correo = self.CorreoEmpleado.text()
		validar = re.match('^[[a-zA-Z0912345678\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$',correo,re.I)
		if correo == "":
			self.CorreoEmpleado.setStyleSheet("border : 1px solid yelow;")
			return False
		elif not validar:
			self.Apellido.setStyleSheet("border: 1px solid red; ")
			return False
		else:
			self.CorreoEmpleado.setStyleSheet("border : 1px solid green;")
			return True
	
	def ValidarCorreoCliente(self):
		correo = self.CorreoCliente.text()
		validar = re.match('^[[a-zA-Z0912345678\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$',correo,re.I)
		if correo == "":
			self.CorreoCliente.setStyleSheet("border : 1px solid yelow;")
			return False
		elif not validar:
			self.CorreoCliente.setStyleSheet("border: 1px solid red; ")
			return False
		else:
			self.CorreoCliente.setStyleSheet("border : 1px solid green;")
			return True

	def ValidarCedulaEmpleado(self):
		cedula = self.LineCedula.text()
		validar = re.match('[123456789]',cedula,re.I)
		if cedula == "":
			self.LineCedula.setStyleSheet("boder: 1px solid red;")
			return False
		elif not validar:
			self.LineCedula.setStyleSheet("border: 1px solid red;")
			return False
		else:
			self.LineCedula.setStyleSheet("border: 1px solod green;")
			return True


	def ValidarRegistroEmpleado(self):
		if self.TrabajadorRepetido() :
			QMessageBox.warning(self,"Estado","Este nombre usuario ya fue registrado",QMessageBox.Discard)
		else:
			if self.ValidarCedulaEmpleado() and self.ValidarCorreoEmpleado() and self.ValidarNombreEmpleado() and self.ValidarApellidoEmpleado():
				trabajador = Empleado()
				trabajador.nombre = self.Nombre.text()
				trabajador.apellido = self.Apellido.text()
				trabajador.nick = self.UsuarioEmpleado.text()
				trabajador.contra = self.LineCon.text()
				trabajador.cedula = self.LineCedula.text()
				trabajador.correo = self.CorreoEmpleado.text()
				trabajador.edad = str(self.EdadBox.value())
				self.empleados.append(trabajador)
				QMessageBox.information(self,"Estado","Registro Exitoso",QMessageBox.Discard)
				self.Nombre.setText("")
				self.Apellido.setText("")
				self.EdadBox.setValue(15)
				self.CorreoEmpleado.setText("")
				self.LineCedula.setText("")
				self.UsuarioEmpleado.setText("")
				self.LineCon.setText("")
				self.stackedWidget.setCurrentIndex(0)
			else:
				QMessageBox.warning(self,"Estado","Registro invalido",QMessageBox.Discard)


	def TrabajadorRepetido(self): # COM´ROBAR QUE NO SE REPITA EL MISMO NOMBRE DE USUARIO PARA LOS TRABAJADORES O EMPLEADOS
		repetido = False
		usuario =self.UsuarioEmpleado.text()
		for i in self.usuarios:
			if usuario == i.nick:
				repetido = True
				break
		for j in self.empleados:
			if usuario == j.nick:
				repetido = True
				break
		return repetido

	def ClienteRepetido(self):  # COMPROBAR QUE NO SE REPITA EL MISMO NOMBRE DE USUARIO PARA LOS CLIENTES O USUARIOS COMUNES
		repetido = False
		usuario =self.NombreUsuario.text()
		for i in self.usuarios:
			if usuario == i.nick:
				repetido = True
				break
		for j in self.empleados:
			if usuario == j.nick:
				repetido = True
				break
		return repetido

	def ValidarRegistroCliente(self):
		if self.ClienteRepetido():
			QMessageBox.warning(self,"Estado ","Este nombre de usuario ya fue registrado",QMessageBox.Discard)
		else:
			if self.ValidarCorreoCliente():
				user = Cliente()
				user.correo = self.CorreoCliente.text()
				user.nick = self.NombreUsuario.text()
				user.contra = self.conUsuario.text()
				self.usuarios.append(user)
				QMessageBox.information(self,"Estado ","Registro Exitoso",QMessageBox.Discard)
				self.NombreUsuario.setText("")
				self.conUsuario.setText("")
				self.CorreoCliente.setText("")
				self.stackedWidget.setCurrentIndex(0)
			else:
				QMessageBox.warning(self,"Estado ","Registro invalido",QMessageBox.Discard)


	def ComprobarClientes(self,nombre,contraseña):
		encontrado = False
		for i in self.usuarios:
			if nombre == i.nick and contraseña == i.contra:
				encontrado =  True
				break
		return encontrado


	def ComprobarEmpleados(self,nombre,contraseña):
		encontrado = False
		for i in self.empleados:
			if nombre == i.nick and contraseña == i.contra:
				encontrado = True
				break
		return encontrado

	
	def IniciarSesion(self):
		usuario = self.CargarUsuario.text()
		contraseña =  self.CargarContra.text()
		if self.ComprobarClientes(usuario,contraseña) or self.ComprobarEmpleados(usuario,contraseña) :
			if self.ComprobarClientes(usuario,contraseña):
				self.BienvenidaUsuario.setText("Bienvenido " + self.CargarUsuario.text() )
				if self.Cantidad() == 15:
					self.AdvertenciaLabel.setText("NOTA: tienes 15 libros,devuelve uno para adquirir otro")
				self.stackedWidget.setCurrentIndex(4)
			elif self.ComprobarEmpleados(usuario,contraseña):
				self.EtiquetaEmpleado.setText("Empleado " + self.CargarUsuario.text())
				self.stackedWidget.setCurrentIndex(8)
		else:
			QMessageBox.warning(self,"Error","Nombre o Contraseña Invalidos",QMessageBox.Discard)

		


myApp =QApplication(sys.argv)
MyProgram = Ventana()
MyProgram.show()
sys.exit(myApp.exec_())
