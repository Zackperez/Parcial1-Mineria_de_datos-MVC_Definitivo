import tkinter as tk
from tkinter import *

class Ventana_Login_Vista():

    def __init__(self):
        
        self.root = tk.Tk()
        self.configurar_ventana()
        self.ventana_bonita()

    def configurar_ventana(self):
        self.root.title("Menu principal") #Aplica un titulo a la ventana
        self.root.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 900
        hventana = 600
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
            height = 600,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"Imagenes\\Login\\background.png")
        self.background = canvas.create_image(
            450.0, 300.0,
            image=self.background_img)

        canvas.create_text(
            221.0, 139.0,
            text = "Inicia sesión:",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        canvas.create_text(
            82.0, 227.0,
            text = "Usuario",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.entry0_img = PhotoImage(file = f"Imagenes\\Login\\img_textBox0.png")
        self.entry0_bg = canvas.create_image(
            217.5, 264.0,
            image = self.entry0_img)

        self.txt_nombre_usuario = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff",
            font = ('Roboto 14'))

        self.txt_nombre_usuario.place(
            x = 42, y = 244,
            width = 351,
            height = 38)

        canvas.create_text(
            96.0, 313.5,
            text = "Contrasena",
            fill = "#ffffff",
            font = ("None", int(14.0)))

        self.entry1_img = PhotoImage(file = f"Imagenes\\Login\\img_textBox1.png")
        self.entry1_bg = canvas.create_image(
            217.5, 350.5,
            image = self.entry1_img)

        self.txt_password_usuario = Entry(
            bd = 0,
            bg = "#202125",
            highlightthickness = 0,
            fg = "#ffffff",
            font = ('Roboto 14'))

        self.txt_password_usuario.place(
            x = 42, y = 330,
            width = 351,
            height = 39)

        canvas.create_text(
            227.5, 545.0,
            text = "Codificado por:\nJean C. Trujillo P.\nFernando Oliveros \nJuan Cervantes \nRicardo Pacheco",
            fill = "#484b54",
            font = ("None", int(12.0)))

        self.img0 = PhotoImage(file = f"Imagenes\\Login\\img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.saludar,
            relief = "flat")

        self.b0.place(
            x = 126, y = 397,
            width = 189,
            height = 34)

    def saludar(self):
        print("HOLA")