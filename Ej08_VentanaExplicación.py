#CBTIS 89
#Programacion 3°B T.M
#Valenzuela Vargas Angel

import tkinter as tk 

ventana=tk.Tk()
ventana.title("ventana de saludo")
ventana.geometry("400x200")

etiqueta=tk.Label(ventana,text="Hola Buenos Dias",font=("Arial",16))
etiqueta.pack(pady=20)

def Saludar():
    etiqueta.config(text="¡que tal! ¿como va tu diá?")

boton=tk.Button(ventana,text="Saludar",command=Saludar)
boton.pack(pady=10) 

ventana.mainloop()
