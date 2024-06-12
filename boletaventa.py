from tkinter import *

def calcular_subtotal():
    cantidad = txt9.get()
    precio = txt10.get()
    
    subtotal = float(cantidad) * float(precio)
    
    txt11.delete(0, END)
    txt11.insert(0, f"{subtotal:.2f}")
    
    return subtotal

def imprimir_boleta():
    dni = txt1.get()
    nombre = txt2.get()
    apellido = txt3.get()
    direccion = txt4.get()
    telefono = txt5.get()
    codigo_producto = txt6.get()
    descripcion = txt7.get()
    unidad = txt8.get()
    cantidad = txt9.get()
    precio = txt10.get()
    
    subtotal = calcular_subtotal()
    
    tasa_impuesto = 0.18
    total = subtotal * (1 + tasa_impuesto)
    
    txt12.delete(0, END)
    txt12.insert(0, f"{total:.2f}")
    
    boleta_texto = f"""
    Boleta de Venta
    ----------------------------
    DNI: {dni}
    Nombre: {nombre}
    Apellido: {apellido}
    Dirección: {direccion}
    Teléfono: {telefono}
    ----------------------------
    Producto: {descripcion}
    Código del Producto: {codigo_producto}
    Unidad: {unidad}
    Cantidad: {cantidad}
    Precio Unitario: {precio}
    Subtotal: {subtotal:.2f}
    Impuesto (18%): {subtotal * tasa_impuesto:.2f}
    ----------------------------
    TOTAL: {total:.2f}
    """
    print(boleta_texto)

interfaz = Tk()
interfaz.title("Boleta de Venta")
interfaz.geometry("800x500")
interfaz.config(bg="white")

etiquetas = [
    ("Boleta de Venta", 250, 50, ("Arial", 16)),
    ("DNI", 30, 100, ("Verdana", 12)),
    ("Nombre", 30, 150, ("Verdana", 12)),
    ("Apellido", 360, 150, ("Verdana", 12)),
    ("Dirección", 30, 200, ("Verdana", 12)),
    ("Teléfono", 30, 250, ("Verdana", 12)),
    ("Cod_Prod", 30, 300, ("Verdana", 12)),
    ("Descripción", 140, 300, ("Verdana", 12)),
    ("Unidad", 260, 300, ("Verdana", 12)),
    ("Cantidad", 360, 300, ("Verdana", 12)),
    ("Precio", 490, 300, ("Verdana", 12)),
    ("Subtotal", 590, 300, ("Verdana", 12))
]

for texto, x, y, fuente in etiquetas:
    etiqueta = Label(interfaz, text=texto, fg="Black", bg="white", font=fuente)
    etiqueta.place(x=x, y=y)

txt1 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt2 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt3 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt4 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt5 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt6 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt7 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt8 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt9 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt10 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt11 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))
txt12 = Entry(interfaz, bg="white", justify="left", font=("Verdana", 12))

txt1.place(x=140, y=105, width=160, height=24)
txt2.place(x=140, y=155, width=200, height=24)
txt3.place(x=450, y=155, width=200, height=24)
txt4.place(x=140, y=205, width=200, height=24)
txt5.place(x=140, y=250, width=160, height=24)
txt6.place(x=30, y=330, width=90, height=30)
txt7.place(x=145, y=330, width=90, height=30)
txt8.place(x=260, y=330, width=90, height=30)
txt9.place(x=370, y=330, width=90, height=30)
txt10.place(x=480, y=330, width=90, height=30)
txt11.place(x=590, y=330, width=90, height=30)
txt12.place(x=670, y=410, width=90, height=30)

lbl_total_nombre = Label(interfaz, text="TOTAL:", fg="Black", bg="white", font=("Verdana", 12))
lbl_total_nombre.place(x=600, y=410)

btn = Button(interfaz, text="Imprimir boleta", command=imprimir_boleta)
btn.place(x=120, y=450)

interfaz.mainloop()
