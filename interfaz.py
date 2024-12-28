import tkinter as tk
from modelo_ia import predecir_numero,obtener_imagen_canvas  # Importar la función desde modelo_ia.py
from PIL import Image

ultima_x, ultima_y = None, None

def comenzarDibujo(event):
    global ultima_x, ultima_y
    ultima_x, ultima_y = event.x, event.y

def dibujar(event):
    global ultima_x, ultima_y
    canvas.create_line((ultima_x, ultima_y, event.x, event.y), fill='black', width=2)
    ultima_x, ultima_y = event.x, event.y

def borrar_todo():
    canvas.delete('all')
    etiqueta_resultado.config(text="Número predicho: ")

def predecir():
    numero = predecir_numero(canvas)
    etiqueta_resultado.config(text=f"Número predicho: {numero}")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Reconocimiento de Números")
ventana.geometry("500x400")

canvas = tk.Canvas(ventana, width=28, height=28, bg='white')
canvas.pack(padx=5, pady=10)
canvas.create_rectangle(0, 0, 400, 400, outline="black", width=5, dash=(4, 2))
canvas.bind('<Button-1>', comenzarDibujo)
canvas.bind('<B1-Motion>', dibujar)

boton_borrar = tk.Button(ventana, text="Borrar todo", command=borrar_todo)
boton_borrar.pack()

boton_predecir = tk.Button(ventana, text="Predecir", command=predecir)
boton_predecir.pack()

etiqueta_resultado = tk.Label(ventana, text="Número predicho: ", font=("Arial", 14))
etiqueta_resultado.pack()



ventana.mainloop()
