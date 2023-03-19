from Modelo.ventana_registro_modelo import Ventana_Registro_Modelo
from Vista.ventana_registro_vista import Ventana_Registro_Vista
import tkinter as tk
from tkinter import messagebox
import pymysql

class Ventana_Registro_Controlador():
    def __init__(self):
        self.model = Ventana_Registro_Modelo
        self.view = Ventana_Registro_Vista()

        self.view.btnGuardar_texto_escrito.config(command = self.registrar_usuario)

    def registrar_usuario(self):
        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_energias"
        )
        fcursor=bd.cursor()
        
        sql="INSERT INTO tlogin (usuario, contraseña) VALUES('{0}', '{1}')".format(self.view.txt_nombre_usuario.get(),self.view.txt_password_usuario.get())

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitoso", title="Aviso")

        except:
            bd.rollback
            messagebox.showinfo(message="Registro anulado", title="Aviso")    

        bd.close()