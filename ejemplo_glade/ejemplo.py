#!/usr/bin/env python
#
#       ejemplo.py
#
# Copyright (C) 2010 Thibault Saunier <tsaunier@gnome.org>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

import gtk

class ejemplo:
    def on_window_destroy(self, widget, data=None):
        """ Permite de terminar el programa cuando ceramos la ventana """
        gtk.main_quit()

    def __init__(self):
        consturctor_interfaz = gtk.Builder() #Instanciamos un objeto para constuir la interfaz
        consturctor_interfaz.add_from_file ("ejemplo.glade") #Indicamos al "Builder" cual es el archivo que describe la interfaz
        self.ventana = consturctor_interfaz.get_object("window") #Guardamos el objeto que describe la ventana en un objeto de classe 
        consturctor_interfaz.connect_signals(self)

if __name__ == "__main__":
    ejemplo = ejemplo() #Instaciamos la classe "ejemplo", (eso llama el metodo "__init__")
    ejemplo.ventana.show() #Mostramos la ventana
    gtk.main()
