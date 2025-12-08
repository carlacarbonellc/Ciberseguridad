README – Ejercicio 3: Reconstrucción de un Archivo Multimedia con Wireshark
Descripción del ejercicio

En este ejercicio se analiza el archivo set3.pcap, el cual contiene tráfico de red correspondiente a la transmisión de un archivo multimedia. Sin embargo, debido al tamaño original del video, en las capturas solo aparece una imagen extraída del mismo, ya que GitHub no permitía subir el archivo completo. El objetivo del ejercicio es identificar el flujo de datos, reconstruir el archivo transmitido y verificar que la imagen recuperada corresponda al contenido multimedia.

Objetivos de aprendizaje

Identificar el protocolo utilizado para la transferencia del contenido multimedia.

Reconstruir los datos capturados y extraer la imagen transmitida.

Utilizar herramientas de Wireshark como "Follow TCP Stream" y "Export Objects".

Verificar la integridad del archivo recuperado.

Herramientas necesarias

Wireshark (versión reciente).

El archivo set3.pcap incluido en el laboratorio.

Procedimiento paso a paso
1. Abrir el archivo PCAP

Abrir Wireshark.

Seleccionar File → Open.

Cargar el archivo set3.pcap.

2. Identificar el flujo de datos

Revisar los primeros paquetes para determinar el protocolo utilizado (generalmente HTTP o TCP).

Aplicar un filtro para aislar la transferencia, por ejemplo:

tcp

o, si corresponde:

http

3. Seguir el flujo de la transferencia

Seleccionar un paquete asociado al envío del archivo multimedia.

Hacer clic derecho y elegir Follow → TCP Stream.

Verificar si en el flujo se observa contenido binario correspondiente a una imagen.

4. Exportar o reconstruir la imagen

Si el archivo se transfiere mediante HTTP:

Ir a File → Export Objects → HTTP.

Localizar la imagen en la lista y guardarla.

Si no aparece en objetos HTTP:

Utilizar el contenido del TCP Stream.

Guardarlo manualmente utilizando "Save as Raw" si es necesario.

5. Verificar la integridad de la imagen recuperada

Abrir la imagen guardada para comprobar que se visualiza correctamente.

Confirmar que corresponde al fragmento del video mencionado en las instrucciones.

Resultado esperado

Se debe obtener la imagen transmitida dentro del archivo set3.pcap, demostrando la capacidad de reconstruir contenido multimedia parcial a partir del tráfico capturado.