import random
import os

salud=100

class Tanque:
    def __init__(self,salud,municion,movimiento):
        self.salud=salud
        self.municion=municion
        self.movimiento=movimiento

    def get_salud(self):
        if self.salud>0:
            return self.salud    

    def recibir_danio(self,danio):
        if self.salud<danio:
            return "Has perdido"
        else:
            salud=self.salud-danio
            return salud


    def get_misil(self):
        return self.municion[0]

    def get_lanzallama(self):
        return self.municion[1]

    def get_metralla(self):
        return self.municion[2]

    def lanzar_misil(self):
        if self.get_misil()>0:
            ataque=self.municion[0]-1
            return ataque
        else:
            return "Ya no tienes misiles para atacar"


    def lanzar_lanzallama(self):
        if self.get_misil()>0:
            ataque=self.municion[1]-1
            return ataque
        else:
            return "Ya no tienes lanzallama para atacar"


    def lanzar_metralla(self):
        if self.get_misil()>0:
            ataque=self.municion[2]-1
            return ataque
        else:
            return "Ya no tienes metralla para atacar"


    def cantidad_municiones(self):
        m=self.municion
        return m[0]>0 or m[1]>0 or m[2]>0


    def mi_posicion(self):
        return self.movimiento





class Tablero:
    def __init__(self):
        jugador1=Tanque(salud,[5,3,3],range(5))
        cpu=Tanque(salud,[5,3,3],range(5,10))
        self.tanques=[jugador1,cpu]
        self.celdas=[]
        for i in range(10):
            self.celdas.append([])
            for j in range(10):
                self.celdas[i].append(' ')


    def limpiar_celdas(self):
        for i in range(10):
            for j in range(10):
                self.celdas[i][j] = " "


                







            
                                    
        


        