import tkinter as tk
from PIL import ImageGrab, Image
import numpy as np
from tensorflow.keras.models import load_model


def comenzarDibujo(event):
    global ultima_x, ultima_y
    
    ultima_x, ultima_y = event.x, event.y

def dibujar(event):
    global ultima_x, ultima_y

    canvas.create_line((ultima_x, ultima_y, event.x, event.y), fill='black',width=2)

    ultima_x, ultima_y = event.x, event.y

def borrar_todo():
    canvas.delete('all')


def obtener_imagen_canvas():
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    w = x + canvas.winfo_width()
    h = y + canvas.winfo_height()

    imagen = ImageGrab.grab(bbox=(x,y,w,h))
    imagen = imagen.convert("L").resize((28,28))
    imagen = 255 - imagen
    
    return imagen


def preparar_imagen(imagen):
    array = np.array(imagen)
    array = array / 255.0
    array = np.expand_dims(array,axis=0)
    return array

def predecir_numero():
    imagen = obtener_imagen_canvas()
    array = preparar_imagen()
    prediccion = modelo.predict(array)
    numero = np.argmax(prediccion)
    etiqueta_resultado.cofing(text=f"Número predicho: {numero}")




ventana = tk.Tk()
ventana.title("prueba")
ventana.geometry("500x300")

canvas = tk.Canvas(ventana,width=400,height=200,bg='white')
canvas.pack(padx=5,pady=10)

canvas.bind('<Button-1>',comenzarDibujo)
canvas.bind('<B1-Motion>',dibujar)

boton_borrar = tk.Button(ventana,text="Borrar todo", command=borrar_todo)
boton_borrar.pack()

ventana.mainloop()