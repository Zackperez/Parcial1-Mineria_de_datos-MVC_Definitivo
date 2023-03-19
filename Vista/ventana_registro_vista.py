import tkinter as tk


class Ventana_Registro_Vista():
    def __init__(self):
        
        self.root = tk.Tk()
        self.configurar_ventana()
        self.decorar_ventana()

    def configurar_ventana(self):
        self.root.config(bg="#0D1216")
        self.root.title("Registro de usuario") #Aplica un titulo a la ventana
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
        self.lbl_nombre_usuario=tk.Label(self.root,text = "Nombre de usuario" )
        self.lbl_nombre_usuario.config(bg="#1D1E22", fg = "white", font = ('Roboto', '15',))
        self.lbl_nombre_usuario.pack()
        
        self.txt_nombre_usuario = tk.Entry(self.root, relief="solid")
        self.txt_nombre_usuario.pack(pady=10)

        self.lblPregunta=tk.Label(self.root,text = "Contraseña" )
        self.lblPregunta.config(bg="#1D1E22", fg = "white", font = ('Roboto', '15',))
        self.lblPregunta.pack(pady=10)
        
        self.txt_password_usuario = tk.Entry(self.root, relief="solid")
        self.txt_password_usuario.pack(pady=10)

        self.btnGuardar_texto_escrito = tk.Button(self.root, text = "Registrar",width = 10, height = 1)
        self.btnGuardar_texto_escrito.pack(pady=10)
