# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# This file is part of Resistencia Cadiz 1812.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Copyright (C) 2007, Manuel Palomo Duarte
# Copyright (C) 2009, Pablo Recio Quijano
#----------------------------------------------------------------------

"""
 @file mover.py
"""

def LoadFunctions(clips):
    #----------------------------------
    # It handles to make the right movement for the team
    #----------------------------------
    # Module name
    mod_name = "MOVER"
    # Module body
    mod_body  = "(import MAIN deftemplate initial-fact movio-r ficha-r fichamuerta fichamuerta-r dimension tiempo mueve turno tiempo-inicial obstaculo obstaculo-r)"
    mod_body += "(import MAIN deffunction ?ALL)"
    # Building the module
    mod_mover = clips.BuildModule(mod_name, mod_body)
    #----------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'movimiento_invalido_ficha'
    # Rule precontents
    rule_prec  = '(declare (salience 90))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))'
    rule_prec += '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y) (descubierta ?d))'
    rule_prec += '(dimension ?dim)'
    rule_prec += '(tiempo-inicial ?ti)'
    rule_prec += '(test (= 0 (str-compare (turno ?ti ?t) ?e)))'
#    rule_prec += '(test (mov-valido ?dim ?m ?x ?y))'
    rule_prec += '(ficha-r (equipo ?e) (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2)))'
#    rule_prec += '(not (movido ?e ?t))'
    # =>
    # Rule body
    rule_body  = '(retract ?h1)'
    rule_body += '(printout t "Movimiento INVÁLIDO, type FICHA " ?m crlf)'
    # Building the rule
    movimiento = mod_mover.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'movimiento_invalido_obstaculo'
    # Rule precontents
    rule_prec  = '(declare (salience 90))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))'
    rule_prec += '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y) (descubierta ?d))'
    rule_prec += '(dimension ?dim)'
    rule_prec += '(tiempo-inicial ?ti)'
    rule_prec += '(test (= 0 (str-compare (turno ?ti ?t) ?e)))'
#    rule_prec += '(test (mov-valido ?dim ?m ?x ?y))'
    rule_prec += '(obstaculo-r (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2)))'
#    rule_prec += '(not (movido ?e ?t))'
    # =>
    # Rule body
    rule_body  = '(retract ?h1)'
    rule_body += '(printout t "Movimiento INVÁLIDO, type OBSTACULO " ?m crlf)'
    # Building the rule
    movimiento = mod_mover.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

   
   
    # ---------------------------------
    # Rule name
    rule_name = 'movimiento'
    # Rule precontents
    rule_prec  = '(declare (salience 90))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))'
    rule_prec += '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y) (descubierta ?d))'
    rule_prec += '(dimension ?dim)'
    rule_prec += '(tiempo-inicial ?ti)'
    rule_prec += '(test (= 0 (str-compare (turno ?ti ?t) ?e)))'
    rule_prec += '(test (mov-valido ?dim ?m ?x ?y))'
    rule_prec += '(not (ficha-r (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2))))'
    rule_prec += '(not (obstaculo-r (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2))))'
    rule_prec += '(not (movido ?e ?t))'
    # =>
    # Rule body
    rule_body  = '(retract ?h1 ?h2)'
    rule_body += '(printout t "Movimiento de "?e", "?n"(puntos "?p") :mov "?m crlf)'
    rule_body += '(assert (movido ?e ?t))'
    rule_body += '(assert (movio-r (equipo ?e) (num ?n) (turno ?t) (mov ?m) (pos-x-ini ?x) (pos-y-ini ?y) (puntos ?p)))'
    rule_body += '(assert (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x (+ ?x (mov-x ?m))) (pos-y (+ ?y (mov-y ?m))) (descubierta ?d)))'
    # Building the rule
    movimiento = mod_mover.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    mod_mover.BuildRule("verificar_movimiento", "(declare (salience 89)) (tiempo ?t) (not (movido ?e ?t))", '(printout t "WARNING: No hubo ningún movimiento en " ?t " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" crlf)')

    # ---------------------------------
    # Rule name
    rule_name = 'ataque-1'
    # Rule precontents
    rule_prec  = '(declare (salience 91))'
    rule_prec += '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))'
    rule_prec += '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))'
    rule_prec += '(dimension ?dim)'
    rule_prec += '(tiempo-inicial ?ti)'
    rule_prec += '(test (= 0 (str-compare (turno ?ti ?t) ?e)))'
    rule_prec += '(test (mov-valido ?dim ?m ?x ?y))'
    rule_prec += '?h3 <- (ficha-r (equipo ?e2&~?e) (num ?n2) (puntos ?p2&:(> ?p ?p2)) (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2)))'
    rule_prec += '(ficha-r (num ?n2) (puntos ?p2))'
    rule_prec += '(not (movido ?e ?t))'
    # =>
    # Rule body
    rule_body  = '(retract ?h1 ?h2 ?h3)'
    rule_body += '(printout t "Ataque con victoria de "?n"(puntos "?p") : mov "?m crlf)'
    rule_body += '(assert (movido ?e ?t))'
    rule_body += '(assert (movio-r (equipo ?e) (num ?n) (puntos ?p) (turno ?t) (mov ?m) (pos-x-ini ?x) (pos-y-ini ?y)))'
    rule_body += '(assert (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x (+ ?x (mov-x ?m))) (pos-y (+ ?y (mov-y ?m))) (descubierta 1)))'
    rule_body += '(assert (fichamuerta-r (num ?n2) (equipo ?e) (puntos ?p2) (pos-x (+ ?x (mov-x ?m))) (pos-y (+ ?y (mov-y ?m)))))'
    # Building the rule
    ataque_1 = mod_mover.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'ataque-2'
    # Rule precontents
    rule_prec  = '(declare (salience 91))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))'
    rule_prec += '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))'
    rule_prec += '(dimension ?dim)'
    rule_prec += '(tiempo-inicial ?ti)'
    rule_prec += '(test (= 0 (str-compare (turno ?ti ?t) ?e)))'
    rule_prec += '(test (mov-valido ?dim ?m ?x ?y))'
    rule_prec += '?h3 <- (ficha-r (equipo ?e2&~?e) (num ?n2) (puntos ?p) (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2)))'
#    rule_prec += '(test (<> 0 (str-compare ?e ?e2)))'
    rule_prec += '(not (movido ?e ?t))'
    # =>
    # Rule body
    rule_body  = '(retract ?h1 ?h2 ?h3)'
    rule_body += '(printout t "Ataque con empate de "?n"(puntos "?p") : mov "?m crlf)'
    rule_body += '(assert (movido ?e ?t))'
    rule_body += '(assert (movio-r (equipo ?e) (num ?n) (puntos ?p) (turno ?t) (mov ?m) (pos-x-ini ?x) (pos-y-ini ?y)))'
    rule_body += '(assert (fichamuerta-r (num ?n)  (equipo ?e) (puntos ?p) (pos-x (+ ?x (mov-x ?m))) (pos-y (+ ?y (mov-y ?m)))))'
    rule_body += '(assert (fichamuerta-r (num ?n2)  (equipo ?e2) (puntos ?p) (pos-x (+ ?x (mov-x ?m))) (pos-y (+ ?y (mov-y ?m)))))'

    
    # Building the rule
    ataque_2 = mod_mover.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'ataque-3'
    # Rule precontents
    rule_prec  = '(declare (salience 91))'
    rule_prec += '(tiempo ?t)'
    rule_prec += '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))'
    rule_prec += '?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))'
    rule_prec += '(dimension ?dim)'
    rule_prec += '(tiempo-inicial ?ti)'
    rule_prec += '(test (= 0 (str-compare (turno ?ti ?t) ?e)))'
    rule_prec += '(test (mov-valido ?dim ?m ?x ?y))'
    rule_prec += '?h3 <- (ficha-r (equipo ?e2&~?e) (num ?n2) (puntos ?p2&:(< ?p ?p2)) (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2)))'
    rule_prec += '(not (movido ?e ?t))'
    # =>
    # Rule body
    rule_body  = '(retract ?h1 ?h2 ?h3)'
    rule_body += '(printout t "Ataque con derrota de "?n"(puntos "?p") : mov "?m crlf)'
    rule_body += '(assert (movido ?e ?t))'
    rule_body += '(assert (movio-r (equipo ?e) (num ?n) (puntos ?p) (turno ?t) (mov ?m) (pos-x-ini ?x) (pos-y-ini ?y)))'    
    rule_body += '(assert (ficha-r (equipo ?e2) (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2) (descubierta 1)))'
    rule_body += '(assert (fichamuerta-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x2) (pos-y ?y2)))'

    # Building the rule
    ataque_3 = mod_mover.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------

    # ---------------------------------
    # Rule name
    rule_name = 'limpia'
    # Rule precontents
    rule_prec  = '(declare (salience 0))'
    rule_prec += '?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))'
    # =>
    # Rule body
    rule_body  = '(retract ?h1)'
    # Building the rule
    limpia = mod_mover.BuildRule(rule_name, rule_prec, rule_body)
    # ---------------------------------
