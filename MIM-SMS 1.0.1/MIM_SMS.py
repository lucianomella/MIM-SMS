#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk #para gtk
import MySQLdb # para o MySQL
import bluetooth #para reconocer el telefono por bluetooth
import gammu
import sys
import os

dir=os.getcwd()+"/Escritorio/mim-software/MIM-SMS 1.0.1/"
os.curdir

class AManual:
  def __init__(self):
    self.builder = gtk.Builder()
    self.builder.add_from_file(dir+'MimSms.glade')
    self.window = self.builder.get_object('manual')
    self.window.set_title("Agregar contacto manualmente") #titulo de la ventana
    self.window.set_position(gtk.WIN_POS_CENTER)#posicionamos en el centro de la pantalla la ventana
    self.telefono = self.builder.get_object('entry5')
    self.nombre = self.builder.get_object('entry6')
    self.guardar=self.builder.get_object('button15')
    self.cancelar=self.builder.get_object('button16')
    self.window.show_all()
    self.cancelar.connect("clicked",self.cerrar)
    self.guardar.connect("clicked",self.Guarda)

  def cerrar(self,widget):
    self.window.destroy()
    
  def Guarda(self,widget):
    try:#leemos el archivo y lo pasamos a la tabla de la base de datos
      self.f=open(dir+"conexion","r+t")
    except IOError:
      self.m=mensaje(u"No se encuentra el archivo de configuración de base de datos", u"Error")
    else:
        self.arch=self.f.readlines() #leemos cada linea del archivo conexion
        self.servidor=str(self.arch[0])
        self.usuario=str(self.arch[1])
        self.clave=str(self.arch[2])
        try:
          self.t="0" + str(int(self.telefono.get_text()))
        except ValueError:
          self.v=mensaje("El número teléfonico solo debe tener numero 0-9","Error:")
        else:
          self.conexion = MySQLdb.connect(self.servidor[:-1], str(self.usuario[:-1]), str(self.clave[:-1]))
          self.conexion.select_db('mimsms')
          #se establece el cursor de la conexion
          self.Cursor = self.conexion.cursor()  
          try:
            self.sql="""insert into contactos(telefono,nombre) values('%s','%s')"""%(str(self.t),str(self.nombre.get_text()))
            self.Cursor.execute(self.sql) 
          except self.Cursor.MySQLError:
            self.m= mensaje(u"El número telefónico ya esta en la lista", "Error:")
          else:
            self.window.destroy()
            

class mensaje:
  def __init__(self,mens,titulo):
    self.builder = gtk.Builder()
    self.builder.add_from_file(dir+'MimSms.glade')
    self.window = self.builder.get_object('dialog1')
    self.window.set_title(titulo) #titulo de la ventana
    self.window.set_position(gtk.WIN_POS_CENTER)#posicionamos en el centro de la pantalla la ventana
    self.texto = self.builder.get_object('label25')
    self.texto.set_text(mens)
    self.aceptar=self.builder.get_object('button12')
    self.window.show_all()
    self.aceptar.connect("clicked",self.cerrar)
  def cerrar(self,widget):
    self.window.destroy()

class AcercaDeMIMSMS:
  def __init__(self):
    self.builder = gtk.Builder()
    self.builder.add_from_file(dir+'MimSms.glade')
    self.window = self.builder.get_object('window2')
    self.boton7= self.builder.get_object('button7')
    self.window.set_title("Acerca de MIM-SMS v1.0")#TITULO DEL PROGRAMA
    self.window.set_position(gtk.WIN_POS_CENTER)#posicionamos en el centro de la pantalla la ventana
    self.window.show_all()
    self.builder.connect_signals(self)
    self.boton7.connect("clicked", self.cerrar)
    #self.boton7.connect("clicked", self.boton41)
  def cerrar(self,widget):
     self.window.hide()
     
class AcercaDeMIM:
  def __init__(self):
    self.builder = gtk.Builder()
    self.builder.add_from_file(dir+'MimSms.glade')
    self.window = self.builder.get_object('window3')
    self.boton8= self.builder.get_object('button8')
    self.window.set_title("Acerca de MIM")#TITULO DEL PROGRAMA
    self.window.set_position(gtk.WIN_POS_CENTER)#posicionamos en el centro de la pantalla la ventana
    self.window.show_all()
    self.builder.connect_signals(self)
    self.boton8.connect("clicked", self.cerrar)
    #self.boton7.connect("clicked", self.boton41)
  def cerrar(self,widget):
     self.window.hide()
     
class AgregaArchivo:
	nomb=[]
	dialogo=[]
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file(dir+'MimSms.glade')
		self.dialogo = self.builder.get_object('filechooserdialog1')
		self.dialogo.set_title("Seleccione un archivo de texto")#TITULO DEL PROGRAMA
		self.dialogo.set_position(gtk.WIN_POS_CENTER)#posicionamos en el centro de la pantalla la ventana
		self.ruta_nombre = self.builder.get_object('entry4')
		
		self.filter = gtk.FileFilter()
		self.filter.set_name("Texto")
		self.filter.add_mime_type("Text/txt")
		self.filter.add_pattern("*.txt")
		self.dialogo.add_filter(self.filter)
		
		self.filter = gtk.FileFilter()
		self.filter.set_name("Todos")
		self.filter.add_pattern("*")
		self.dialogo.add_filter(self.filter)
		
		self.dialogo.show_all()
		
		self.cancelar= self.builder.get_object('button11')
		self.cancelar.connect("clicked", self.cerrar)
		self.abrir= self.builder.get_object('button10')
		self.abrir.connect("clicked", self.ruta)
		self.dialogo.connect("file-activated",self.asig)
	
	def cerrar(self,widget):
		self.dialogo.destroy()
	
	def asig(self,widget):
		self.ruta_nombre.set_text(u"%s"%self.dialogo.get_filename())
	
	def ruta(self,widget):
		self.repite=0
		if self.ruta_nombre.get_text()!="":
			try:#leemos el archivo y lo pasamos a la tabla de la base de datos
				self.f=open(dir+"conexion","r+t")	
			except IOError:
				self.m=mensaje(u"No se encuentra el archivo de configuración de base de datos", u"Error")
			else:
				self.lista=self.f.readlines() #leemos cada linea del archivo conexion
				self.servidor=str(self.lista[0])
				self.usuario=str(self.lista[1])
				self.clave=str(self.lista[2])
				self.conexion = MySQLdb.connect(self.servidor[:-1], str(self.usuario[:-1]), str(self.clave[:-1]))
				self.conexion.select_db('mimsms')
				#se establece el cursor de la conexion
				self.Cursor = self.conexion.cursor()  
				self.sql="""delete from contactos"""
				self.Cursor.execute(self.sql)
				try:
					self.f2=open(self.ruta_nombre.get_text(),"r+t")
				except IOError:
					self.m2=mensaje(u"No se encuentra el archivo de configuración de base de datos", u"Error")
				else:
					self.contador=0
					for self.i in self.f2.readlines(): 
						self.contador=self.contador+1
						try:
							#self.Cursor = self.conexion.cursor()  
							if self.contador%2!=0:
								#print "es inpar"  #borrar
								self.telefono="0"+str(int(self.i[:-1]))
								self.sql2="""insert into contactos(telefono) values('%s')"""%(self.telefono)
							else:
								#print "es par"  #borrar
								self.nombre=str(self.i[:-1])
								#print self.nombre
								self.sql2="""update contactos set nombre='%s' where telefono='%s'"""%(self.nombre,self.telefono)
							self.Cursor.execute(self.sql2)
						except ValueError:
							self.m2=mensaje(u"El archivo no tiene el formato correcto, verifique", u"Error") #se activa siempre
						except self.Cursor.MySQLError:
							self.repite=self.repite+1
						#hasta aqui el error
					if (self.repite>0):
						self.men=mensaje(u"Se actualizaron corecctamente los números de la lista.\n\n Se encontraron %d números repetidos"%(self.repite),"Lista actualizada")
				self.f2.close()
			self.f.close()
			self.dialogo.hide()
		else:
			self.men=mensaje("Debe seleccionar un archivo","Error")


      
class Principal:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file(dir+'MimSms.glade')
		self.window = self.builder.get_object('window1')
		self.window.set_title("MIM-SMS v1.0.1")#TITULO DEL PROGRAMA
		self.window.set_position(gtk.WIN_POS_CENTER)#posicionamos en el centro de la pantalla la ventana
		
		self.salir= self.builder.get_object('button6')
		self.amimsms= self.builder.get_object('acercademimsms')
		self.amim= self.builder.get_object('acercademim')
		self.menusalir= self.builder.get_object('menusalir')
		self.archivo=self.builder.get_object('button2')
		self.guardar_a=self.builder.get_object('button13')
		self.Ag_agenda=self.builder.get_object('button9')
		self.vaciar=self.builder.get_object('button4')
		self.a_manual=self.builder.get_object('button3')
		self.enviar=self.builder.get_object('button1')
		self.direc=self.builder.get_object('entry1')
		self.puerto=self.builder.get_object('entry2')
		self.sms=self.builder.get_object('entry3')
		self.contactos= self.builder.get_object('treeview2')
		
		self.column = gtk.TreeViewColumn("Teléfono", gtk.CellRendererText(), text =0)   
		self.column.set_resizable(True)
		self.column.set_sort_column_id(1)
		self.contactos.append_column(self.column)
		self.column = gtk.TreeViewColumn("Contacto", gtk.CellRendererText(), text = 1)
		self.column.set_resizable(True)
		self.column.set_sort_column_id(2)
		self.contactos.append_column(self.column)
		
		self.lista = gtk.ListStore(str, str)
		self.contactos.set_model(self.lista)
		self.window.show_all()
		
		#self.builder.connect_signals(self)
		if (self.window):     #con esto cerramos la ventana
			self.window.connect("destroy", gtk.main_quit)
		self.salir.connect("clicked", self.cerrar)
		self.menusalir.connect("activate", gtk.main_quit)
		self.amimsms.connect("activate",self.acercademimsms)
		self.amim.connect("activate",self.acercademim)
		self.archivo.connect("clicked", self.BuscarArchivo)
		self.vaciar.connect("clicked", self.Vaciar)
		self.a_manual.connect("clicked", self.Manual)
		self.Ag_agenda.connect("clicked",self.Agenda)
		self.enviar.connect("clicked",self.EnviarSMS)
		self.guardar_a.connect("clicked",self.Guarda)
		self.window.connect("event",self.Actualizar)#actualiza
		
	def Guarda(self,widget):
		#aqui se coloca lo que se guardará en la tabla agenda
		try:#leemos el archivo y lo pasamos a la tabla de la base de datos
			self.f=open(dir+"conexion","r+t")
		except IOError:
			self.m=mensaje(u"No se encuentra el archivo de configuración de base de datos", u"Error")
		else:
			self.arch=self.f.readlines() #leemos cada linea del archivo conexion
			self.servidor=str(self.arch[0])
			self.usuario=str(self.arch[1])
			self.clave=str(self.arch[2])
			self.conexion = MySQLdb.connect(self.servidor[:-1], str(self.usuario[:-1]), str(self.clave[:-1]))
			self.conexion.select_db('mimsms')#se establece el cursor de la conexion
			self.Cursor = self.conexion.cursor()  
			self.sql="""select telefono, nombre from contactos order by telefono"""
			self.Cursor.execute(self.sql)
			self.resultado=self.Cursor.fetchall()
			self.fila_actual=0
			self.repite=0
			self.bien=0
			for self.elem in self.resultado:
				try:
					self.sql2="""insert into agenda(telefono,nombre) values('%s','%s')"""%(str(self.elem[0]),str(self.elem[1]))
					self.Cursor.execute(self.sql2) 
				except self.Cursor.MySQLError:
					#self.Cursor2 = self.conexion.cursor()  
					self.repite=self.repite+1
					#self.sql2="""update agenda set nombre='%s' where telefono='%s')""" %(self.elem[1],self.elem[0])
					#self.Cursor2.execute(self.sql2) 
				else:
					self.bien=self.bien+1
			self.m= mensaje(u"Este proceso finalizó correctamente:\n\n + Contactos nuevos: %d \n -Contactos repetidos: %d"%(self.bien,self.repite), "Proceso Finalizado:")
			
	def EnviarSMS(self,widget):		#aqui va el codigo de envio de mensajes
		self.sm=gammu.StateMachine()
		self.sm.ReadConfig()
		self.sm.Init()
		self.data=str(self.sms.get_text())
		try:#leemos el archivo y lo pasamos a la tabla de la base de datos
			self.f=open(dir+"conexion","r+t")
		except IOError:
			self.m=mensaje(u"No se encuentra el archivo de configuración de base de datos", u"Error")
		else:
			self.arch=self.f.readlines() #leemos cada linea del archivo conexion
			self.servidor=str(self.arch[0])
			self.usuario=str(self.arch[1])
			self.clave=str(self.arch[2])
			self.conexion = MySQLdb.connect(self.servidor[:-1], str(self.usuario[:-1]), str(self.clave[:-1]))
			self.conexion.select_db('mimsms')#se establece el cursor de la conexion
			self.Cursor = self.conexion.cursor()  
			self.sql="""select telefono from contactos order by telefono"""
			self.Cursor.execute(self.sql)
			self.resultado=self.Cursor.fetchall()
			self.fila_actual=0
			for self.contac in self.resultado: 
				self.mobile="+58"+str(int(self.contac[0]))
				self.message={'Text':'%s'%(self.data),'SMSC':{'Location': 1},'Number': self.mobile,}
				self.sm.SendSMS(self.message)
			self.m=mensaje(u"Datos enviados correctamente", u"Datos enviados")
		
	
	def Agenda(self,widget):
		try:#leemos el archivo y lo pasamos a la tabla de la base de datos
			self.f=open(dir+"conexion","r+t")
		except IOError:
			self.m=mensaje(u"No se encuentra el archivo de configuración de base de datos", u"Error")
		else:
			self.arch=self.f.readlines() #leemos cada linea del archivo conexion
			self.servidor=str(self.arch[0])
			self.usuario=str(self.arch[1])
			self.clave=str(self.arch[2])
			self.conexion = MySQLdb.connect(self.servidor[:-1], str(self.usuario[:-1]), str(self.clave[:-1]))
			self.conexion.select_db('mimsms')
			#se establece el cursor de la conexion
			self.Cursor = self.conexion.cursor()  
			self.sql="""delete from contactos"""
			self.Cursor.execute(self.sql)
			self.sql="""select telefono,nombre from agenda"""
			self.Cursor.execute(self.sql)
			self.resultado=self.Cursor.fetchall()
			self.fila_actual=0
			for self.elem in self.resultado: # Agregando filas hijas
				self.sql2="""insert into contactos(telefono, nombre) values('%s','%s')"""%(str(self.elem[0]),str(self.elem[1]))
				self.Cursor.execute(self.sql2)
				self.f.close()
	
	def cerrar(self,widget):
		self.lista.clear()
		try:#leemos el archivo y lo pasamos a la tabla de la base de datos
			self.f=open(dir+"conexion","r+t")      
		except IOError:
			self.m=mensaje(u"No se encuentra el archivo de configuración de base de datos", u"Error")
		else:
			self.arch=self.f.readlines() #leemos cada linea del archivo conexion
			self.servidor=str(self.arch[0])
			self.usuario=str(self.arch[1])
			self.clave=str(self.arch[2])
			self.conexion = MySQLdb.connect(self.servidor[:-1], str(self.usuario[:-1]), str(self.clave[:-1]))
			self.conexion.select_db('mimsms')
			#se establece el cursor de la conexion
			self.Cursor = self.conexion.cursor()  
			self.sql="""delete from contactos"""
			self.Cursor.execute(self.sql)
		self.window.destroy()
	
	def Manual(self,widget):
		#self.lista.clear()
		self.man=AManual()
	
	def Vaciar(self,widget):
		self.lista.clear()
		try:#leemos el archivo y lo pasamos a la tabla de la base de datos
			self.f=open(dir+"conexion","r+t")
		except IOError:
			self.m=mensaje(u"No se encuentra el archivo de configuración de base de datos", u"Error")
		else:
			self.arch=self.f.readlines() #leemos cada linea del archivo conexion
			self.servidor=str(self.arch[0])
			self.usuario=str(self.arch[1])
			self.clave=str(self.arch[2])
			self.conexion = MySQLdb.connect(self.servidor[:-1], str(self.usuario[:-1]), str(self.clave[:-1]))
			self.conexion.select_db('mimsms')
			#se establece el cursor de la conexion
			self.Cursor = self.conexion.cursor() 
			self.sql="""delete from contactos"""
			self.Cursor.execute(self.sql)
			
	def BuscarArchivo(self,widget):
		self.v1=AgregaArchivo()
		self.v1.cerrar
		# print u"Entró a actualizar"
		self.lista.clear()
	
	def Actualizar(self,widget,callback_data):
		self.lista.clear()
		self.fila_Actual=0
		try:#leemos el archivo y lo pasamos a la tabla de la base de datos
			self.f=open(dir+"conexion","r+t")
		except IOError:
			self.m=mensaje(u"No se encuentra el archivo de configuración de base de datos", u"Error")
		else:
			self.arch=self.f.readlines() #leemos cada linea del archivo conexion
			self.servidor=str(self.arch[0])
			self.usuario=str(self.arch[1])
			self.clave=str(self.arch[2])
			self.conexion = MySQLdb.connect(self.servidor[:-1], str(self.usuario[:-1]), str(self.clave[:-1]))
			self.conexion.select_db('mimsms')
			#se establece el cursor de la conexion
			self.Cursor = self.conexion.cursor()  
			self.sql="""select telefono,nombre from contactos order by telefono"""
			self.Cursor.execute(self.sql)
			self.resultado=self.Cursor.fetchall()
			self.fila_actual=0
			for self.elem in self.resultado: # Agregando filas hijas
				self.lista.insert(self.fila_actual,[self.elem[0],self.elem[1]])
				self.fila_actual=self.fila_actual+1
	
	def acercademimsms(self,widget):
		self.v2=AcercaDeMIMSMS()
	
	def acercademim(self,widget):
		self.v3=AcercaDeMIM()
     

if __name__ == '__main__':
  v = Principal()
  gtk.main()
