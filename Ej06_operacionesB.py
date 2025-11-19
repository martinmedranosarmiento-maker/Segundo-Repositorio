#CBTIS 89
#Programacion 3°B T.M
#Valenzuela Vargas Angel

import tkinter as tk

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        suma = num1 + num2
        resultado.config(text=f"Resultado: {suma}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

def restar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resta = num1 - num2
        resultado.config(text=f"Resultado: {resta}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

def multiplicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        multi = num1 * num2
        resultado.config(text=f"Resultado: {multi}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")
def dividir():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        div = num1 / num2
        resultado.config(text=f"Resultado: {div}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Operaciones de dos números")
ventana.geometry("350x230")

# Crear los cuadros de texto
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
entrada1.pack(pady=5)
entrada2.pack(pady=5)

# Crear botones para cada operación
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(pady=5)

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack(pady=5)

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()

