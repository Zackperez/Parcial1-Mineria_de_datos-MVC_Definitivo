import tkinter as tk
from tkinter import *

class Ventana_Registro_Vista():

    def __init__(self):
        self.root = tk.Tk()
        self.configurar_ventana()
        self.ventana_bonita()

    def configurar_ventana(self):
        self.root.title("Registro de usuario") #Aplica un titulo a la ventana
        self.root.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 900
        hventana = 270
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def ventana_bonita(self):
        self.root.config(bg="#0D1216")
        canvas = Canvas(
            self.root,
            bg = "#ffffff",
            height = 270,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"Imagenes\\Registrar\\background.png")
        self.background = canvas.create_image(
            450.0, 135.0,
            image=self.background_img)

        canvas.create_text(
            108.0, 44.0,
            text = "Registrarse",
            fill = "#ffffff",
            font = ("None", int(24.0)))

        canvas.create_text(
            84.0, 94.0,
            text = "Usuario",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.entry0_img = PhotoImage(file = f"Imagenes\\Registrar\\img_textBox0.png")
        self.entry0_bg = canvas.create_image(
            219.5, 131.0,
            image = self.entry0_img)

        self.txt_nombre_usuario = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff",
            font = ('Roboto 14'))

        self.txt_nombre_usuario.place(
            x = 44, y = 111,
            width = 351,
            height = 38)

        canvas.create_text(
            567.0, 93.5,
            text = "Contrasena",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.entry1_img = PhotoImage(file = f"Imagenes\\Registrar\\img_textBox1.png")
        self.entry1_bg = canvas.create_image(
            688.5, 130.5,
            image = self.entry1_img)

        self.txt_password_usuario = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff",
            font = ('Roboto 14'))

        self.txt_password_usuario.place(
            x = 513, y = 110,
            width = 351,
            height = 39)
        #regresar
        self.img0 = PhotoImage(file = f"Imagenes\\Registrar\\img0.png")
        self.b1 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat")

        self.b1.place(
            x = 732, y = 208,
            width = 149,
            height = 34)