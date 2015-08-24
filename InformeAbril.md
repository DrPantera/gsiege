# Actividades realizadas durante el mes de abril de 2011 #

## Apertura de tickets de trabajo ##
Entre finales de marzo y principios de abril se añadieron al gestor de tickets una gran cantidad de elementos, entre los que figuraban funcionalidades nuevas, mejoras de otras ya existentes y reparaciones de errores.

El trabajo durante este mes se ha centrado en trabajar y cerrar el mayor número de tickets posible.

## Tickets en los que se ha trabajado ##
### Ticket 1: Logs de las competiciones ###
Aunque previamente existía cierto logging de los resultados de los campeonatos, la información era escasa y poco manejable. Se ha escrito un nuevo sistema para registrar los resultados de las competiciones, en los que se incluyen las puntuaciones de cada uno de los encuentros y las tablas de puntos finales.

### Ticket 2: Rondas superadas ###
Al finalizar cada competición no se podía ver qué partidos se habían disputado, simplemente se mostraba el resultado final, así que se implementó gráficamente un árbol de clasificación que muestra, en los campeonatos, los encuentros que se han celebrado junto con los resultados del mismo. Es posible ver una captura en la dirección: http://twitpic.com/4i96be/full

### Ticket 3: Emparejamientos ###
En cada ronda no se sabía a priori qué partidos se iban a disputar. Se ha implementado un cuadro de diálogo que informa de los partidos de cada ronda al inicio de la misma.

### Tickets 4, 7 y 8 ###
Estos tres tickets guardaban una relación entre sí que hizo que se llevaran a cabo de forma simultánea:

  * Ticket 4: implementar alguna forma de abortar una competición.
  * Ticket 7: modo de avance automático o _play_.
  * Ticket 8: animaciones de transición para las fichas.

Estos tres tickets implicaban hacer modificaciones al módulo de dibujado de las partidas. Se estudió el código existente y se decidió reescribir por completo el módulo para facilitar la adición de nuevas funcionalidades y, sobre todo, mejorar la forma en que se pintaban los elementos gráficos. Así, fue posible:

  * Implementar el ticket 4, añadiendo un botón que abortaba la competición en la interfaz
  * Implementar el ticket 7, añadiendo un botón que active el avance automático. También se ha añadido, en el panel de configuración del juego, un control para la velocidad del avance automático.
  * Implementar el ticket 8, añadiendo animaciones suaves para los movimientos de las fichas, que ahora también se desvanecen cuando resultan eliminadas.

### Ticket 14: Equipos fantasma ###
En las competiciones tipo eliminatoria, en los casos en los que el número de equipos en la primera ronda no es una potencia de dos, tarde o temprano alguno de los equipos se quedará sin rival y será automáticamente ascendido a la siguiente ronda, lo cual suele ser problemático si ocurre en rondas cercanas a la final.

La solución fue modificar el algoritmo de emparejamientos de forma que, en la primera ronda, se rellene con equipos fantasma hasta tener un número potencia de dos, de forma que todos los conflictos se resuelvan en la ronda inicial y en posteriores rondas todos los equipos tengan contra quién jugar.

### Ticket 15: nombre del ejecutable ###
Progresivamente se están cambiando los nombres que hacían referencia a la nomenclatura anterior (resistencia1812) por la nueva nominación (Gades Siege - gsiege)

### Ticket 5: lectura de posiciones ###
Uno de los problemas más habituales son los errores a la hora de definir las formaciones de los equipos. Previamente se hacía editando un fichero de Clips. Esto resultaba un proceso tedioso y muy propenso a errores, por lo que se decidió modificar el proceso cambiando la forma de definir las formaciones. A partir de ahora, los jugadores podrán escribir ficheros de texto plano con sus equipos en la forma

```
1:3:3:2:2:2:2:2
4:4:5:6:5:2:2:2
```

En este caso, se representan las dos filas en las que las fichas pueden colocarse inicialmente, siendo cada número el valor de las mismas. Esto nos permite hacer un preprocesado inicial, de forma que evitemos errores bien o malintencionados en los que aparezcan fichas fuera de sitio, más fichas de la cuenta, etcétera.

### Ticket 16: información sobre cada partido ###
Previamente, al término de cada partido sólo se indicaba el ganador del mismo, utilizando el nombre codificado del equipo. Esto hacía difícil distinguir el fichero de formación y reglas que se había utilizado, así como ver cuál era el contrincante.

Se modificó el sistema de forma que al finalizar cada partido aparezca un mensaje tipo:

> RESULTADOS DEL JUEGO:

> Ganador: equipo **Fulanito** con formación **Menganito**

> Contrincante: equipo **Noséquién** con formación **Nosécuánto**

### Ticket 18: información sobre el proyecto ###
Se ha ampliado la información existente en el cuadro de diálogo _Acerca de_, en la aplicación

### Ticket 19: directorio de equipos ###
Se ha añadido una funcionalidad en el panel de configuración en la que se detecta si el directorio elegido para almacenar los ficheros de los equipos es correcto o no. Esto se hace verificando que existen los subdirectorios correspondientes a los ficheros de formación y reglas. En caso de que la elección sea incorrecta, los cambios realizados se desechan para evitar inconsistencias durante el juego.