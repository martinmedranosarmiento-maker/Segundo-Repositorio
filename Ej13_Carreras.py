#CBTIS 89
#Programacion 3°B Matutino
#Valenzuela Vargas Angel

import tkinter as tk
from tkinter import ttk


ventana=tk.Tk()
ventana.title("Carrearas")
ventana.geometry("300x200")


etiqueta=tk.Label(ventana, text="Eige una opcion:")
etiqueta.pack(pady=10)


opciones=["ARH","Arquitectatura","Comercio electronico","Comercio Internacional y Aduanas"
"Construccion","Contabilidad","Mecatronca","Programacion"]
ComboColores=ttk.Combobox(ventana, values=opciones,state="readonly")
ComboColores.pack(pady=5)


def mostrar_seleccion(event):
    seleccion=ComboColores.get() 
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}")


ComboColores.bind("<<ComboboxSelected>>", mostrar_seleccion)


etiqueta_resultado=tk.Label(ventana, text="Aun no has seleccionado nada")
etiqueta_resultado.pack(pady=20)


ventana.mainloop()
