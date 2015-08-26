
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

#*************************************READY**********************************************
    #Proceso listo, esperar atencion de CPU
    completado = 0
    while completado < ins:
        #Conectarnos con el CPU
        with CPU.request() as req:
            yield req
            #Determinar instrucciones a realizar
            if (ins-completado)>=3:
                eje=3
            else:
                eje=(ins-completado)
            #El tiempo de ejecucion es de 1/(instrucciones por unidad de tiempo) con "eje" instrucciones a realizar 
            yield env.timeout(eje/ins_x_ut)

#*************************************RUNNING**********************************************
            #Actualizar el contador de instrucciones a realizar 
            completado += eje
 
        #Cola: Numero aleatorio si es 1 pasa a  cola waiting y si es 2 pasa a cola ready)
        Cola = random.randint(1,2)

        #si random es 1 va a cola waiting
        if Cola == 1 and completado<ins:
        
#*************************************Waiting**********************************************   
            with waiting.request() as req2:
                yield req2
                #espera en cola de operaciones I/O
                yield env.timeout(1)                

    RAM.put(memoria)

    # Se agraga al tiempo Final = (tiempo actual - tiempo  llegada)
    lista.append (env.now - T_Llegar)
    TiempoFinal += (env.now - T_Llegar)
