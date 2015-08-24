# Avance/ataque precavido #

Esta regla, del alumno de la UCA **Juan Manuel Morcillo** (del curso 2010-11 de la asignatura _Diseño de Videojuegos_) nos puede servir de regla de avance precavido hacia fichas enemigas cercanas, ya que hace que las piezas se muevan hacia las que se encuentren en casillas contiguas diagonales solo si el ataque puede saldarse con una victoria o un empate.

Para ello, comprueba que la ficha enemiga esté descubierta y su puntuación sea menor o igual que la de la ficha propia. Las cuatro reglas corresponden a las cuatro posibles direcciones.

```
(defrule EQUIPO-A::precavido1
	(declare (salience 40))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	(ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	(tiempo ?t)
	(test (and (!= ?p1 6) (!= ?p1 1)))
	(test (and (or (> ?p1 ?p2) (= ?p1 ?p2)) (= ?y2 (+ ?y1 1)) (or (= ?x1 (+ ?x2 1)) (= ?x1 (- ?x2 1)))))
	=>
	(assert (mueve (num ?n1) (mov 3) (tiempo ?t)))) 

(defrule EQUIPO-A::precavido2
	(declare (salience 39))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	(ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	(tiempo ?t)
	(test (and (!= ?p1 6) (!= ?p1 1)))
	(test (and (or (> ?p1 ?p2) (= ?p1 ?p2)) (= ?x2 (- ?x1 1)) (or (= ?y1 (+ ?y2 1)) (= ?y1 (- ?y2 1)))))
	=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::precavido3
	(declare (salience 39))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	(ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	(tiempo ?t)
	(test (and (!= ?p1 6) (!= ?p1 1)))
	(test (and (or (> ?p1 ?p2) (= ?p1 ?p2)) (= ?x2 (+ ?x1 1)) (or (= ?y1 (+ ?y2 1)) (= ?y1 (- ?y2 1)))))
	=>
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::precavido4
	(declare (salience 38))
	(ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	(ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	(tiempo ?t)
	(test (and (!= ?p1 6) (!= ?p1 1)))
	(test (and (or (> ?p1 ?p2) (= ?p1 ?p2)) (= ?y2 (- ?y1 1)) (or (= ?x1 (+ ?x2 1)) (= ?x1 (- ?x2 1)))))
	=>
	(assert (mueve (num ?n1) (mov 4) (tiempo ?t))))

```