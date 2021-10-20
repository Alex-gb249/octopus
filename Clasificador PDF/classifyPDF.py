from pdf2image import convert_from_path # pdf2image: Esta librería nos permitirá transformar el pdf en imagenes (No es lo único que hace, pero eso la usaremos)
import pytesseract # Esta librería nos permite usar Tesseract desde python, así que podremos identificar texto en una imagen.
import os
import shutil # Para mover los pdf UwU
import time # Para tomar los tiempos de ejecución

# Estos son los directorios que manejaremos, si se desean agregar categorias, deben crear una nueva key:
directorios = {
    "pdfs":os.path.dirname(os.path.abspath(__file__))+"\\pdfs",
    "categorias":os.path.dirname(os.path.abspath(__file__))+"\\categorias",
    "images":os.path.dirname(os.path.abspath(__file__))+"\\images"
}

lista_pdfs = os.listdir(directorios["pdfs"])

if lista_pdfs:
    for x in lista_pdfs:
        print(x)
else: 
    print("Fokiu")