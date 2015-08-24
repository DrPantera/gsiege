# Barrido con peones #
Esta regla hará que todos los peones intenten barrer el tablero, llevándose por delante al mayor número de fichas posible. Suponemos que tenemos a todos los peones (ficha número 2) en la fila de vanguardia.

La idea es que vayan en fila. Así, una vez que todos los peones estén en la fila 2, empiecen a avanzar a la fila 3, en lugar de que ninguno de ellos se escape del pelotón.

```
(defrule EQUIPO-A::avance_peones_f2
    (declare (salience 60))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 2) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::avance_peones_f3
    (declare (salience 59))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 3) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
(defrule EQUIPO-A::avance_peones_f4
    (declare (salience 58))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 4) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
(defrule EQUIPO-A::avance_peones_f5
    (declare (salience 57))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 5) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
(defrule EQUIPO-A::avance_peones_f6
    (declare (salience 56))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 6) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
(defrule EQUIPO-A::avance_peones_f7
    (declare (salience 55))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 7) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
```

Existe una regla para cada fila, ya que hacerlo de manera genérica incrementaría la complejidad mucho. Además, así es más sencillo controlar la prioridad de los movimientos.