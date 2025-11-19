#CBTIS 89
#Programacion 3°B T.M
#Valenzuela Vargas Angel

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Nombre y Apellido")

# Etiqueta y cuadro de texto para el nombre
etiqueta_nombre = tk.Label(ventana, text="Escribe tu nombre:")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Etiqueta y cuadro de texto para el apellido
etiqueta_apellido = tk.Label(ventana, text="Escribe tu apellido:")
etiqueta_apellido.pack()
entrada_apellido = tk.Entry(ventana)
entrada_apellido.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Función para mostrar el nombre completo
def mostrar_nombre():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    etiqueta_resultado.config(text="Tu nombre completo es: " + nombre + " " + apellido)

# Botón para mostrar el nombre completo
boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_nombre)
boton_mostrar.pack()

# La ventana
ventana.mainloop()
