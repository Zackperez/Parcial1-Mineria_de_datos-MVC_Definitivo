from Vista.ventana_insertar_vista import Ventana_Insertar_Vista
from Modelo.ventana_menu_insertar_modelo import Ventana_Menu_Insertar_Modelo
from tkinter import messagebox
import pymysql

class Ventana_Menu_Insertar_Controlador():
    def __init__(self):
        self.view = Ventana_Insertar_Vista()
        self.modelo = Ventana_Menu_Insertar_Modelo()
        self.view.btn_guardar.config(command = self.agregar_informacion)
        self.view.btn_regresar.config(command = self.regresar_ventana_principal)


    def agregar_informacion(self):

        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_energias"
        )

        if len(self.view.txt_proyecto.get()) != 0 and len(self.view.txt_tipo.get()) != 0 and len(self.view.txt_capacidad.get()) != 0 and len(self.view.txt_departamento.get()) != 0 and len(self.view.txt_municipio.get()) != 0 and len(self.view.txt_cod_departamento.get()) != 0 and len(self.view.cod_municipio.get()) != 0 and len(self.view.txt_fecha.get()) != 0 and len(self.view.txt_energia.get()) != 0 and len(self.view.txt_usuarios.get()) != 0 and len(self.view.txt_inversion.get()) !=0 and len(self.view.txt_empleos_estimados.get()) != 0 and len(self.view.emisiones.get()) != 0:
            fcursor=bd.cursor()
            
            sql="INSERT INTO metafncer (Proyecto, Tipo, Capacidad, Departamento, Municipio, Codigo_Departamento, Codigo_Municipio, Fecha_Estimada_FPO, Energia, Usuarios, Inversion_Estimada, Empleos_estimados, Emisiones_CO2) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}' )".format(self.view.txt_proyecto.get(), self.view.txt_tipo.get(), self.view.txt_capacidad.get(), self.view.txt_departamento.get(), self.view.txt_municipio.get(), self.view.txt_cod_departamento.get(), self.view.cod_municipio.get(), self.view.txt_fecha.get(), self.view.txt_energia.get(), self.view.txt_usuarios.get(), self.view.txt_inversion.get(), self.view.txt_empleos_estimados.get(), self.view.emisiones.get()) 

            try:
                fcursor.execute(sql)
                bd.commit()
                messagebox.showinfo(message="Registro exitoso", title="Aviso")

            except:
                bd.rollback
                messagebox.showinfo(message="Registro anulado", title="Aviso")   

        else: 
            messagebox.showinfo(title="Error", message="Los campos no pueden estar vacio")


    def regresar_ventana_principal(self):
        self.view.root.destroy()
