import tkinter as tk


class Ventana_Principal_Vista():
    def __init__(self):
        self.root = tk.Tk()
        self.configurar_ventana()
        self.decorar_ventana()

    def configurar_ventana(self):
        self.root.config(bg="#0D1216")
        self.root.title("Menu principal") #Aplica un titulo a la ventana
        self.root.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 600
        hventana = 400
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def decorar_ventana(self):
        self.menu_ventana_principal()

    def menu_ventana_principal(self):
        self.menuppal = tk.Menu(self.root)
        self.opciones = tk.Menu(self.menuppal)

