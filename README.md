# Laboratorio 7 Plataformas abiertas
# Scripting y Procesos en Python
Manfred Soza Garcia - B97755

## Contenido

- [Descripción general](#Descripción-general)
- [Estructura del Proyecto](#Estructura-del-proyecto)
- [Instrucciones de Ejecución](#Instrucciones-de-ejecución)
- [Discusion de resultados](#Discusión-de-resultados)
## Descripción General

En este proyecto se ponen en práctica los conceptos y aplicaciones de scripting y procesos ya vistos anteriormente en Bash, pero implementados al uso de Python. De manera en la que se da solución a 3 ejercicios.

## Estructura del Proyecto

En cuanto a la estructura del proyecto se agregan 3 scripts, en los cuales se resuelven cada uno de los problemas

## Instrucciones de Ejecución

**Ejercicio 1:**
Para este ejercicio se puede utilizar pgrep -f <proceso> para obtener el ID del proceso y con ello proceder con Python3 Lab7.1.py ID del proceso. Con ello se obtienen todos los datos relevantes.

**Ejercicio 2:**
Para ejecutar este script en caso de querer analizar el navegador brave, su ejecucion es usando los siguientes comandos: python Lab7.2.py brave brave.

**Ejercicio 3:**
Finalmente para ejecutar el último script se usa: python Lab7.3.py <nombre_del_ejecutable>

## Discusión de resultados
**Parte 1:**
Se obtienen los valores esperados al ejecutar y analizar los procesos.

**Parte2:**
Para este caso el código empleado, utiliza la verificación de los dos argumentos, tanto el
nombre del proceso como el comando de ejecución, para seguidamente almacenar los argumentos
y entrar en un bucle while de verificación cada 30 segundos que indica si el proceso está en
ejecución y de no ser así, se encarga de iniciarlo.
Cabe destacar que en la terminal se muestra un mensaje por parte de GTK, que recomienda
no usar este método para iniciar los procesos por cuestión de compatibilidad del sistema, pero
es funcional y óptimo.

**Parte 3:**
El script realizado verifica el argumento que se da al ejecutarlo, si no se da correctamente
el argumento indica un mensaje de error, seguidamente se asigna el nombre a la variable de
ejecutable, luego se monitorea durante 60 segundos o cuando se cierre el proceso que se está
monitoreando, este valor se puede modificar para que sea mayor o menor. Luego con el comando
start time. La función is brave running() verifica si el proceso especificado (en este caso, el
proceso Brave) está en ejecución. Utiliza el comando pgrep para buscar el proceso por nombre.
Consiguientemente se hace un bucle que permite el monitoreo constante hasta cumplir el tiempo
o hasta cerrarse el proceso.
Finalmente se genera la gráfica con los datos registrados.
