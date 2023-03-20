import tkinter as tk
from  tkinter import ttk
from tkinter import *

class Ventana_Visualizar_Vista():

    def __init__(self):
        self.root = tk.Tk()
        self.configurar_ventana()
        self.tabla()

    def configurar_ventana(self):
        self.root.title("Visualizar datos de la BD") #Aplica un titulo a la ventana
        self.root.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 900
        hventana = 350
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def tabla(self):

        self.scrollY = Scrollbar()
        self.scrollY.pack(side=RIGHT, fill=Y)

        self.scrollX = Scrollbar(orient='horizontal')
        self.scrollX.pack(side= BOTTOM,fill=X)

        self.tree = ttk.Treeview(self.root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14"), show='headings', yscrollcommand=self.scrollY.set, xscrollcommand =self.scrollX.set)

        self.scrollY.config(command=self.tree.yview)
        self.scrollX.config(command=self.tree.xview)

        self.tree.column("#1",anchor=CENTER, width=80)

        self.tree.heading("#1", text="Id")

        self.tree.column("#2",anchor=CENTER, width=80)

        self.tree.heading("#2", text="Proyecto")

        self.tree.column("#3", anchor=CENTER, width=80)

        self.tree.heading("#3", text="Tipo")

        self.tree.column("#4",anchor=CENTER, width=80)

        self.tree.heading("#4", text="Capacidad")

        self.tree.column("#5",anchor=CENTER, width=80)

        self.tree.heading("#5", text="Departamento")

        self.tree.column("#6", anchor=CENTER, width=80)

        self.tree.heading("#6", text="Municipio")

        self.tree.column("#7", anchor=CENTER, width=80)

        self.tree.heading("#7", text="Codigo_Departamento")

        self.tree.column("#8", anchor=CENTER, width=80)

        self.tree.heading("#8", text="Codigo_Municipio")

        self.tree.column("#9", anchor=CENTER, width=80)

        self.tree.heading("#9", text="Fecha_estimada_FPO")

        self.tree.column("#10", anchor=CENTER, width=80)

        self.tree.heading("#10", text="Energia")

        self.tree.column("#11", anchor=CENTER, width=80)

        self.tree.heading("#11", text="Usuarios")

        self.tree.column("#12", anchor=CENTER, width=80)

        self.tree.heading("#12", text="Inversion_estimada")

        self.tree.column("#13", anchor=CENTER, width=80)

        self.tree.heading("#13", text="Empleos_estimados")

        self.tree.column("#14", anchor=CENTER, width=80)

        self.tree.heading("#14", text="Emisiones_CO2")

        self.tree.pack()

        self.btn_visualizar = tk.Button(text="Mostrar datos")
        self.btn_visualizar.pack(pady=5)

        self.btn_regresar = tk.Button(text="Regresar")
        self.btn_regresar.pack(pady=5)
