import numpy as np
from PIL import ImageGrab, Image
from tensorflow.keras.models import load_model

# Cargar el modelo entrenado
modelo = load_model("modelo_mnist.h5")  # Asegúrate de tener el modelo guardado como modelo_mnist.h5

def obtener_imagen_canvas(canvas):
    """
    Captura el contenido del lienzo como una imagen procesable.
    """
    from PIL import ImageGrab  # Importar aquí si no está ya importado
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    w = x + canvas.winfo_width()
    h = y + canvas.winfo_height()

    imagen = ImageGrab.grab(bbox=(x, y, w, h))
    imagen = imagen.convert("L").resize((28, 28))  # Escalar a 28x28 píxeles
    imagen = np.array(imagen)  # Convertir a NumPy
    imagen = 255 - imagen  # Invertir colores (fondo negro, número blanco)
    return imagen


def preparar_imagen(imagen):
    """
    Convierte la imagen capturada en un array NumPy normalizado.
    """
    array = np.array(imagen)
    array = array / 255.0
    array = np.expand_dims(array, axis=0)
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


