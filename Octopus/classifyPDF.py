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

lista_pdfs = os.listdir(directorios["pdfs"]) # Lista con los nombres de los archivos.

if lista_pdfs:
    print("Empezando la clasificación...")
    for pdf in lista_pdfs:
        try:
            if pdf.split(".")[-1] == "pdf": # Esto comprueba si el documento es formato pdf, esto se puede cambiar/reemplazar/eliminar si se requiere
                print(f"Detectando tipo de documento para {pdf}")

                inicio = time.time() # Inicio toma del tiempo.
                rutaPDF = directorios["pdfs"]+'\\'+pdf # Ruta del pdf.
                images = convert_from_path(rutaPDF, last_page=1) #Rescata la página 1 del pdf
                images[0].save(directorios["images"]+'\\'+'page'+str(0)+'.jpg', 'JPEG')

                texto = pytesseract.image_to_string(directorios["images"]+"\\page0.jpg")
                texto = texto.lower()

                if texto:
                    # Tiene texto
                    if "factura" in texto:
                        # Mover a la carpeta de facturas
                        shutil.move(rutaPDF, directorios["categorias"]+"\\"+"Facturas")
                    elif "cuenta de cobro" in texto:
                        # En caso de cuenta de cobro
                        shutil.move(rutaPDF, directorios["categorias"]+"\\"+"Cuentas de cobro")
                    elif "sena" in texto:
                        # En caso sea algo del sena XD
                        shutil.move(rutaPDF, directorios["categorias"]+"\\"+"SENA")
                    else:
                        # En caso que no se identifique a donde pertenece
                        shutil.move(rutaPDF, directorios["categorias"]+"\\"+"Otros")
                else:
                    # Significa que la primera página vino vacía o no se encontró texto
                    print("No se encontró texto para clasificar. (En la primera página)")

                fin = time.time()
                print(f"Tiempo de clasificación para el pdf'{pdf}': {fin-inicio}")
            else:
                print(f"El archivo {pdf} no es extensión '.pdf'")
        except:
            pass
else: 
    print("Carpeta general vacía.")