# Sweep with the 6 piece

This is one of the most common rules. The idea is to use the most powerful piece (the one worth six) to reach the other side of the table and sweep the rows of the opponent. Assume we start with this formation file:
```
2:2:2:2:2:2:2:6
2:5:5:4:4:3:3:1
```

This strategy is executed in two stages. In the first stage, we check that our 6-piece exists and that it is **not** in the top row. In that case, we make it move towards the enemy.
```
(defrule EQUIPO-A::sweep6_stage1
    (declare (salience 80))
    (tiempo ?t)
    (ficha (equipo "A") (num ?n) (pos-y ?y) (puntos 6))
    (test (<> ?y 8))
    =>
    (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)
```

In the second stage, we check that the 6-piece exists and that it is in the back row of the enemy (`(pos-y 8)`), having it sweep the row.
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
