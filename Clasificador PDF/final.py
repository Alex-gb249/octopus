from pdf2image import convert_from_path # pip install pdf2image
import pytesseract # pip install pytesseract
import os
import shutil # Para mover los pdf UwU
import time # Para tomar los tiempos de ejecución

ruta = os.path.dirname(os.path.abspath(__file__))+"\\pdfs" # Carpeta contenedora de los PDFs
rutaCAT =  os.path.dirname(os.path.abspath(__file__))+"\\categorias" # Carpeta contenedora de las categorias
listaPDF = os.listdir(ruta) # Lista con los PDFs
rutaIMGS = os.path.dirname(os.path.abspath(__file__))+"\\images" # Esta es la ruta de la/s imagen/es que guardaremos a continuación y usaremos después.

for elemento in listaPDF: # Para cada PDF en la lista

    print("Empezando la clasificación...")
    inicio = time.time()
    
    rutaPDF = ruta+'\\'+elemento # Ruta del PDF actual (elemento)

    images = convert_from_path(rutaPDF, last_page=1) # Convierte cada página del PDF actual en una imagen, que se guarda en la lista 'images'
    
    images[0].save(rutaIMGS+'\\'+'page'+ str(0) +'.jpg', 'JPEG') # Esto guarda la primera imagen únicamente, si se quisiera guardar todas, habría que hacer un for como en pdfImage.py

    # Si terminas guardando más de una imagen, habría que examianr cada una con un for como en pytess.py, por ahora usaremos solo una imagen.

    texto = pytesseract.image_to_string(rutaIMGS+"\\page0.jpg") # Sacando el texto de una imagen con Tesseract
    
    if "factura" in texto:
        # Mover a la carpeta de facturas
        destino = rutaCAT+"\\"+"Facturas"
    elif "cuenta de cobro" in texto:
        # En caso de cuenta de cobro
        destino = rutaCAT+"\\"+"Cuentas de cobro"
    elif "sena" in texto:
        # En caso sea algo del sena XD
        destino = rutaCAT+"\\"+"SENA"
    else:
        # En caso que no se identifique a donde pertenece
        destino = rutaCAT+"\\"+"Otros"

    shutil.move(rutaPDF, destino)

    fin = time.time()
    print(f"Tiempo de clasificación para el pdf'{elemento}': {fin-inicio}")

print("Finalizado.")