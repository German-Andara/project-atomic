import os
import random

DANIO_MISIL = 50
DANIO_LANZALLAMA = 40
DANIO_METRALLA = 30
CANTIDAD_SALUD= 100

class tanque:

    def __init__(self, salud, municiones, rango):
        self.salud = salud
        self.municiones = municiones
        self.rango = rango

    def obtener_salud(self):
        return self.salud  

    def reducir_salud(self, danio):
        if self.salud < danio:
            self.salud = 0
        else:
            self.salud -= danio

    def tiene_salud(self):
        return self.salud > 0

    def obtener_cantidad_de_misiles(self):
        return self.municiones[0]

    def obtener_cantidad_de_metrallas(self):
        return self.municiones[1]

    def obtener_cantidad_de_lanzallamas(self):
        return self.municiones[2]

    def utilizar_misil(self):
        if self.municiones[0] > 0:
            self.municiones[0] -= 1

    def utilizar_metralla(self):
        if self.municiones[1] > 0:
            self.municiones[1] -= 1

    def utilizar_lanzallama(self):
        if self.municiones[2] > 0:
            self.municiones[2] -= 1

    def tiene_municiones(self):
        m = self.municiones
        return m[0] > 0 or m[1] > 0 or m[2] > 0

    def tiene_misiles(self):
        return self.municiones[0] > 0

    def tiene_metrallas(self):
        return self.municiones[1] > 0

    def tiene_lanzallamas(self):
        return self.municiones[2] > 0

    def establecer_posicion(self, posicion):
        self.posicion = posicion

class tablero: 

    def __init__(self):
        jugador = tanque(100, [5, 3, 2], range(5))
        cpu = tanque(100, [5, 3, 2], range(5, 10))
        self.tanques = [jugador, cpu]
        self.celdas = []
        for i in range(10):
            self.celdas.append([])
            for j in range(10):
                self.celdas[i].append(' ')

    def limpiar_celdas(self):
        for i in range(10):
            for j in range(10):
                self.celdas[i][j] = " "

    def dibujar_ataque(self,tipo,coordenada1,coordenada2):
        jugador = self.tanques[0]
        [x,y] = jugador.posicion
        self.limpiar_celdas()
        self.celdas[x][y] = "T"
        if tipo == 'misil':
            self.celdas[coordenada1][coordenada2] = "*"
        elif tipo == "lanzallama":
            if coordenada2 == 1 :
                for j in range(5,10):
                    self.celdas[coordenada1][j] = "*"
            else:
                for j in range(5):
                    self.celdas[coordenada1][j] = "*"
        else:
            for i in range(coordenada1 - 1, coordenada1 + 2):
                for j in range(coordenada2 - 1, coordenada2 + 2):
                    self.celdas[i][j] = "*"
        self.imprimir_tablero()

    def imprimir_tablero(self):
        for i in range(10):
            for j in range(10):
                print(self.celdas[i][j],end="")
            print()        


    def posicion_inicial_jugador(self):
        jugador = self.tanques[0]
        print("definiendo posicion inicial del jugador")
        print("---------------------------------------")
        print()
        fila = int(input("ingrese la fila (de 0 a 9): "))
        columna = int(input("ingrese la columna (de 0 a 4): "))
        print()
        if(0 <= fila and fila <= 10 and 0 <= columna and columna <= 4):
            jugador.establecer_posicion([fila, columna])
            print("se ha definido la posicion del jugador,su localizacion es ", fila, ",", columna, sep="")
        else:
            jugador.establecer_posicion([0, 0])
            print("la posicion no es valida")
            print("se definio la posicion inicial del jugador en 0,0")
            print()

    def posicion_inicial_cpu(self):
        cpu = self.tanques[1]
        fila = random.randrange(10)
        columna = random.randrange(5, 10)
        cpu.establecer_posicion([fila, columna])

    def datos_jugador(self):
        jugador = self.tanques[0]
        print("Datos por turno del jugador")
        print()
        print("salud del jugador:",jugador.obtener_salud())
        print()
        print("metralla:",jugador.obtener_cantidad_de_metrallas())
        print()
        print("lanzallama:",jugador.obtener_cantidad_de_lanzallamas())
        print()
        print("misil:",jugador.obtener_cantidad_de_misiles())
        print()
        #print("salud del jugador:",jugador.obtener_salud(),"municiones:","\n\nmetralla:"jugador.obtener_cantidad_de_metrallas(),"\n\nlanzallama:"jugador.obtener_cantidad_de_lanzallamas(),"\n\nmisil:"jugador.obtener_cantidad_de_misiles())
        
           

    def datos_cpu(self):
        cpu = self.tanques[1]
        print("Datos por turno cpu tanque:")
        print()
        print("salud del cpu:",cpu.obtener_salud())
        print()
        print("metralla cpu:",cpu.obtener_cantidad_de_metrallas())
        print()
        print("lanzallama cpu:",cpu.obtener_cantidad_de_lanzallamas())
        print()
        print("misil cpu:",cpu.obtener_cantidad_de_misiles())
        print()
        #print("salud del jugador:",cpu.obtener_salud(),"municiones:","\n\nmetralla:"cpu.obtener_cantidad_de_metrallas(),"\n\nlanzallama:"cpu.obtener_cantidad_de_lanzallamas(),"\n\nmisil:"cpu.obtener_cantidad_de_misiles())
        

    def ataque_jugador(self):
        jugador = self.tanques[0]
        cpu = self.tanques[1]
        [x, y] = cpu.posicion #x,y representan la fila y la columna de tanque cpu
        municion = input("que municion desea utilizar: ")
        if municion == "misil":
            if jugador.tiene_misiles():
                fila = int(input("ingrese la fila a atacar (de 0 a 9): "))
                columna = int(input("ingrese la columna a atacar (de 5 a 9): "))
                if 0 <= fila and fila <= 9 and 5 <= columna and columna <= 9:
                    if fila == x and columna == y:
                        cpu.reducir_salud(DANIO_MISIL)
                        print("Tu enemigo ha recibido danio:","\n\nSalud Actual:",cpu.reducir_salud(DANIO_MISIL),"\n\nDanio Recibido:",DANIO_MISIL,"misil:",jugador.obtener_cantidad_de_misiles())
                    else:
                        print("no le has causado danio a tu enemigo","\n\nsalud actual:",cpu.obtener_salud())
                    jugador.utilizar_misil()
                    self.dibujar_ataque("misil",fila,columna)
                else:
                    print("no es posible atacar en esa direccion")
            else:
                print("no posee misiles, ha perdio el ataque")
        elif municion == "lanzallama": #mostramos qu secede en el ataque si usamos lanzallama
            if jugador.tiene_lanzallamas():
                fila = int(input("ingrese la fila a atacar (de 0 a 9): "))
                if 0 <= fila and fila <= 9:
                    if fila == x:
                        cpu.reducir_salud(DANIO_LANZALLAMA)
                        print("Tu enemigo ha recibido danio:","\nSalud Actual:",cpu.reducir_salud(DANIO_LANZALLAMA),"\n\nDanio Recibido:",DANIO_LANZALLAMA,"lanzallama:",jugador.obtener_cantidad_de_lanzallamas())
                    else:
                        print("no le has causado danio a tu enemigo","\nsalud actual:",cpu.obtener_salud())
                    jugador.utilizar_lanzallama()
                    self.dibujar_ataque("lanzallama",fila,1)
                else:
                    print("no es posible atacar en esa direccion")
            else:
                print("no posee lanzallama,ha perdidio el ataque")
        elif municion == "metralla":
            if jugador.tiene_metrallas():
                fila = int(input("ingrese la fila a atacar (de 1 a 8): "))
                columna = int(input("ingrese la columna a atacar (de 6 a 8): "))
                if 1 <= fila and fila <= 8 and 6 <= columna and columna <= 8:
                    if x in range(fila - 1, fila + 2) and y in range(columna - 1, columna + 2):
                        cpu.reducir_salud(DANIO_METRALLA)
                        print("tu enemigo ha recibido danio:","\nsalud actual:",cpu.reducir_salud(DANIO_METRALLA),"\n\nDanaio Recibido:",DANIO_METRALLA,"METRALLA:",jugador.obtener_cantidad_de_metrallas())
                    else:
                        print("no le has causado danio a tu enemigo","\nsalud Actual:",cpu.obtener_salud())
                    jugador.utilizar_metralla()
                    self.dibujar_ataque("metralla",fila,columna)
                else:
                    print("no es posble atacar en esa direccion")
            else:
                print("no posee metralla,ha perdidio la oportunidad de atacar")
        else:
            print("opcion invalida, ya no puede atacar")

    def ataque_cpu(self):
        jugador = self.tanques[0]
        cpu = self.tanques[1]
        [x, y] = jugador.posicion #x,y representan la fila y la columna de tanque jugador
        municion = random.choice(["misil","lanzallama","metralla"])
        if municion == "misil":
            if cpu.tiene_misiles():
                fila = random.randrange(10)
                columna = random.randrange(0,5)
                if fila == x and columna == y:
                    jugador.reducir_salud(DANIO_MISIL)
                    jugador.obtener_salud() #aqui van los resultados cuando el ataque es exitoso
                    print("Tu enemigo ha recibido danio:","\n\nSalud Actual:",jugador.obtener_salud(),"\n\nDanio Recibido:",DANIO_MISIL,"misil:",cpu.obtener_cantidad_de_misiles())
                else:
                    print("no le has causado danio a tu enemigo","\nsalud actual:",jugador.obtener_salud())
                cpu.utilizar_misil()
                self.dibujar_ataque("misil",fila,columna)
            else:
                print("no posee misiles, ha perdio el ataque")
        elif municion == "lanzallama":
            if cpu.tiene_lanzallamas():
                fila=random.randrange(10)
                if fila == x:
                    jugador.reducir_salud(DANIO_LANZALLAMA)
                    print("Tu enemigo ha recivido danio:","\n\nSalud Actual:",jugador.obtener_salud(),"\n\nDanio Recivido:",DANIO_LANZALLAMA,"lanzallama:",cpu.obtener_cantidad_de_lanzallamas())
                else:
                    print("no le has causado danio a tu enemigo","\n\nsalud actual:",jugador.obtener_salud())
                cpu.utilizar_lanzallama()
                self.dibujar_ataque("lanzallama",fila,0)
            else:
                print("no posee lanzallama,ha perdidio el ataque")
        else:
            if cpu.tiene_metrallas():
                fila = random.randrange(1,9)
                columna = random.randrange(1,4)
                if fila == x and columna == y:
                    jugador.reducir_salud(DANIO_METRALLA)
                    print("tu enemigo ha recivido danio:","\n\nsalud actual:",jugador.obtener_salud(),"\n\nDanaio Recivido:",DANIO_METRALLA,"METRALLA:",cpu.obtener_cantidad_de_metrallas())
                else:
                    print("no le has causado danio a tu enemigo","\n\nsalud Actual:",jugador.obtener_salud())
                cpu.utilizar_metralla()
                self.dibujar_ataque("metralla",fila,columna)
            else:
                print("no posee metralla,ha perdidio la oportunidad de atacar")



    def mover_jugador(self):
        jugador = self.tanques[0]
        [x, y] = jugador.posicion
        fila=int(input("ingrese la fila a la que desea moverse: "))
        columna=int(input("ingrese la columna a la que desea moverse: "))
        if fila in range(x - 1, x + 2) and columna in range(y - 1, y + 2):
            jugador.establecer_posicion([fila, columna])
            print('Se movio a ', fila, ',', columna)
        else: 
            print("La direccion que ha ingresado no es valida, ha perdido su turno")

    def mover_cpu(self):
        cpu = self.tanques[1]
        [x, y] = cpu.posicion
        fila = random.randrange(x - 1, x + 2)
        columna = random.randrange(y - 1, y + 2)
        cpu.establecer_posicion([fila, columna])

    def comenzar_partida(self):
        jugador = self.tanques[0]
        cpu = self.tanques[1]
        bitacora=[]
        self.posicion_inicial_jugador()
        self.posicion_inicial_cpu() 
        turno=1
        while jugador.tiene_salud() and cpu.tiene_salud() and (jugador.tiene_municiones() or cpu.tiene_municiones()):
            self.datos_jugador()#mostrar los datos que mostrara
            self.ataque_jugador()#defino el tipo de ataque
            self.mover_jugador()#posicion a la que se movera el jugador,varificara si la posicion es validad
            self.datos_cpu()
            self.ataque_cpu()
            self.mover_cpu()
            turno+=1
        if jugador.tiene_salud() and not cpu.tiene_salud():
            print("el jugador gano")
            while turno>=1 :
                bitacora.append()
        elif cpu.tiene_salud() and not jugador.tiene_salud():
            print("ha ganado tu enemigo")
        else:
            print("empate")

if __name__=="__main__":
    t = tablero()
    t.comenzar_partida()