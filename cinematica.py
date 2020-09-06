import matplotlib as plt
import numpy as np

#crearemos las funciones para nuestros objetos fundamentales

#para nuestro primer objeto fundamental altura "y(t)":

def obj_y_t(y_0,v_y_0,t,a):
	y_t=y_0+v_y_0+a*(t**2)/2
	return y_t


def obj_x_t(x_0,v_x_0,t):
	x_t=x_0+v_x_0
	return x_t


def obj_r_t(x_t,y_t):
	r_t=[]
	r_t.append(x_t)
	r_t.append(y_t)
	return r_t


print(obj_r_t(2,3))	


