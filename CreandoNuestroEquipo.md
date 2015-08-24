# Creando nuestro equipo #
Como se ha comentado previamente, en el directorio **teams** dentro de **data** encontraremos las carpetas donde guardar los ficheros de nuestro sistema experto. Éste se compone de dos partes.

## Fichero de formación ##
Los ficheros de formación indican la posición inicial de nuestro sistema experto en el tablero. En anteriores versiones se utilizaba un fichero Clips para expresar estas posiciones, pero posteriormente decidimos utilizar una representación más sencilla.

El fichero de formación debe contenerse en la carpeta **formations** del directorio **teams**, y su nombre debe seguir la estructura **equipoNombre.form**, donde _Nombre_ será el identificador de tu equipo. El contenido de un fichero de formación es muy sencillo:

```
5:6:5:4:4:3:3:2
2:2:2:2:2:2:2:1
```

Como se ve a simple vista, el fichero consta de dos líneas de números separados entre sí por dos puntos. Estas dos líneas representan las dos filas en las que las fichas podrán colocarse inicialmente en el tablero si el equipo comienza en la parte inferior (si lo hace en la superior sería su reflejo). La formación del ejemplo se representaría en el tablero como se ve en la siguiente imagen.

![http://gsiege.googlecode.com/svn/web/ejemplo_mismo_equipo.png](http://gsiege.googlecode.com/svn/web/ejemplo_mismo_equipo.png)

Como se puede observar, ambos equipos tienen la misma formación, pero ésta queda "reflejada" según el bando.


## Fichero de reglas ##
Los ficheros de reglas definen las condiciones que el sistema experto evaluará en cada momento para decidir qué acción tomar. Estos ficheros se encuentran en la carpeta **rules** del directorio **teams**, y la nomenclatura a seguir será **reglasNombre.clp**, siendo _Nombre_, de nuevo, el mismo identificador que en el fichero de formación.

Los ficheros de reglas son ficheros de Clips propiamente, por eso tienen la extensión .clp, y siguen la sintaxis de Clips. Las primeras líneas de este fichero suelen contener comentarios que expliquen cómo funciona nuestro equipo. En particular, podemos escribir un comentario, que veremos en la aplicación, si escribimos en la primera línea:

`; DOC: aquí va el comentario de nuestro fichero`

También podemos escribir comentarios aclaratorios en cualquier parte del fichero utilizando el signo de punto y coma. Seguidamente listaremos, una detrás de otra, las reglas de nuestro sistema. Todas las reglas siguen una estructura similar:
```
(defrule EQUIPO-A::nombreRegla
  (declare (salience PRIORIDAD))
  (tiempo ?t)
  ; resto de condiciones
  =>
  ; acciones
)
```

En primer lugar, la cabecera de la regla indica su **nombre** y **módulo**. Seguidamente podemos indicar la **prioridad**, que puede tomar como máximo el valor 80, que indica la mayor prioridad. La siguiente línea es el indicador del **tiempo**, que nos informará del turno.

```
(defrule EQUIPO-A::atacar1
  (declare (salience 30))
  (ficha (equipo "A") (num ?n1) (pos-x ?x1)
         (pos-y ?y1) (puntos ?p1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2)
         (pos-y ?y2) (puntos ?p2) (descubierta 1))
  (test (and (> ?p1 ?p2) (= ?y1 ?y2) (> ?x1 ?x2)))
  (tiempo ?t)
    =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)
```

Explicaremos la regla línea a línea:

`(defrule EQUIPO-A::atacar1` Cabecera de la regla de nombre `atacar1`, dentro del módulo `EQUIPO-A`.

`(declare (salience 30))` Indicamos la prioridad de la regla respecto al resto.

`(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))` Buscamos una ficha de nuestro equipo y guardamos sus datos en las variables indicadas, para poder hacer luego comprobaciones.

`(ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))` Buscamos una ficha del equipo contrario, con la condición de que esté descubierta.

`(test (and (> ?p1 ?p2) (= ?y1 ?y2) (> ?x1 ?x2)))` En este bloque de comprobación, se verifica que nuestra ficha tenga mayor valor que la ficha adversaria, que ambas se encuentren en la misma columna y que nuestra ficha esté más a la derecha que la ficha contraria.

`(tiempo ?t)` Guardamos en la variable `t` el turno actual.

Si todas estas condiciones se cumplen, se ejecuta el bloque de acciones.

`(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))` Movemos nuestra ficha en dirección a la ficha adversaria.

Existe una entrada con [ReglasDeEjemplo](ReglasDeEjemplo.md)

### Obstáculos ###
En las últimas versiones de Gades Siege es posible añadir **obstáculos** en el tablero. El motor del juego ignorará las reglas que intenten atravesar un obstáculo, pero lo ideal es que sea el propio jugador el que los tenga en cuenta.

Existirán unos hechos, con el siguiente formato
```
(obstaculo (pos-x ?x) (pos-y ?y))
```

Con estos, el jugador podrá evaluar la estrategia que más le convenga según los obstáculos que existan en la partida.

Es posible imprimir todos los obstáculos al inicio del turno con esta regla:
```
(defrule EQUIPO-A::imprimeObstaculos
  (declare (salience 70)) 
  (tiempo ?t)
  (obstaculo (pos-x ?x) (pos-y ?y))
  =>
  (printout t "OBSTACULO EN " ?x "," ?y crlf))
```
Al ser una regla que no provoca movimientos, no consume turno.

### Fichas muertas ###
A la hora de crear nuestra estrategia, es posible saber qué fichas han muerto utilizando predicados del estilo:
```
(not (ficha (puntos 6)))
```

Eso funciona en la mayoría de los casos, pero habrá veces en los que queramos mayor control. Por ejemplo, puede ser interesante saber **en qué casilla murió** nuestra fichas 5, para evitar pasar por allí, ya que probablemente haya un 6.

Para ello, hemos implementado la plantilla `fichamuerta`, con los siguientes parámetros:
```
(fichamuerta (equipo ?e) (num ?n) (pos-x ?x) (puntos ?p) (pos-y ?y) (pos-y ?y))
```

Con ello, podremos saber qué fichas han muerto y en qué casilla murieron.

Puedes utilizar la siguiente regla para imprimir en cada turno la lista de fichas que han muerto:
```
(defrule EQUIPO-A::imprimeMuertas
  (declare (salience 70)) 
  (tiempo ?t) 
  (fichamuerta (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  =>
  (printout t "Ficha muerta, equipo " ?e ", num " ?n ", puntos " ?p ", " ?x "," ?y crlf))
```
Al igual que en el caso anterior, esta regla no provoca movimientos, por lo que no consume turno.

### Movimientos anteriores ###
Gades Siege mantiene un historial con los movimientos que ha hecho cada equipo, utilizando la siguiente plantilla para guardar la información:
```
(movio (equipo ?e) (num ?n) (puntos ?p) (turno ?tr) (mov ?m) (pos-x-ini ?y) (pos-y-ini ?y))
```

Como se puede apreciar, la plantilla guarda información sobre ĺa posición inicial de la ficha y el tipo de movimiento que hizo, así como la identidad de la ficha, equipo y turno.

# Depurando nuestro equipo #
Para depurar nuestro equipo, la herramienta que más nos va a servir será el fichero de log `clipsOutputFile`. En este fichero encontrarás, en modo texto, toda la información referente al transcurso de la partida, con el estado de la misma en cada turno.

En vuestras reglas podéis imprimir mensajes y valores con la siguiente función
```
(printout t "Este es el mensaje y el valor de x es " ?x ". Fin del mensaje" crlf)
```

Tened en cuenta algo importante: habrá veces en los que la regla se ejecute, y el mensaje se imprima, pero el movimiento que intenta hacer puede que no sea válido y no tenga efecto. Por ejemplo, si nuestra regla de mayor prioridad hace que una ficha con 2 puntos se mueva hacia adelante, probablemente nuestra regla se ejecutará para cada ficha de 2 puntos viva hasta que encuentre una que no tenga ningún obstáculo delante y el movimiento se pueda realizar.

Lo ideal, pues, es que en vuestras reglas **comprobéis manualmente** que la casilla a la que os queréis mover está libre (o tiene un enemigo de menor nivel).