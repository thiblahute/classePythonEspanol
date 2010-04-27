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

class time():
    def     __init__(self, hora=0, minutos=0, segundos=0):
        print "Instanciacion de la clase"
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos

    def set_hora(self, hora):
        self.hora = hora
    
    def print_hora (self):
        print "Son las", str (self.hora), " horas", str (self.minutos), " minutos", str (self.segundos), " segundos"

if __name__ == "__main__":
    hora = time()
    hora.print_hora ()

