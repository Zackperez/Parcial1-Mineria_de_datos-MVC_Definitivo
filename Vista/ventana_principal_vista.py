import tkinter as tk


class Ventana_Principal_Vista():
    def __init__(self):
        self.root = tk.Tk()
        self.configurar_ventana()
        self.decorar_ventana()

    def configurar_ventana(self):
        self.root.config(bg="#0D1216")
        self.root.title("Ventana principal") #Aplica un titulo a la ventana
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

    def decorar_ventana(self):
        self.decorar_ventana_principal()
        self.menu_ventana_principal()

    def menu_ventana_principal(self):
        self.menuppal = tk.Menu(self.root)
        self.opciones = tk.Menu(self.menuppal)

    def decorar_ventana_principal(self):
        #Simple label que indica la descripcion del programa
        self.lblTituloDescripcion = tk.Label(self.root, text="Ventana principal")
        self.lblTituloDescripcion.config(bg="#0D1216", fg = "#FFBD59", font=('Roboto', '25', 'bold'))
        self.lblTituloDescripcion.grid(row=1, column=0,pady=30)
        self.lblDescripcion = tk.Label(self.root, text="¡Bienvenido!, te encuentras en la pantalla principal. \nCon esta pequeña aplicación de python (y tkinter) podrás:\n 1. Insertar información a la base de datos referente al tema\n 2. Visualizar la data de 'Meta FNCER: Incorporar en la matriz energética nueva capacidad instalada a partir de Fuentes No Convencionales de Energía Renovable - FNCER'\n 3. Ver un pequeño manual de usuario")
        self.lblDescripcion.config(bg="#0D1216", fg = "white", font=('Roboto Mono Regular', '10', 'bold'),wraplength=900, justify="left")
        self.lblDescripcion.grid(row=2, column=0, pady=20, padx = 20)

