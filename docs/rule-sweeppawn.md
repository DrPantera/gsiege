# Sweep with the pawns

This rule will have all pawns sweep the board, trying to defeat as many pieces as possible. We will assume we have all pawns in the front row.

The idea is to have them all stay in a row: first, they will all advance to row 2, then to row 3, and so on, without breaking formation.

```
(defrule EQUIPO-A::advance_pawns_f2
    (declare (salience 60))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 2) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::advance_pawns_f3
    (declare (salience 59))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 3) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
(defrule EQUIPO-A::advance_pawns_f4
    (declare (salience 58))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 4) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
(defrule EQUIPO-A::advance_pawns_f5
    (declare (salience 57))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 5) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
(defrule EQUIPO-A::advance_pawns_f6
    (declare (salience 56))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 6) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
(defrule EQUIPO-A::advance_pawns_f7
    (declare (salience 55))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y 7) (puntos 2))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
```

There is a rule for each piece, since doing it in a more parametric form would increase the complexity significantly. This also allows for tweaking the priority, changing the order in which pawns advance to the next row.
