# Barrer con el seis #
Esta regla es de las más típicas que hay. Consiste en hacer que el seis, la ficha más poderosa, llegue hasta el otro lado del tablero y barra las filas del enemigo. Vamos a suponer que partimos con el siguiente fichero de formación:

```
2:2:2:2:2:2:2:6
2:5:5:4:4:3:3:1
```

Esta estrategia se ejecuta en dos partes. En la primera parte, comprobamos que exista la ficha 6 de nuestro equipo y que **no se encuentre** en la fila superior. En tal caso, hacemos que se mueva verticalmente hacia el enemigo.
```
(defrule EQUIPO-A::barrido6_paso1
    (declare (salience 80))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y ?y) (puntos 6))
    (test (<> ?y 8))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
```

En la segunda parte, comprobamos que exista la ficha 6 y que ya se encuentre en la retaguardia del enemigo (pos-y 8), caso en el que hacemos que barra.
```
(defrule EQUIPO-A::barrido6_paso2
    (declare (salience 80))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y 8) (puntos 6))
    (test (<> ?x 8))
    =>
    (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)
```