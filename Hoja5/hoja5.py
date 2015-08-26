
#******************************************************************************************************************
# ------------------------------------------Hoja de trabajo numero 5----------------------------------------------
# Algoritmos y Estructura de datos
# Seccion 30
# Autores: Marlon Castillo 14427, Javier Lima 14373, Sebastian Castillo 14102
# 24/08/2015
#*******************************************************************************************************************

import math
import simpy
import random
lista = [] #almacena todos los tiempos de los procesos

# name: identificacion 
# Creart: simulacion de creacion de tiempo 
# ins: instrucciones 
# ins_x_ut: instrucciones por unidad de tiempo.

def proceso(env, Creart, name, RAM, memoria, ins, ins_x_ut):
    global sumatoria #almacena la sumatoria de (x-media)^2 para calcular la desviacion estandar
    global TiempoFinal #Tiempo final acumulado de los procesos.
    
#*****************************************NEW**********************************************
    # El proceso llega al sistema operativo, debe esperar asignaacion de memoria RAM (SIMULACION)
    yield env.timeout(Creart)
    T_Llegar = env.now # aqui llego el proceso (tiempo de llegada)
    
    #Si hay memoria pasa a estado Ready 
    yield RAM.get(memoria) #solicita memoria
