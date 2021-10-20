# Requiere instalación de tesseract OCR, descargar "el mejor modelo" para español. https://parzibyte.me/blog/2019/05/11/instalar-tesseract-ocr-windows-10/
# El tesseract OCR debe estar en el path
import pytesseract # pip install pytesseract
import os

ruta = os.path.dirname(os.path.abspath(__file__))+"\\images"
print(ruta)

lista = os.listdir(ruta)
cuentasCobro = 0
facturas = 0
otros = 0

for elemento in lista:
    if elemento.split('.')[-1] in ('png','jpg','jpeg'):
        

        texto = pytesseract.image_to_string(ruta+"\\"+elemento)
        # print("(-------------------"+elemento+"------------------------)\n"+texto+"\n(-------------------------------------------)")

        if "factura" in texto:
            # Mover a la carpeta de facturas
            facturas += 1
        elif "cuenta de cobro" in texto:
            # En caso de cuenta de cobro
            cuentasCobro += 1
        else:
            otros += 1
        

print("- Facturas: ",facturas,"\n- Cuentas de cobro: ",cuentasCobro,"\n- Otros: ",otros)
