import os
import shutil

rutaPDF = os.path.dirname(os.path.abspath(__file__))+"\\pdfs"

rutaCC = os.path.dirname(os.path.abspath(__file__))+"\\categorias\\Cuentas de cobro"
rutaFAC = os.path.dirname(os.path.abspath(__file__))+"\\categorias\\Facturas"
rutaOTROS = os.path.dirname(os.path.abspath(__file__))+"\\categorias\\Otros"
rutaSENA = os.path.dirname(os.path.abspath(__file__))+"\\categorias\\SENA"

listaCC = os.listdir(rutaCC)
listaFAC = os.listdir(rutaFAC)
listaOTROS = os.listdir(rutaOTROS)
listaSENA = os.listdir(rutaSENA)

lista = [listaCC, listaFAC, listaOTROS, listaSENA]

for listado in lista:
    if listado:
        if listado == listaCC:
            ruta = rutaCC
        elif listado == listaFAC:
            ruta = rutaFAC
        elif listado == listaSENA:
            ruta = rutaSENA
        else:
            ruta = rutaOTROS
        
        for elemento in listado:
            shutil.move(ruta+"\\"+elemento, rutaPDF)