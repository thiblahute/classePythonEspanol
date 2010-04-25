#!/usr/bin/env python
import gtk
import sys

class ejemplo:
    def on_window_destroy(self, widget, data=None):
        """ Permite de terminar el programa cuando ceramos la ventana """
        gtk.main_quit()

    def __init__(self):
        consturctor_interfaz = gtk.Builder() #Instanciamos un objeto para constuir la interfaz
        builder.add_from_file ("ejemplo.glade") #Indicamos al "Builder" cual es el archivo que describe la interfaz
        self.ventana = builder.get_object("window") #Guardamos el objeto que describe la ventana en un objeto de classe 
        builder.connect_signals(self)

if __name__ == "__main__":
    ejemplo = ejemplo() #Instaciamos la classe "ejemplo", (eso llama el metodo "__init__")
    ejemplo.window.show() #Mostramos la ventana
    gtk.main()
