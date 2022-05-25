class kala:
    grados = 0.0
    escala = ""
    def converToGrados(self, grados, escala):
        if escala == 'F' and self.escala == 'C':
            return float(5*(grados-32)/9)
        elif escala == 'C' and self.escala == 'F':
            return float(9*(grados+32)/5)
        elif escala == 'K' and self.escala == 'C':
            return float(grados - 273.15)
        elif escala == 'C' and self.escala == 'K':
            return float(grados + 273.15)
        elif escala == 'F' and self.escala == 'K':
            return float((5*(grados-32)/9) + 273.15)
        else:
            return float(9*((grados - 273.15)+32)/5)
    def converToEscala(self, escala):
        if escala == "F" and self.escala == "C":
            return "C"
        elif escala == "C" and self.escala == "F":
            return "F"
        elif escala == "K" and self.escala == "C":
            return "C"
        elif escala == "C" and self.escala == "K":
            return "K"
        elif escala == "F" and self.escala == "K":
            return "K"
        elif escala == "K" and self.escala == "F":
            return "F"
    def adder(self, escala, grados):
        if escala != self.escala:
            escala = self.converToEscala(escala)
            grados = self.converToGrados(grados, escala)
        #print(escala)
        #print(grados)
        print(str(self.grados + grados) + escala)

    def sub(self, escala, grados):
        if escala != self.escala:
            escala = self.converToEscala(escala)
            grados = self.converToGrados(grados, escala)
        print(str(self.grados - grados) + escala)
    
    def multi(self, escala, grados):
        if escala != self.escala:
            escala = self.converToEscala(escala)
            grados = self.converToGrados(grados, escala)
        print(str(self.grados*grados) + escala)
    
    def div(self, escala, grados):
        if escala != self.escala:
            escala = self.converToEscala(escala)
            grados = self.converToGrados(grados, escala)
        print(str(self.grados/grados) + escala)

a = kala()
a.grados = 150
a.escala = "F"

b = kala()
b.grados = 50
b.escala = "C"

a.div(b.escala, b.grados)