import tkinter as tk
from funciones import predecir_numero


def comenzarDibujo(event):
    global ultima_x, ultima_y
    
    ultima_x, ultima_y = event.x, event.y

def dibujar(event):
    global ultima_x, ultima_y
    canvas.create_line((ultima_x, ultima_y, event.x, event.y), fill='black',width=2)
    ultima_x, ultima_y = event.x, event.y

def borrar_todo():
    canvas.delete('all')
    etiqueta_resultado.config(text= "Numero predicho: " )

def predecir():
    numero= predecir_numero(canvas)
    etiqueta_resultado.config(text=f"Número predicho: {numero}")


ventana = tk.Tk()
ventana.title("prueba")
ventana.geometry("500x300")

canvas = tk.Canvas(ventana,width=400,height=200,bg='white')
canvas.pack(padx=5,pady=10)
canvas.bind('<Button-1>',comenzarDibujo)
canvas.bind('<B1-Motion>',dibujar)

boton_borrar = tk.Button(ventana,text="Borrar todo", command=borrar_todo)
boton_borrar.pack()

boton_predecir = tk.Button(ventana,text="Predecir",command=predecir)
boton_predecir.pack()

etiqueta_resultado = tk.Label(ventana, text="Numero Predicho: ", font=("Arial", 14))
etiqueta_resultado.pack()

ventana.mainloop()