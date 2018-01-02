# When 50 turns are left

When there are only so many turns left, this rule will go all out with the pieces worth 4:

```
(defrule EQUIPO-A::check50
	(declare (salience 70))
	(tiempo ?t)
	(test (< ?t 50))
	=>
	(assert (allout4)))

(defrule EQUIPO-A::goallout4
	(declare (salience 40))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 4))
	(tiempo ?t)
	(allout4)
	=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t))))
```
