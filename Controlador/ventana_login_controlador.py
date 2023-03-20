from Modelo.ventana_login_modelo import Ventana_Login_Modelo
from Vista.ventana_login_vista import Ventana_Login_Vista
from Controlador.ventana_principal_controlador import Ventana_Principal_Controlador
from Controlador.ventana_registro_controlador import Ventana_Registro_Controlador

import tkinter as tk
from tkinter import messagebox
import pymysql


class Ventana_Login_Controlador():
    def __init__(self):
        # 1> connection database connection

        # 2> create model instance
        self.model = Ventana_Login_Modelo

        # 3> create view instance
        self.view = Ventana_Login_Vista()

        # 4> set default value
        #self.view.btnGuardar_texto_escrito.config(command = self.iniciar_sesion)
        #self.view.btnRegistrar_Usuario.config(command = self.ventana_registro)
        # 5> create event handler
        self.view.b0.config(command=self.iniciar_sesion)
        self.view.b2.config(command = self.ventana_registro)
        # 6> run Tkinter application
        self.view.root.mainloop()

    def iniciar_sesion(self):

        try:
            bd=pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db="bd_energias"
            )
        except:
            messagebox.showinfo(title="Inicio de sesión correcta", message="Comprueba que la Base de Datos esté activa")
        else:

            fcursor=bd.cursor()

            if len(self.view.txt_nombre_usuario.get()) !=0 and len(self.view.txt_password_usuario.get()) !=0:

                fcursor.execute("SELECT contraseña FROM tlogin WHERE usuario='"+ self.view.txt_nombre_usuario.get()+"'and contraseña='"+ self.view.txt_password_usuario.get()+"'")

                if fcursor.fetchall():
                    messagebox.showinfo(title="Inicio de sesión correcta", message="Usuario y contraseña correcta")
                    self.ventana_principal()
                else: 
                    messagebox.showinfo(title="Inicio de sesión incorrecta", message="Usuario y contraseña incorrecta")
                    
                bd.close()
            else:
                messagebox.showinfo(title="Error", message="Los campos no pueden estar vacio")

    def ventana_principal(self):
        Ventana_Principal_Controlador()
        self.view.root.destroy()

    def ventana_registro(self):
        self.view.root.destroy()
        Ventana_Registro_Controlador()
