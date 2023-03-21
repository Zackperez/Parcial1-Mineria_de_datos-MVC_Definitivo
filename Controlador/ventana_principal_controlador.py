from Modelo.ventana_principal_modelo import Ventana_Principal_Modelo
from Vista.ventana_principal_vista import Ventana_Principal_Vista

from Controlador.ventana_menu_insertar_controlador import Ventana_Menu_Insertar_Controlador
from Controlador.ventana_menu_visualizar_controlador import Ventana_Menu_Visualizar_Controlador

from Modelo.ventana_menu_insertar_modelo import *
import webbrowser

class Ventana_Principal_Controlador():
    def __init__(self):
        self.model = Ventana_Principal_Modelo

        # 3> create view instance
        self.view = Ventana_Principal_Vista()

        self.view.opciones.add_command(label="Insertar", command = self.ventana_menu_insertar_datos)
        self.view.opciones.add_command(label="Visualizar",  command = self.ventana_menu_visualizar_datos)
        self.view.opciones.add_command(label="Acerca de",  command = self.abrir_enlace)
        self.view.menuppal.add_cascade(label="Opciones", menu=self.view.opciones)
        self.view.root.config(menu=self.view.menuppal)

    def saludar(self):
        print("HOLA")

    def ventana_menu_insertar_datos(self):
        Ventana_Menu_Insertar_Controlador()

    def ventana_menu_visualizar_datos(self):
        Ventana_Menu_Visualizar_Controlador()

    def abrir_enlace(self):
        webbrowser.open('https://malachite-single-c94.notion.site/Manual-de-usuario-ba0fc44199b241a98d791ec6b3f262ae')