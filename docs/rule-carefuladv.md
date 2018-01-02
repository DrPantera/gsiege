# Careful advance

This rule from **Juan Manuel Morcillo** (a student from the University of Cádiz during the 2010-11 edition of the _Videogame Design_ module) serves as a good example of a careful advance towards nearby enemy pieces. It only moves pieces towards those in diagonally adjacent positions only if the attack can be resolved as a victory or a tie.

To do so, it checks that the opponent piece is uncovered and that its value is less than or equal to is own. There are four rules: one per direction.

```
(defrule EQUIPO-A::careful1
	(declare (salience 40))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	(ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	(tiempo ?t)
	(test (and (!= ?p1 6) (!= ?p1 1)))
	(test (and (or (> ?p1 ?p2) (= ?p1 ?p2)) (= ?y2 (+ ?y1 1)) (or (= ?x1 (+ ?x2 1)) (= ?x1 (- ?x2 1)))))
	=>
	(assert (mueve (num ?n1) (mov 3) (tiempo ?t)))) 

(defrule EQUIPO-A::careful2
	(declare (salience 39))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	(ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	(tiempo ?t)
	(test (and (!= ?p1 6) (!= ?p1 1)))
	(test (and (or (> ?p1 ?p2) (= ?p1 ?p2)) (= ?x2 (- ?x1 1)) (or (= ?y1 (+ ?y2 1)) (= ?y1 (- ?y2 1)))))
	=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::careful3
	(declare (salience 39))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	(ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	(tiempo ?t)
	(test (and (!= ?p1 6) (!= ?p1 1)))
	(test (and (or (> ?p1 ?p2) (= ?p1 ?p2)) (= ?x2 (+ ?x1 1)) (or (= ?y1 (+ ?y2 1)) (= ?y1 (- ?y2 1)))))
	=>
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::careful4
	(declare (salience 38))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	(ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	(tiempo ?t)
	(test (and (!= ?p1 6) (!= ?p1 1)))
	(test (and (or (> ?p1 ?p2) (= ?p1 ?p2)) (= ?y2 (- ?y1 1)) (or (= ?x1 (+ ?x2 1)) (= ?x1 (- ?x2 1)))))
	=>
	(assert (mueve (num ?n1) (mov 4) (tiempo ?t))))

```
