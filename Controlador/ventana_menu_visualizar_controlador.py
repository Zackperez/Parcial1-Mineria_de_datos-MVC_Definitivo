from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import *
from Vista.ventana_visualizar_vista import Ventana_Visualizar_Vista
import pymysql

class Ventana_Menu_Visualizar_Controlador():
    def __init__(self):
        self.view = Ventana_Visualizar_Vista()
        self.view.btn_visualizar.config(command = self.visualizar_datos_tabla)
        self.view.btn_regresar.config(command = self.regresar_ventana_principal)

    def visualizar_datos_tabla(self):
        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_energias"
        )
        fcursor=bd.cursor()

        fcursor.execute("SELECT * FROM metafncer")

        rows = fcursor.fetchall()    

        for row in rows:

            print(row) 

            self.view.tree.insert("", tk.END, values=row)        

        fcursor.close()

    def regresar_ventana_principal(self):
        self.view.root.destroy()