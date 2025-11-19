#CBTIS 89
#Programacion 3°B Matutino
#Valenzuela Vargas Angel

import tkinter as tk

def IVA():
    num=float(entrada1.get())
    num2=float(entrada2.get())
    res=(num*num2)*0.16
    resultado.config(text=f"IVA:  {res:.2f} ")
   

def Subtotal():
    num=float(entrada1.get())
    num2=float(entrada2.get())
    res=num*num2
    resultado.config(text=f"Subtotal :  {res:.2f} ")
   

def Total():
    num=float(entrada1.get())
    num2=float(entrada2.get())
    res=(num*num2)*0.16
    total= res+(num*num2)
    resultado.config(text=f"Total :  {total:.2f} ")
   
    
   
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventas")
ventana.geometry("350x350")

# Crear los cuadros de texto
etiqueta = tk.Label(ventana, text="cantidad de articulos", font=("Arial", 14))
etiqueta.pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)
etiqueta1 = tk.Label(ventana, text="Precio por articulo", font=("Arial", 14))
etiqueta1.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)
# Crear botones para cada operación
boton_Subtotal = tk.Button(ventana, text="Subtotal", command=Subtotal,bg="light blue", fg="white")
boton_Subtotal.pack(pady=5)

boton_IVA = tk.Button(ventana, text="IVA", command=IVA,bg="grey", fg="white")
boton_IVA.pack(pady=5)

boton_Total= tk.Button(ventana, text="Total", command=Total,bg="mediumaquamarine", fg="white")
boton_Total.pack(pady=5)



# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="El total es : ", font=("Arial", 14))
resultado.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
