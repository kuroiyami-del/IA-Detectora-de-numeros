import numpy as np
from PIL import ImageGrab
from tensorflow.keras.models import load_model

modelo = load_model("modelo_mnist.h5")



def obtener_imagen_canvas(canvas):

    """
    Captura el contenido del lienzo como una imagen procesable.
    """

    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    w = x + canvas.winfo_width()
    h = y + canvas.winfo_height()

    imagen = ImageGrab.grab(bbox=(x,y,w,h))
    imagen = imagen.convert("L").resize((28,28))
    imagen = 255 - imagen
    
    return imagen


def preparar_imagen(imagen):
    """
    Convierte la imagen capturada en un array NumPy normalizado.
    """

    array = np.array(imagen)
    array = array / 255.0
    array = np.expand_dims(array,axis=0)
    return array

def predecir_numero(canvas):
    """
    Captura la imagen del canvas, la procesa y predice el número.
    """

    imagen = obtener_imagen_canvas(canvas)
    array = preparar_imagen(imagen)
    prediccion = modelo.predict(array)
    numero = np.argmax(prediccion)
    return numero









