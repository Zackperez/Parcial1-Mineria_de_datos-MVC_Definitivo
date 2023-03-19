from Vista.ventana_insertar_vista import Ventana_Insertar_Vista


class Ventana_Menu_Insertar_Controlador():
    def __init__(self):
        self.view = Ventana_Insertar_Vista()
        self.view.btn_guardar.config(command = self.insertar_datos)
        self.view.btn_regresar.config(command = self.regresar_ventana_principal)

    def insertar_datos(self):
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

        print(nombre_proyecto,capacidad,cod_depa,municipio,fecha,usuarios,departamento,cod_muni,emisiones,energia,inversion,empleos,tipo)
        
    def saludar(self):
        print("hola")

    def regresar_ventana_principal(self):
        self.view.root.destroy()