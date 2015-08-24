# Cuando Queden 50 Turnos #

Cuando quedan 50 turnos lanza los 4 al ataque

```
(defrule EQUIPO-A::comprueba50
	(declare (salience 70))
	(tiempo ?t)
	(test (< ?t 50))
	=>
	(assert (al-ataque4)))

(defrule EQUIPO-A::ataca4
	(declare (salience 40))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 4))
	(tiempo ?t)
	(al-ataque4)
	=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

```