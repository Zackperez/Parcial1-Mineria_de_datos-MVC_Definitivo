import tkinter as tk
from tkinter import *

class Ventana_Insertar_Vista():

    def __init__(self):
        
        self.root = tk.Tk()
        self.formulario()
        self.configurar_ventana()

    def configurar_ventana(self):
        self.root.title("Insertar datos") #Aplica un titulo a la ventana
        self.root.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 1108
        hventana = 600
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def formulario(self):
        canvas = Canvas(
            self.root,
            bg = "#0D1216",
            height = 600,
            width = 1108,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = 'Imagenes\\Menu_Insertar\\otronombre.png')
        self.background = canvas.create_image(
            570.0, 303.0,
            image=self.background_img)

        canvas.create_text(
            796.5, 72.0,
            text = "INSERTAR DATOS A LA BASE DE DATOS",
            fill = "#ffffff",
            font = ("Inter-Bold", int(24.0)))
        
        #PROYECTO INICIO
        canvas.create_text(
            114.5, 166.0,
            text = "Nombre proyecto",
            fill = "#ffffff",
            font = ("None", int(14.0)))
        
        self.txt_proyecto_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox0.png")
        self.txt_proyecto_bg = canvas.create_image(
            293.0, 200.5,
            image = self.txt_proyecto_img)

        self.txt_proyecto = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff") 

        self.txt_proyecto.place(
            x = 56, y = 180,
            width = 474,
            height = 39)
        
        #CAPACIDAD INICIO
        canvas.create_text(
            93.5, 252.5,
            text = "Capacidad",
            fill = "#ffffff",
            font = ("None", int(14.0)))
        
        self.txt_capacidad_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox1.png")
        self.txt_capacidad_bg = canvas.create_image(
            169.5, 286.5,
            image = self.txt_capacidad_img)

        self.txt_capacidad = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")
        

        self.txt_capacidad.place(
            x = 56, y = 266,
            width = 227,
            height = 39)
        
        #FECHA INICIO
        canvas.create_text(
            871.0, 252.5,
            text = "Fecha estimada FPO",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.txt_fecha_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox2.png")
        self.txt_fecha_bg = canvas.create_image(
            915.5, 290.5,
            image = self.txt_fecha_img)

        self.txt_fecha = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")
        
        self.txt_fecha.place(
            x = 802, y = 270,
            width = 227,
            height = 39)
        
        #MUNICIPIO INICIO
        canvas.create_text(
            582.5, 249.5,
            text = "Municipio",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.txt_municipio_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox6.png")
        self.txt_municipio_bg = canvas.create_image(
            663.5, 290.5,
            image = self.txt_municipio_img)

        self.txt_municipio = Entry(
            bd = 0,
            bg = "#202125", 
            highlightthickness = 0,
            fg = "#ffffff")

        self.txt_municipio.place(
            x = 550, y = 270,
            width = 227,
            height = 39)
        
        #DEPARTAMENTO INICIO
        canvas.create_text(
            379.5, 341.5,
            text = "Departamento",
            fill = "#ffffff",
            font = ("None", int(14.0)))
        
        self.txt_departamento_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox3.png")
        self.txt_departamento_bg = canvas.create_image(
            416.5, 467.5,
            image = self.txt_departamento_img)

        self.txt_departamento = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")

        self.txt_departamento.place(
            x = 306, y = 360,
            width = 227,
            height = 39)
        
        #COD_DEPARTAMENTO INICIO
        canvas.create_text(
            354.5, 252.5,
            text = "Código Departamento",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.txt_cod_departamento_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox5.png")
        self.txt_cod_departamento_bg = canvas.create_image(
            416.5, 290.5,
            image = self.txt_cod_departamento_img)
        
        self.txt_cod_departamento = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")

        self.txt_cod_departamento.place(
            x = 303, y = 270,
            width = 227,
            height = 39)
        
        #COD_MUNICIPIO INICIO
        canvas.create_text(
            607.0, 341.5,
            text = "Codigo Municipio",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.cod_municipio_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox11.png")
        self.cod_municipio_bg = canvas.create_image(
            663.5, 380.5,
            image = self.cod_municipio_img)

        self.cod_municipio = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")

        self.cod_municipio.place(
            x = 550, y = 360,
            width = 227,
            height = 39)
        
        #TIPO INICIO
        canvas.create_text(
            816.5, 429.5,
            text = "Tipo",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.txt_tipo_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox7.png")
        self.txt_tipo_bg = canvas.create_image(
            915.5, 467.5,
            image = self.txt_tipo_img)

        self.txt_tipo = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")
        
        self.txt_tipo.place(
            x = 802, y = 447,
            width = 227,
            height = 39)

        self.img0 = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img0.png")
        self.btn_guardar = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        self.btn_guardar.place(
            x = 840, y = 537,
            width = 189,
            height = 34)

        self.img1 = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img1.png")
        self.btn_regresar = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        self.btn_regresar.place(
            x = 80, y = 51,
            width = 189,
            height = 34)
        
        #USUARIOS INICIO
        canvas.create_text(
            88.0, 346.0,
            text = "Usuarios",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.txt_usuarios_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox8.png")
        self.txt_usuarios_bg = canvas.create_image(
            172.5, 380.5,
            image = self.txt_usuarios_img)

        self.txt_usuarios = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")
        
        self.txt_usuarios.place(
            x = 59, y = 360,
            width = 227,
            height = 39)

        #ENERGIA INICIO
        canvas.create_text(
            115.5, 430.0,
            text = "Energia [kWh/da]",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.txt_energia_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox9.png")
        self.txt_energia_bg = canvas.create_image(
            169.5, 467.5,
            image = self.txt_energia_img)

        self.txt_energia = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")

        self.txt_energia.place(
            x = 56, y = 447,
            width = 227,
            height = 39)

        #INVERSION INICIO
        canvas.create_text(
            367.0, 432.5,
            text = "Inversion estimada",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.txt_inversion_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox10.png")
        self.txt_inversion_bg = canvas.create_image(
            419.5, 380.5,
            image = self.txt_inversion_img)
        
        self.txt_inversion = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")

        self.txt_inversion.place(
            x = 303, y = 447,
            width = 227,
            height = 39)

        #EMISIONES INICIO
        canvas.create_text(
            884.5, 341.5,
            text = "Emisiones CO2 [Ton/anio]",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.emisiones_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox12.png")
        self.emisiones_bg = canvas.create_image(
            915.5, 380.5,
            image = self.emisiones_img)

        self.emisiones = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")

        self.emisiones.place(
            x = 802, y = 360,
            width = 227,
            height = 39)
        
        #EMPLEOS INICIO
        canvas.create_text(
            617.0, 432.5,
            text = "Empleos estimados",
            fill = "#ffffff",
            font = ("None", int(14.0)))
        
        self.txt_empleos_estimados_img = PhotoImage(file = f"Imagenes\\Menu_Insertar\\img_textBox4.png")
        self.txt_empleos_estimados_bg = canvas.create_image(
            663.5, 467.5,
            image = self.txt_empleos_estimados_img)

        self.txt_empleos_estimados = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff")

        self.txt_empleos_estimados.place(
            x = 550, y = 447,
            width = 227,
            height = 39)