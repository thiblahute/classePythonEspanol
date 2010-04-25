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

