file=open('Descripcion de el proyecto','a')
file.write(""""Salud: cada jugador tendra una salud inicial de 100.

Rango: Los movimientos de cada jugador estaran limitados a una matriz de 10x10
10x5 para cada jugador. 

Cada Tanque tendra tres tipos de armas : misil,lanzallamas y metralla con una cantidad de 5 municiones cada una, el danio que cada muncion causa al enemigo esta descrito de la siguiente manera:

misil:Cada disparo tiene la capacidad de atinar un golpe de 50 de
danio. Afecta una sola celda del tablero enemigo.

Lanzallamas:Cada disparo tiene la capacidad de atinar un golpe de 40 de
danio. Afecta toda una fila del tablero enemigo.


metralla:Cada disparo tiene la capacidad de atinar un golpe de 30 de
danio. Afecta la celda seleccionada y todas las celdas vecinas del tablero enemigo.

en el tablero el danio causado por el tipo de arma se representara mediante el caracter (*) y el tanque del jugador y enemigo se representara mediante la letra T. 

Los turnos de ataque de cada jugador dependeran de la cantidad de municiones que cada uno posea, osea que si en dicho caso el cpu por ejemplo se queda sin municiones de cuaquier tipo de arma, entonces no tiene turnos para seguir atacando y aunque este posea salud mayor que la de el enemigo perdera automaticamente.

Movimientos de el jugador:

Cada jugador podra moverse a la casilla vecina solamente.


Ganar el juego.

Para ganar el juego tendra que pasar lo siguiente:

1-que algun jugador quede con salud cero.
2-que algun jugador se quede sin municiones para seguir atacando pierde automaticamente.
 """)

file.close()

