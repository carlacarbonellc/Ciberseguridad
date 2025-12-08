README – Ejercicio 5: Búsqueda y Verificación de Credenciales en Texto Plano en un Archivo PCAP de Mayor Tamaño
Descripción del ejercicio

En este ejercicio se analiza el archivo set5.pcap, un archivo de captura más grande que contiene múltiples flujos de comunicación. Dentro de este tráfico existen credenciales transmitidas en texto plano. El objetivo es identificar dichas credenciales entre una cantidad mayor de datos y comprobar cómo pueden ser detectadas incluso cuando el volumen de tráfico es elevado.

Objetivos de aprendizaje

Analizar un archivo PCAP de gran tamaño sin perder de vista los flujos relevantes.

Identificar tráfico inseguro donde se transmiten credenciales sin cifrado.

Aplicar filtros avanzados en Wireshark para localizar información sensible más rápidamente.

Verificar la validez de credenciales encontradas dentro del flujo.

Herramientas necesarias

Wireshark (versión reciente).

El archivo set5.pcap incluido en el laboratorio.

Procedimiento paso a paso
1. Abrir el archivo PCAP

Abrir Wireshark.

Seleccionar File → Open.

Cargar el archivo set5.pcap.

2. Reducir el tráfico con filtros iniciales

Debido al tamaño del archivo, es recomendable comenzar aplicando filtros que limiten la vista a protocolos donde es más común encontrar credenciales sin cifrado. Por ejemplo:

http || ftp || telnet || smtp


También se pueden usar filtros directos para buscar texto:

frame contains "user"


o

frame contains "pass"

3. Localizar conversaciones relevantes

Identificar paquetes que formen parte de una transferencia de credenciales.

Hacer clic derecho en un paquete y seleccionar Follow → TCP Stream para ver la comunicación completa.

Revisar cuidadosamente el flujo hasta encontrar nombres de usuario, contraseñas u otra información sensible.

4. Confirmar las credenciales

Una vez encontradas, se deben verificar dentro del contexto del flujo:

Confirmar que forman parte de una solicitud o autenticación legítima dentro del tráfico.

Registrar las credenciales detectadas y validar que corresponden al contenido transmitido.

5. Revisar tráfico adicional

Debido al tamaño del archivo, puede haber múltiples credenciales o conversaciones de autenticación.
Es recomendable repetir el proceso con diferentes conversaciones hasta cubrir los posibles flujos relevantes.

Resultado esperado

Al finalizar el ejercicio, se deben haber identificado credenciales transmitidas en texto plano dentro del archivo set5.pcap, demostrando que incluso en capturas de gran tamaño es posible localizar información sensible cuando se utilizan protocolos sin cifrado.