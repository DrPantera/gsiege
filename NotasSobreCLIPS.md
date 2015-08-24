Para indicar en CLIPS que algo es distinto se usa <>, por ejemplo (<> ?y ?y2)

Para indicar que no existe una ficha determinada se usa el not, por ejemplo:

```
(defrule EQUIPO-A::basica-3
  (declare (salience 22))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 4))
  (not (ficha (equipo "A") (pos-x 4) (pos-y 4)))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))
```

Y a ese not se le pueden poner condiciones incrustadas con &: por ejemplo

```
(defrule EQUIPO-A::basica-3
  (declare (salience 22))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 4))
  (not (ficha (equipo "A") (pos-x ?x) (pos-y ?y2&:(= ?y2 (+ ?y 1)))))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))
```

Más información en en [Manual de CLIPS](http://clipsrules.sourceforge.net/OnlineDocs.html)