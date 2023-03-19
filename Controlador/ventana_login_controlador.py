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
        # 6> run Tkinter application
        self.view.root.mainloop()

    def iniciar_sesion(self):
   
        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_energias"
        )
        fcursor=bd.cursor()

        fcursor.execute("SELECT contraseña FROM tlogin WHERE usuario='"+ self.view.txt_nombre_usuario.get()+"'and contraseña='"+ self.view.txt_password_usuario.get()+"'")

        if fcursor.fetchall():
            messagebox.showinfo(title="Inicio de sesión correcta", message="Usuario y contraseña correcta")
            self.ventana_principal()
        else: 
            messagebox.showinfo(title="Inicio de sesión incorrecta", message="Usuario y contraseña incorrecta")
            
        bd.close()

    def ventana_principal(self):
        Ventana_Principal_Controlador()
        self.view.root.destroy()

    def ventana_registro(self):
        Ventana_Registro_Controlador()
