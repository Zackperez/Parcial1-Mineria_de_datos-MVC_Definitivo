from Vista.ventana_insertar_vista import Ventana_Insertar_Vista
from tkinter import messagebox
import pymysql

class Ventana_Menu_Insertar_Controlador():
    def __init__(self):
        self.view = Ventana_Insertar_Vista()
        self.view.btn_guardar.config(command = self.agregar_informacion)
        self.view.btn_regresar.config(command = self.regresar_ventana_principal)

    def saludar(self):
        print("hola")

    def prueba(self):
        nombre_proyecto = self.view.txt_proyecto.get()
        capacidad = self.view.txt_capacidad.get()
        cod_depa = self.view.txt_cod_departamento.get()
        municipio = self.view.txt_municipio.get()
        fecha = self.view.txt_fecha.get()
        usuarios = self.view.txt_usuarios.get()
        departamento = self.view.txt_departamento.get()
        cod_muni = self.view.cod_municipio.get()
        emisiones = self.view.emisiones.get()
        energia = self.view.txt_energia.get()
        inversion = self.view.txt_inversion.get()
        empleos = self.view.txt_empleos_estimados.get()
        tipo = self.view.txt_tipo.get()

        print(nombre_proyecto,capacidad,cod_depa,cod_muni,municipio,fecha,usuarios,departamento,emisiones,energia,inversion,empleos,tipo)

    def agregar_informacion(self):

        global nombre_proyecto

        nombre_proyecto = self.view.txt_proyecto.get()
        capacidad = self.view.txt_capacidad.get()
        cod_depa = self.view.txt_cod_departamento.get()
        municipio = self.view.txt_municipio.get()
        fecha = self.view.txt_fecha.get()
        usuarios = self.view.txt_usuarios.get()
        departamento = self.view.txt_departamento.get()
        cod_muni = self.view.cod_municipio.get()
        emisiones = self.view.emisiones.get()
        energia = self.view.txt_energia.get()
        inversion = self.view.txt_inversion.get()
        empleos = self.view.txt_empleos_estimados.get()
        tipo = self.view.txt_tipo.get()

        print(nombre_proyecto,tipo,capacidad,cod_depa,cod_muni,municipio,fecha,usuarios,departamento,emisiones,energia,inversion,empleos,)

        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_energias"
        )
        fcursor=bd.cursor()
        
        sql="INSERT INTO metafncer (Proyecto, Tipo, Capacidad, Departamento, Municipio, Codigo_Departamento, Codigo_Municipio, Fecha_Estimada_FPO, Energia, Usuarios, Inversion_Estimada, Empleos_estimados, Emisiones_CO2) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}' )".format(self.view.txt_proyecto.get(), self.view.txt_tipo.get(), self.view.txt_capacidad.get(), self.view.txt_departamento.get(), self.view.txt_municipio.get(), self.view.txt_cod_departamento.get(), self.view.cod_municipio.get(), self.view.txt_fecha.get(), self.view.txt_energia.get(), self.view.txt_usuarios.get(), self.view.txt_inversion.get(), self.view.txt_empleos_estimados.get(), self.view.emisiones.get()) 

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitoso", title="Aviso")

        except:
            bd.rollback
            messagebox.showinfo(message="Registro anulado", title="Aviso")   

    def regresar_ventana_principal(self):
        self.view.root.destroy()