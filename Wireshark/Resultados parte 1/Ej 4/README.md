README – Ejercicio 4: Búsqueda y Verificación de Credenciales en Texto Plano con Wireshark
Descripción del ejercicio

En este ejercicio se analiza el archivo set4.pcap, el cual contiene tráfico de red donde se transmiten credenciales en texto plano. El propósito es identificar estas credenciales dentro del flujo de datos y comprobar cómo pueden ser visibles cuando no se utiliza cifrado en las comunicaciones.

Objetivos de aprendizaje

Identificar protocolos inseguros en los que las credenciales viajan sin cifrado.

Utilizar filtros y herramientas de Wireshark para localizar información sensible.

Extraer y verificar nombres de usuario y contraseñas transmitidos abiertamente.

Entender la importancia del cifrado en la seguridad de la red.

Herramientas necesarias

Wireshark (versión reciente).

El archivo set4.pcap incluido en el laboratorio.

Procedimiento paso a paso
1. Abrir el archivo PCAP

Abrir Wireshark.

Seleccionar File → Open.

Cargar el archivo set4.pcap.

2. Identificar protocolos inseguros

Los protocolos más comunes que transmiten credenciales en texto plano son:

HTTP


Es posible filtrarlos utilizando:

http

3. Buscar credenciales directamente

Una forma rápida de localizar texto plano es usando el siguiente filtro:

frame contains "user"

o

frame contains "pass"

También se puede revisar manualmente seleccionando un paquete y abriendo la sección “Line-based text data”.

4. Seguir la conversación

Seleccionar un paquete relevante del protocolo detectado.

Hacer clic derecho y elegir Follow → TCP Stream.

Revisar el flujo de datos completo para localizar nombres de usuario, contraseñas u otra información sensible transmitida sin cifrado.

5. Verificar credenciales encontradas

Una vez localizadas, se deben registrar y confirmar comparándolas con el contenido del flujo. Esto permite verificar su validez dentro de la comunicación.

Resultado esperado

Al finalizar el ejercicio se deben haber identificado credenciales transmitidas en texto plano dentro del archivo set4.pcap, demostrando los riesgos de utilizar protocolos sin cifrado en redes reales.