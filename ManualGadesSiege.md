En este manual se presentará el modo de uso de Gades Siege, cómo está estructurada la instalación, etcétera.



# Inicio #
La **instalación** de Gades Siege es muy sencilla y está íntegramente reflejada en el artículo [creado a tal efecto](InstruccionesInstalacion.md).

## Ejecución ##
En este manual vamos a considerar que estamos trabajando con una instalación correcta de Gades Siege. Para ejecutar el juego, dentro de la carpeta "trunk" del mismo lanzamos el siguiente comando:
```
./gsiege.py
```

O este otro:
```
python gsiege.py
```

## Ficheros de registro ##
En Gades Siege existen dos clases de ficheros de registro o **logging**. Por un lado, existe un fichero llamado `log_gsiege`, que encontrarás en la carpeta principal del programa (`trunk`), que contiene los mensajes que se producen durante la ejecución del programa: avisos, errores, y mensajes de depuración.

Por otro lado, por cada encuentro disputado se genera un fichero de log con la reconstrucción de la partida. Estos ficheros los encontrarás en la carpeta `data/games`, organizados por tipos de juegos.

# Opciones del menú principal #
En el menú principal de Gades Siege encontraremos una serie de opciones, que detallaremos con más atención a continuación.

## Partida rápida ##
Este modo nos permite lanzar una partida simple entre dos sistemas expertos. Al abrir este modo, el cuadro de diálogo nos permitirá elegir los equipos que se van a enfrentar, así como diversas opciones adicionales:
  * Podemos elegir el máximo número de turnos del juego con el indicador **Número de turnos**.
  * Si activamos **No guardar la partida**, no se generará ningún fichero de log con el resultado de la misma.
  * Si activamos **Solo los resultados**, nos aparecerá directamente el desenlace final de la partida, sin posibilidad de ver el progreso de la misma.
  * Si activamos **Esconder el valor de las piezas**, el valor de cada pieza aparecerá oculto hasta que sea descubierta por otra pieza.

Una vez pulsemos en el botón **Aplicar**, la partida comenzará con las opciones indicadas.

## Competiciones ##
El modo de competiciones es el modo más usado de Gades Siege. Permite lanzar competiciones variadas entre un gran número de equipos, siguiendo tres posibles formatos:
  * **Liga**: en una liga, todos los equipos juegan contra todos, generándose una clasificación por puntos que determinará los ganadores de la competición.
  * **Copa**: en este caso, los equipos apuntados a la competición son emparejados y enfrentados, de forma aleatoria. Los equipos vencidos son automáticamente eliminados de la competición, y los ganadores pasan a la siguiente ronda. Así, la progresión de partidos se hace en forma de árbol, y en cada ronda siempre hay un número de partidos potencia de dos. Gades Siege está programado de forma que se resuelvan todos las [exenciones](http://es.wikipedia.org/wiki/Exenci%C3%B3n_%28competiciones_deportivas%29) en la primera ronda.
  * **Torneo mixto**: este modo es una mezcla entre los dos anteriores. Primero, se realiza una liga entre todos los participantes. A partir de la clasificación de ésta, la mitad de los jugadores en mejores posiciones jugarán una eliminatoria.

Las opciones en esta ventana son las siguientes:
  * **Ida y vuelta**: esta opción, que solo tiene validez al jugarse una liga, fuerza a que se realicen los partidos entre cada par de equipos dos veces, permutando las posiciones de los equipos.
  * **Solo los resultados**: al igual que en el modo de _partida rápida_, solo muestra los resultados de cada partido, no el transcurso del mismo.
  * **Número de turnos**: igual que en _partida rápida_, permite elegir el número máximo de turnos.

En la pestaña de **Jugadores** podremos elegir los equipos que van a participar en la competición, teniendo la opción de agregar, directamente, todos los equipos instalados en el sistema.

## Jugar contra un sistema experto ##
Este modo es el más interactivo de Gades Siege. Nos permitirá tomar el mando de uno de los equipos del juego y enfrentarnos a un Sistema Experto controlado por la máquina.

En el apartado **Equipo humano** elegiremos nuestra formación y la posición del equipo. En la sección **Equipo de la máquina** elegiremos nuestro oponente, con la opción de elegirlo al azar. Las opciones de configuración son iguales que en los modos anteriores.

Una vez que lancemos el juego, en nuestros turnos podremos hacer click en la ficha que deseemos mover. Al hacerlo, se nos indicarán con cuadros de color cyan las posibles posiciones a las que mover nuestra ficha. Tal y como le pasara a un sistema experto que nosotros programáramos, no veremos el valor de las fichas enemigas hasta que sean descubiertas por otra ficha. El objetivo del juego es, lógicamente, encontrar y capturar al rey. Una vez que se produzca este evento, la partida terminará.

## Modo laboratorio ##

En este modo podremos poner a pelear a nuestro sistema experto de forma automatizada un gran número de veces. Una vez que elijamos el sistema experto a testear en el apartado **Sistema experto principal**, podremos elegir una serie de opciones:
  * Indicamos el **número de repeticiones** que se realizarán para cada partido.
  * Indicamos también el **número de turnos** máximo para cada encuentro.

Una vez hecho esto, podemos elegir manualmente con qué equipos enfrentar a nuestro sistema, o indicar que se **usen todos los equipos instalados**. Tras esto, simplemente tendremos que aceptar y esperar a que termine el procesamiento.

Al terminar, se nos mostrarán unas estadísticas junto a unas gráficas, con los siguientes datos:
  * Número de encuentros realizados.
  * Partidas ganadas.
  * Partidas perdidas.
  * Partidas empatadas.
  * Número de turnos en los que el sistema gana.
  * Número de turnos en los que el sistema pierde.
  * Turno en el que la pieza de más valor suele perder.

## Partidas antiguas ##
En este modo, es posible revisar partidas previamente jugadas. Al indicar esta opción, tendremos que elegir un fichero de log correcto. Tras ello, aparecerá el reproductor de partidas (el mismo que se utiliza en los otros modos), que nos permitirá reproducir el encuentro.

## Configuración ##
Las opciones de configuración que podemos modificar en esta sección son las siguientes:
  * Ruta al directorio de logs de partidas previas.
  * Ruta al directorio de sistemas expertos. Para que sea un directorio correcto, debe contener dos subdirectorios: **rules** y **formations**. [Posteriormente](CreandoNuestroEquipo.md) se explicará el sentido de estas carpetas.
  * Opción de activar o desactivar la música en el tablero.
  * Ritmo de avance de las fichas en el modo de avance automático.

## Acerca de ##
En este panel encontrará los créditos del juego, así como información adicional.

# Estructura de ficheros de Gades Siege #
Gades Siege se estructura en la siguiente jerarquía de directorios:
  * **data** : incluye todos los ficheros de recursos,
    * **fonts** : tipografías.
    * **games** : logs de juegos y competiciones anteriores.
    * **glade** : ficheros que definen las interfaces de usuario.
    * **images** : imágenes y gráficos.
    * **music** : música del juego.
    * **teams** : <font color='#ff0000'><b>importante</b></font>, aquí es donde se guardan los ficheros de los equipos. [Posteriormente](CreandoNuestroEquipo.md) explicaremos con más detalle cómo incluir tus equipos en Gades Siege. Consta de dos subdirectorios:
      * **formations** : aquí se encuentran las formaciones de los equipos, esto es, cómo van colocadas las fichas inicialmente.
      * **rules** : aquí se encuentran las reglas del sistema experto que controla tu equipo.
  * **doc** : Documentación varia, irrelevante.
  * **guadaborad** : ficheros Python con el módulo guadaboard, que se encarga de representar en pantalla las partidas.
  * **libguadalete** : ficheros Python con el módulo del motor principal. Es el que se encargar de procesar los ficheros Clips y generar los resultados de las partidas.
  * **po** : ficheros de traducción.
  * **resistencia** : ficheros Python con el módulo principal del programa, que controla el funcionamiento en general, las interfaces gráficas de usuario, opciones de configuración, etcétera.

## Ficheros de los equipos ##
Para obtener más información sobre cómo crear los ficheros de los equipos, visita la página del wiki [Creando Nuestro Equipo](CreandoNuestroEquipo.md).

## Obstáculos ##
Los obstáculos se definen en el fichero **obstaculos** dentro de la carpeta **data**. La sintaxis para definir los obstáculos es muy sencilla. Simplemente, por cada línea hay que escribir una tupla `(x,y)` con la posición del obstáculo. Por ejemplo, este sería un fichero de obstáculos válido:
```
(1,4)
(2,4)
(3,4)
(4,4)
```

Tal y como se explica en el artículo [Creando Nuestro Equipo](CreandoNuestroEquipo.md), es posible conocer desde nuestras reglas los obstáculos que hay en el tablero mediante el hecho `(obstaculo (pos-x) (pos-y))`.