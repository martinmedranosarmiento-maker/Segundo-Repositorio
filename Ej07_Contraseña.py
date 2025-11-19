#CBTIS 89
#Programacion 3°B T.M
#Valenzuela Vargas Angel

import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Función para mostrar la ventana principal
def mostrar_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")
    ventana_principal.geometry("350x200")
    ventana_principal.configure(bg="#e0f7fa")
    fuente_bienvenida = font.Font(family="Helvetica", size=14, weight="bold")
    label_bienvenida = tk.Label(
        ventana_principal,
        text="¡Bienvenido al sistema!",
        font=fuente_bienvenida,
        bg="#e0f7fa"
    )
    label_bienvenida.pack(expand=True)
    ventana_principal.mainloop()

# Función para verificar la contraseña
def verificar_password():
    password = entrada_password.get()
    if password == "papu":
        messagebox.showinfo("Acceso", "Acceso correcto")
        ventana.destroy()  # Cierra la ventana de login
        mostrar_ventana_principal()  # Abre la ventana principal
    else:
        messagebox.showerror("Acceso", "Acceso denegado")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Acceso")
ventana.geometry("350x200")
ventana.configure(bg="#f0f4f8") # color de fondo claro

# Fuente personalizada
fuente_titulo = font.Font(family="Helvetica", size=14, weight="bold")
fuente_normal = font.Font(family="Helvetica", size=10)

# Marco centrado
marco = tk.Frame(ventana, bg="#ffffff", bd=2, relief="groove")
marco.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta de título
titulo = tk.Label(marco, text="Ingrese su contraseña", font=fuente_titulo, bg="#ffffff")
titulo.pack(padx=20, pady=(15, 5))

# Campo de entrada de password
entrada_password = tk.Entry(marco, show="*", font=fuente_normal, width=25, bd=2, relief="solid")
entrada_password.pack(pady=5, padx=20)

# Botón de verificación
boton_verificar = tk.Button(
    marco, text="Verificar acceso", command=verificar_password,
    bg="#4CAF50", fg="white", font=fuente_normal, padx=10, pady=5,
    activebackground="#a04545", relief="flat"
)
boton_verificar.pack(pady=(10, 15))

# Ejecutar la app
ventana.mainloop()
