#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
# This file is part of Resistencia Cadiz 1812.                                #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by        #
# the Free Software Foundation, either version 3 of the License, or           #
# any later version.                                                          #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
# Copyright (C) 2010, Pablo Recio Quijano, <pablo.recioquijano@alum.uca.es>   #
###############################################################################

"""
Main file that indicates how to execute the application, and initialize
the environment
"""

import locale
import gettext
import gtk
import gtk.glade
import os
import logging

APP = 'resistencia1812'
DIR = os.path.join(os.getcwd(),"po")  #'/usr/share/locale'

gettext.textdomain(APP)
gettext.bindtextdomain(APP, DIR)
gtk.glade.textdomain(APP)
gtk.glade.bindtextdomain(APP, DIR)


# set the locale to LANG, or the user's default
locale.setlocale(locale.LC_ALL, '')

# this installs _ into python's global namespace, so we don't have to
# explicitly import it elsewhere

from resistencia.nls import gettext as _

from resistencia.gui import main_window
import resistencia.configure as configure

configure.load_configuration()
  
def main():
    "Main function"

    logging.basicConfig(format='[%(levelname)s] [%(filename)s (%(lineno)d) %(funcName)s] %(message)s', filename='log_gsiege', level=logging.DEBUG)
    logging.info("#" * 40)
    logging.info("Init logging")
    # Crea una nueva instancia de la clase Resistencia, que guarda todos los
    # cuadros de diálogo
    editor = main_window.Resistencia()

    # Muestra el cuadro de diálogo principal
    editor.window.show()

    # Lanza el bucle de GTK (?)
    gtk.main()
    logging.info("End logging\n\n")
    
if __name__ == "__main__":
    main()
