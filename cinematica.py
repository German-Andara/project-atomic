import math

"""bienvenido a este programa cuya funcion es contestar a ciertas preguntas sobre la cinematica en
	2d, para ello hay ciertas funciones que reciven varios parametros los cuales varian dependiendo de el usuario,
	tales parametros tratan sobre la velocidad incial o el tiempo ambos sujetos a la gravdad que se este ejerciendo,
	la cual tambien puede variar ya que en el programa esta no esta de manera fija , por lo que podemos ver que pasa si
	un proyectil es lanzado en jupyter o marte."""

#crearemos las funciones para nuestros objetos fundamentales

#para nuestro primer objeto fundamental altura "y(t)":

def obj_y_t(y_0,v_y_0,t,a):
	y_t=y_0+v_y_0+a*(t**2)/2
	return y_t

# para el objeto fundamental x(t):
def obj_x_t(x_0,v_x_0,t):
	x_t=x_0+v_x_0*t
	return x_t


#para el objeto fundamental r(t):

def obj_r_t(y_0,v_y_0,x_0,v_x_0,t,a):
	r_t=[]
	r_t.append(obj_y_t(y_0,v_y_0,t,a))
	r_t.append(obj_x_t(x_0,v_x_0,t))
	return r_t




#crear ciertas funciones que ayuden a la hora de consultas sobre la cinematica:



#velocidad de el proyectil si este es lanzado de forma horizontal:


def velocidad_proyectil(v_0,t,a):
	v=v_0+a*t
	pr=(v/v_0)*100
	return pr





#velocidad de un proyectil en el caso que este es lanzdo desde un lugar de altura h y en donde las ecuaciones estan
#en terminos de el tiempo t.

def velocidad(theta,v_0,t,a):
	vx=v_0*math.cos(theta)*t
	vy=-v_0*math.sin(theta)-a*t
	v=math.sqrt((vx**2)+(vy**2))
	pr=v_0*(1/100)*v
	return pr

	

#en que tiempo t una pelota definida en su estado inicial cae al suelo:	

def tiempo_de_caida(y_0,v_y_0,y_t,a):
	if ((v_y_0**2)-4*(a/2)*(y_0-y_t))<0:
		print("la solucion de la ecuacion son numeros complejos: ")
	else:
		t1=(-v_y_0+(math.sqrt(v_y_0**2-(4*(a/2)*(y_0-y_t)))))/a
		t2=(-v_y_0-(math.sqrt(v_y_0**2-(4*(a/2)*(y_0-y_t)))))/a
		print("el tiempo o tiempos posibles en que la pelota toque el suelo es :")
		print(t1)
		print()
		print(t2)

#en este codigo anterior lo que tenemos que tener en cuenta se presentan dos soluciones y la que nos interesa es el
#caso positivo. 







#problemas especiales:

def colicion(v_0,theta_2,t,t1,a):
	theta_1=30
	#tenemos una trayectoria fija y supondremos que la trayectoria corresponde al primer proyectil
	x_1=v_0*math.cos(math.radians(theta_1))*t
	y_1=v_0*math.sin(math.radians(theta_1))-(1/2)*a*t**2
	r_1=[]
	r_1.append(x_1)
	r_1.append(y_1)
	x_2=v_0*math.cos(math.radians(theta_2))*(t-t1)
	y_2=v_0*math.sin(math.radians(theta_2))-(1/2)*a*(t-t1)**2
	#si igualamos cada componente x_1 con x_2 y y_1 con y_2 tenemos el tiempo de coalicion:
	t_col=((2*v_0)/a)*(math.sin(math.radians(theta_1-theta_2)))*(math.cos(math.radians(theta_2))/((math.cos(math.radians(theta_2))**2
		- math.cos(math.radians(theta_1))**2)))
	r_2=[]
	r_2.append(x_2)
	r_2.append(y_2)
	print("el tiempo de colicion es :")
	print()
	print(t_col)
	print("con trayectoria:")
	print()
	print(r_2)
	



def interfaz():
	print("HOLA , que desea saber sobre cinematica en 2d?:")
	print()
	print("1-evolucion de la altura y(t) en un tiempo t para un proyectil\n2-Movimiento horizontal de un proyectil\n",
	'3-trayectoria de el proyectil\n',
	"4-velocidad de el proyectil si este es lanzado de forma horizontal\n",
	"5-velocidad de un proyectil en el caso que este es lanzdo desde un lugar de altura h\n",
	"6-en que tiempo t una pelota definida en su estado inicial cae al suelo\n",
	"7-colicion de dos proyectiles")
	eleccion=input("ingrese su eleccion:")
	if eleccion=="1":
		print("ingrese los siguentes datos nesesarios:y_0,v_y_0,t,a\n")
		y_0=int(input("y0:"))
		v_y_0=int(input("vy0:"))
		t=int(input("t:"))
		a=float(input("a:"))
		print(obj_y_t(y_0,v_y_0,t,a))
	elif eleccion=="2":
		print("ingrese los siguentes datos nesesarios:x_0,v_x_0,t,a\n")
		x_0=int(input("x0"))
		v_x_0=int(input("vx0:"))
		t=int(input("t:"))
		a=float(input("a:"))
	elif eleccion=="3":
		print("ingrese los siguentes datos nesesarios:x_0.v_x_0,y_0,v_y_0,t,a\n")
		x_0=int(input("x0"))
		v_x_0=int(input("vx0:"))
		y_0=int(input("y0:"))
		v_y_0=int(input("vy0:"))
		t=int(input("t:"))
		a=float(input("a:"))
		print(obj_r_t(y_0,v_y_0,x_0,v_x_0,t,a))
	elif eleccion=="4":
		print("ingrese los siguentes datos nesesarios:v_0,t,a\n")
		v_0=int(input("v_0:"))
		t=int(input("t:"))
		a=float(input("a:"))
		print(velocidad_proyectil(v_0,t,a))
	elif eleccion=="5":
		print("ingrese los siguentes datos nesesarios:theta,v_0,t,a\n")
		theta=float(input("theta:"))
		v_0=int(input("v_0:"))
		t=int(input("t:"))
		a=float(input("a:"))
		print(velocidad(theta,v_0,t,a))
	elif eleccion=="6":
		print("ingrese los siguentes datos nesesarios:y_0,v_y_0,y_t,a\n")
		y_0=float(input("y_0:"))
		v_y_0=int(input("v_y_0:"))
		y_t=int(input("y_t:"))
		a=float(input("a:"))
		print(tiempo_de_caida(y_0,v_y_0,y_t,a))
	else:
		print("ingrese los siguentes datos nesesarios:v_0,theta_2,t,t1,a\n")
		v_0=int(input("v_0:"))
		theta_2=int(input("theta_2:"))
		t=int(input("t:"))
		t1=int(input("t1:"))
		a=float(input("a:"))
		print(colicion(v_0,theta_2,t,t1,a))


		


		


		


		

		

interfaz()
		







