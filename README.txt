Debes asegurarte que existan las siguientes carpetas, ya que al subir a github, no sube carpetas vacías, pese a que se necesitan.
    - Octopus
        - categorias
            - Epi crisis
            - Facturas
            - Facturas credito
            - Facturas debito
            - Historias clinicas
            - Ordenes de pedido
            - Ordenes de remision
            - Sin clasificar
            - Vacios
        - images
        - logs
        - pdfs

Si acabas de clonar esto de github, es probable que no tengas la carpeta "categorias", entonces creala en la raiz de octopus,
es decir, al mismo nivel del archivo classifyPDF.py, "categorias" contiene estas carpetas: "Cuentas de cobro", "Facturas", "Otros", 
"SENA".

En el archivo requirements.txt están las especificaciones de lo que se necesita.

Archivo:
    - classifyPDF.py es el script principal, el cuál actualmente trabaja con archivos locales (Requiere la correcta carpetería que se indica al principio).