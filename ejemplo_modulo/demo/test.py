#!/usr/bin/env python

class testMadre():
    
    def TestPrint(self):
        print "     >Escribiando desde el modulo demo: fonccion testPrint de la classe madre"

    def Print(self):
        print "     >Veamos si el la implementacion de la classe hija imprima en ves de esa fonccion"

class test(testMadre):
    def Print(self):
        print "     >El hijo esta imprimiando!!"
