README – Ejercicio 2: Extracción de Imágenes y Archivos con Wireshark
Descripción del ejercicio

En este ejercicio se analiza el archivo set2.pcap, el cual contiene tráfico de red donde se transmiten imágenes y otros archivos. El objetivo es aprender a localizar, reconstruir y extraer estos objetos desde la captura utilizando Wireshark.

Objetivos de aprendizaje

Identificar tráfico HTTP dentro del archivo PCAP.

Localizar archivos transferidos en una conexión (imágenes, documentos, etc.).

Utilizar Wireshark para "Follow TCP Stream" y "Export Objects".

Guardar correctamente los archivos extraídos y verificar su integridad.

Herramientas necesarias

Wireshark (cualquier versión reciente).

El archivo set2.pcap incluido en el laboratorio.

Procedimiento paso a paso
1. Abrir el archivo PCAP

Abrir Wireshark.

Seleccionar File → Open.

Cargar el archivo set2.pcap.

2. Filtrar tráfico HTTP

En la barra de filtros, escribir:

http


Esto mostrará únicamente los paquetes HTTP, donde normalmente se transmiten archivos.

3. Exportar objetos HTTP

Ir a File → Export Objects → HTTP.

Wireshark mostrará todos los archivos transferidos a través de HTTP.

Seleccionar todos (Ctrl + A).

Hacer clic en Save All.

Elegir una carpeta de destino y guardar.

4. Verificar los archivos recuperados

Abrir los archivos guardados para comprobar que:

Se descargaron correctamente.

La información está completa.

Las imágenes se visualizan sin error.

Los documentos o archivos se abren correctamente.

Resultado esperado

Al finalizar este ejercicio se deben haber recuperado todas las imágenes y archivos transmitidos dentro del archivo set2.pcap.