from Vista.ventana_insertar_vista import Ventana_Insertar_Vista
import tkinter as tk

class Ventana_Menu_Insertar_Modelo():
    def __init__(self):
        nombre_proyecto = tk.StringVar()
        self.capacidad = tk.DoubleVar()
        self.cod_depa = tk.StringVar()
        self.municipio = tk.StringVar()
        self.fecha = tk.StringVar()
        self.usuarios = tk.StringVar()
        self.departamento = tk.StringVar()
        self.cod_muni = tk.StringVar()
        self.emisiones = tk.StringVar()
        self.energia = tk.IntVar()
        self.inversion = tk.IntVar()
        self.empleos = tk.IntVar()
        self.tipo = tk.StringVar()


    def get_nombre_proyecto(self):
        return self.nombre_proyecto

    def set_nombre_proyecto(self, nombre_proyecto):
        self.nombre_proyecto = nombre_proyecto

    def get_capacidad(self):
        return self.capacidad

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def get_cod_depa(self):
        return self.cod_depa

    def set_cod_depa(self, cod_depa):
        self.cod_depa = cod_depa

    def get_municipio(self):
        return self.municipio

    def set_municipio(self, municipio):
        self.municipio = municipio

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_usuarios(self):
        return self.usuarios

    def set_usuarios(self, usuarios):
        self.usuarios = usuarios

    def get_departamento(self):
        return self.departamento

    def set_departamento(self, departamento):
        self.departamento = departamento

    def get_cod_muni(self):
        return self.cod_muni

    def set_cod_muni(self, cod_muni):
        self.cod_muni = cod_muni

    def get_emisiones(self):
        return self.emisiones

    def set_emisiones(self, emisiones):
        self.emisiones = emisiones

    def get_energia(self):
        return self.energia

    def set_energia(self, energia):
        self.energia = energia

    def get_inversion(self):
        return self.inversion

    def set_inversion(self, inversion):
        self.inversion = inversion

    def get_empleos(self):
        return self.empleos

    def set_empleos(self, empleos):
        self.empleos = empleos

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

