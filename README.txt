Si acabas de clonar esto de github, es probable que no tengas la carpeta "categorias", entonces creala en la raiz de octopus,
es decir, al mismo nivel del archivo classifyPDF.py, "categorias" contiene estas carpetas: "Cuentas de cobro", "Facturas", "Otros", 
"SENA".

En el archivo requirements.txt están las especificaciones de lo que se necesita.

Archivos:
    - classifyPDF.py es el script principal, el cuál actualmente trabaja con archivos locales.
    - retract.py es un script que revierte lo hecho en el classifyPDF.py, solo es usado para pruebas, al final se eliminará