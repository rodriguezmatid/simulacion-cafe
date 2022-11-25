
#holis
import matplotlib as plt
import numpy as np

###### Asumo este costo por turno para cada uno de los recursos humanos.
costo_recepcionista = 2800
costo_chef = 5000
costo_barista = 1200
cantidad_de_chef = 2
cantidad_de_baristas = 2

ta_lun_9 = 0
consume_lun_9 = 0
ta_lun_12 = 0
consume_lun_12 = 0
ta_sab_10 = 0
consume_sab_10 = 0
ta_sab_12 = 0
consume_sab_12 = 0

ct_ta_lun_am = 0
ct_co_lun_am = 0
ct_ta_lun_pm = 0
ct_co_lun_pm = 0
ct_ta_sab_am = 0
ct_co_sab_am = 0
ct_ta_sab_pm = 0
ct_co_sab_pm = 0

with open('./lunes_9am.csv', 'r') as lunes_9am:
  for linea in lunes_9am:
    linea = linea.split(',')
    linea.pop(0)
    if linea[2] == 'TA' or linea[2] == 'TA\n':
      ta_lun_9 = ta_lun_9 + 1
      despacho_ta = np.random.uniform(15,20)
      consumo_ta = np.random.uniform(400,1800)
      linea.append(despacho_ta)
      linea.append(consumo_ta)
      ct_ta_lun_am = consumo_ta + ct_ta_lun_am


    elif linea[2] == 'Consume' or linea[2]=='Consume\n':
      consume_lun_9 = consume_lun_9 + 1
      despacho_co = np.random.uniform(45,60)
      consumo_co = np.random.uniform(300,2000)
      linea.append(despacho_co)
      linea.append(consumo_co)
      ct_co_lun_am = consumo_co + ct_co_lun_am
  arribos_totales_lun_am = ta_lun_9 + consume_lun_9

##CHEQUEAR PQ OBSERVACIONES SON SOLO POR 30'
with open('./lunes_12pm.csv', 'r') as lunes_12pm:
   for linea in lunes_12pm:
     linea = linea.split(',')
     linea.pop(0)
     #print(linea)
     if linea[2] == 'TA' or linea[2] == 'TA\n':
       ta_lun_12 = ta_lun_12 + 1
       despacho_ta = np.random.uniform(15,20)
       consumo_ta = np.random.uniform(400,1800)
       linea.append(consumo_ta)
       linea.append(despacho_ta)
       ct_ta_lun_pm = consumo_ta + ct_ta_lun_pm
     elif linea[2] == 'Consume' or linea[2]=='Consume\n':
       consume_lun_12 = consume_lun_12 + 1
       despacho_co = np.random.uniform(60,120)
       consumo_co = np.random.uniform(1800,4500)
       linea.append(consumo_co)
       linea.append(despacho_co)
       ct_co_lun_pm = consumo_co + ct_co_lun_pm
   arribos_totales_lun_pm = ta_lun_12 + consume_lun_12

with open('./sab_10am.csv', 'r') as sab_10am:
   for linea in sab_10am:
     linea = linea.split(',')
     linea.pop(0)
     #print(linea)
     if linea[2] == 'TA' or linea[2] == 'TA\n':
       ta_sab_10 = ta_sab_10 + 1
       despacho_ta = np.random.uniform(15,20)
       linea.append(despacho_ta)
       consumo_ta = np.random.uniform(400,1800)
       linea.append(consumo_ta)
       ct_ta_sab_am = consumo_ta + ct_ta_sab_am
     elif linea[2] == 'Consume\n' or linea[2]=='Consume\n':
       consume_sab_10 = consume_sab_10 + 1
       despacho_co = np.random.uniform(45,60)
       linea.append(despacho_co)
       consumo_co = np.random.uniform(1800,4500)
       linea.append(consumo_co)
       ct_co_sab_am = consumo_ta + ct_co_sab_am
   arribos_totales_sab_am = ta_sab_10 + consume_sab_10

#OBSERVACIONES POR 40'
with open('./sab_12pm.csv', 'r') as sab_12pm:
   for linea in sab_12pm:
     linea = linea.split(',')
     linea.pop(0)
     if linea[2] == 'TA' or linea[2] == 'TA\n':
       ta_sab_12 = ta_sab_12 + 1
       despacho_ta = np.random.uniform(15,20)
       consumo_ta = np.random.uniform(400,1800)
       linea.append(consumo_ta)
       linea.append(despacho_ta)
       ct_ta_sab_pm = consumo_ta + ct_ta_sab_pm

     elif linea[2] == 'Consume\n' or linea[2]=='Consume\n':
       consume_sab_12 = consume_sab_12 + 1
       despacho_co = np.random.uniform(60,120)
       linea.append(despacho_co)
       consumo_co = np.random.uniform(1800,4500)
       linea.append(consumo_co)
       ct_co_sab_pm = consumo_ta + ct_co_sab_pm
       arribos_totales_sab_pm = ta_sab_12 + consume_sab_12

print('Takeaway Lunes 12pm, personas: ' + str(ta_lun_12*2)) #Multiplico x 2 porque son observaciones de 30'
print('Consumo Lunes 12pm, personas: ' + str(consume_lun_12*2))#Idem arriba
print('Takeaway Sabado 10 Am, personas: ' + str(ta_sab_10))
print('Consumo Sabado 10 Am, personas: ' + str(consume_sab_10))
print('Takeaway Lunes 9 Am, personas: ' + str(ta_lun_9))
print('Consumo Lunes 9 Am, personas: ' + str(consume_lun_9))
print('Takeaway Sabado 12pm, personas: ' + str((ta_sab_12/40)*60))
print('Consumo Sabado 12pm, personas: ' + str((consume_sab_12/40)*60))

print('Lambda de Poisson sábado 10 am '+ str(arribos_totales_sab_am))
print('Lambda de Poisson sábado 12pm '+ str(arribos_totales_sab_pm))
print('Lambda de Poisson lunes 9 am '+ str(arribos_totales_lun_am))
print('Lambda de Poisson lunes 12pm '+ str(arribos_totales_lun_pm))

#Sumo consumos por dias y por turno
ct_lunes = ct_co_lun_am + ct_ta_lun_am + ct_co_lun_pm + ct_ta_lun_pm
ct_sabado = ct_co_sab_am + ct_ta_sab_am + ct_co_sab_pm + ct_ta_sab_pm
ct_am =  ct_co_lun_am + ct_ta_lun_am +  ct_co_sab_am + ct_ta_sab_am
ct_pm = ct_co_lun_pm + ct_ta_lun_pm + ct_co_sab_pm + ct_ta_sab_pm

arribos_totales_sabado = arribos_totales_sab_am + arribos_totales_sab_pm
arribos_totales_lunes = arribos_totales_lun_am + arribos_totales_lun_pm

ticket_promedio_sabado = ct_sabado / arribos_totales_sabado
ticket_promedio_lunes = ct_lunes / arribos_totales_lunes

#sumarizo el total
consumos_totales = ct_co_lun_am + ct_ta_lun_am + ct_co_lun_pm + ct_ta_lun_pm + ct_co_sab_am + ct_ta_sab_am + ct_co_sab_pm + ct_ta_sab_pm

#Sumo los costos por turno
costos_totales_am = costo_recepcionista + costo_chef + costo_barista * cantidad_de_baristas
costos_totales_pm = costo_recepcionista + costo_chef * cantidad_de_chef + costo_barista * cantidad_de_baristas

#Sumo los costos por dia
costo_diario = costos_totales_am + costos_totales_pm

#utilidades
#Multiplico el costo diario por dos, ya que tengo los  datos de consumo de dos dias, y el costo_diario solo considera uno.
utilidad_total = consumos_totales - costo_diario * 2
utilidad_sabado = ct_sabado - costo_diario
utilidad_lunes  = ct_lunes - costo_diario
utilidad_am = ct_am - costos_totales_am
utilidad_pm = ct_pm - costos_totales_pm

ganancia_promedio_am = utilidad_am/(arribos_totales_lun_am + arribos_totales_sab_am)
ganancia_promedio_pm = utilidad_pm/(arribos_totales_lun_pm + arribos_totales_sab_pm)
ganancia_promedio_sab = utilidad_sabado/(arribos_totales_sab_am + arribos_totales_sab_pm)
ganancia_promedio_lun = utilidad_lunes/(arribos_totales_lun_am + arribos_totales_lun_pm)

print("ganancia_promedio_am",ganancia_promedio_am)
print("ganancia_promedio_pm",ganancia_promedio_pm)
print("ganancia_promedio_sab",ganancia_promedio_sab)
print("ganancia_promedio_lun",ganancia_promedio_lun)
print("utilidad total: $",utilidad_total)

"""# Sábado

Baja demanda
"""

## SIMULACIÓN TIEMPO ENTRE ARRIBOS TOTALES PARA SABADO

## BAJA DEMANDA
experimentos = 100
arribos = 20
param_arribos = arribos_totales_sab_am #Sale del print anterior que muestra arribos en 1 hora del sabado Am
samples = np.zeros((arribos, experimentos))

for j in range(0, experimentos):
  for i in range(0, arribos):
    samples[i, j] = np.random.exponential(1/param_arribos)

mean_sab_baja = np.mean(samples)
std_sab_baja = np.std(samples)

print('Promedio: ' + str(mean_sab_baja))
print('Desvío estandar: ' + str(std_sab_baja))
print(np.sum(samples>0.25)/experimentos) # Proba de que haya mas de 0.25 de espera

plt.title('tiempo entre arribos exp 0')
plt.bar(np.arange(len(samples[0])),samples[0])
plt.show()

plt.title('tiempo entre arribos exp 1')
plt.bar(np.arange(len(samples[0])),samples[1])
plt.show()

plt.title('tiempo entre arribos exp 2')
plt.bar(np.arange(len(samples[0])),samples[2])
plt.show()

plt.title('tiempo entre arribos exp 3')
plt.bar(np.arange(len(samples[0])),samples[3])
plt.show()

plt.plot(np.cumsum(samples[:,0]))
plt.plot(np.cumsum(samples[:,1]))
plt.plot(np.cumsum(samples[:,2]))
plt.plot(np.cumsum(samples[:,3]))
plt.plot(np.cumsum(samples[:,4]))
plt.show()

## ACUMULACIÓN DE GENTE EN FILA
nSim = 100 #horas?
cum_fila = np.zeros(nSim)
param_arribos = arribos_totales_sab_am
param_despachos = 0
co_o_ta = 0 #Variable para ver si es consumo o takeaway
gente_total_despachada = 0

## 0 = TAKEAWAY
## 1 = CONSUMO

for i in range(1, nSim):
  co_o_ta = np.random.choice(2, p = [0.7, 0.3]) #Random entre 0 y 1
  gente_arriba = np.random.poisson(param_arribos)
  if co_o_ta == 0:
    gente_despacha = np.random.uniform(15,20)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  elif co_o_ta == 1:
    gente_despacha = np.random.uniform(45,60)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  gente_total_despachada = gente_total_despachada + 1

# probabilidad de que el sistema se sature el sabado 10 am
# lambda será en este caso arribos por hora, y Mu servicio por hora (cantidad de gente atendida)
tasa_de_saturacion = (arribos_totales_sabado/10)/gente_total_despachada

#print(cum_fila)
print('Promedio de gente acumulada ' + str(np.mean(cum_fila)))
print('Desviación estándar de gente acumulada ' + str(np.std(cum_fila)))
plt.plot(cum_fila, marker = 'o')
plt.xlabel('Experimentos')
plt.ylabel('Acumulación de personas')
plt.show()

# next steps
# calcular metricas de la fila como cantidad promedio de gente esperando o la probabilidad de que x = 0 , x = 1 ..... es decir armar el vector de proba de estado
# si el costo de tener esperando a una persona es $ precio promedio de compra, determinar el costo de oportunidad por gente no despachada que espera
# hacer un escenario hipotetico que el lambda aumenta de arribos, el lambda de arribos disminuye, calcular el precio por hora de mantener a un empleado atendiendo y ver cual es el minimo lambda que deberias tener para qqiue tu ROI no sea negativo

# calcular el precio por hora de mantener a un empleado atendiendo
hora_atencion = costo_diario/10

# para calcular mi ROI debo despejar lambda. El ticket promedio * lambda - costos >= 0
lambda_estimado_lunes = costo_diario/ticket_promedio_lunes
lambda_estimado_sabado = costo_diario/ticket_promedio_sabado

"""Alta demanda"""

## SIMULACIÓN TIEMPO ENTRE ARRIBOS TOTALES PARA SABADO

## ALTA DEMANDA
import numpy as np
import matplotlib.pyplot as plt

experimentos = 100
arribos = 40
param = 45 #Sale del print anterior que muestra arribos en 1 hora
samples = np.zeros((arribos, experimentos))

for j in range(0, experimentos):
  for i in range(0, arribos):
    samples[i, j] = np.random.exponential(1/param)

mean_sab_alta = np.mean(samples)
std_sab_alta = np.std(samples)

print('Promedio: ' + str(mean_sab_alta))
print('Desvío estandar: ' + str(std_sab_alta))

plt.plot(np.cumsum(samples[:,0]))
plt.plot(np.cumsum(samples[:,1]))
plt.plot(np.cumsum(samples[:,2]))
plt.plot(np.cumsum(samples[:,3]))
plt.plot(np.cumsum(samples[:,4]))

import matplotlib.pyplot as plt
plt.plot(np.cumsum(samples[:,0]))
plt.plot(np.cumsum(samples[:,1]))
plt.plot(np.cumsum(samples[:,2]))
plt.plot(np.cumsum(samples[:,3]))
plt.plot(np.cumsum(samples[:,4]))

## ACUMULACIÓN DE GENTE EN FILA
nSim = 100 #horas?
cum_fila = np.zeros(nSim)
param_arribos = 45
param_despachos = 0
co_o_ta = 0 #Variable para ver si es consumo o takeaway

## 0 = TAKEAWAY
## 1 = CONSUMO

for i in range(1, nSim):
  co_o_ta = np.random.choice(2, p = [0.7, 0.3]) #Random entre 0 y 1
  gente_arriba = np.random.poisson(param_arribos)
  if co_o_ta == 0:
    gente_despacha = np.random.uniform(15,20)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  elif co_o_ta == 1:
    gente_despacha = np.random.uniform(45,60)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0

#print(cum_fila)
print('Promedio de gente acumulada ' + str(np.mean(cum_fila)))
print('Desviación estándar de gente acumulada ' + str(np.std(cum_fila)))
plt.plot(cum_fila, marker = 'o')
plt.title('Acumulación en la fila si la probabilidad de TA > Consumo')
plt.xlabel('Experimentos')
plt.ylabel('Acumulación de personas')
plt.show()

#Análisis de sensibilidad

## CAMBIA PROBA DE TA O CONSUMO

## 1
nSim = 100
cum_fila = np.zeros(nSim)
param_arribos = 45
param_despachos = 0
co_o_ta = 0

for i in range(1, nSim):
  co_o_ta = np.random.choice(2, p = [0.5, 0.5]) #Misma proba
  gente_arriba = np.random.poisson(param_arribos)
  if co_o_ta == 0:
    gente_despacha = np.random.uniform(15,20)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  elif co_o_ta == 1:
    gente_despacha = np.random.uniform(45,60)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0

#print(cum_fila)
print('Promedio de gente acumulada ' + str(np.mean(cum_fila)))
print('Desviación estándar de gente acumulada ' + str(np.std(cum_fila)))
plt.plot(cum_fila, marker = 'o')
plt.title('Acumulación en la fila si la probabilidad de TA y Consumo es igual')
plt.xlabel('Experimentos')
plt.ylabel('Acumulación de personas')
plt.show()

## 2
nSim = 100
cum_fila = np.zeros(nSim)
param_arribos = 45
param_despachos = 0
co_o_ta = 0

for i in range(1, nSim):
  co_o_ta = np.random.choice(2, p = [0.3, 0.7]) #Distinta proba
  gente_arriba = np.random.poisson(param_arribos)
  if co_o_ta == 0:
    gente_despacha = np.random.uniform(15,20)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  elif co_o_ta == 1:
    gente_despacha = np.random.uniform(45,60)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0

#print(cum_fila)
print('Promedio de gente acumulada ' + str(np.mean(cum_fila)))
print('Desviación estándar de gente acumulada ' + str(np.std(cum_fila)))
plt.plot(cum_fila, marker = 'o')
plt.title('Acumulación en la fila si la probabilidad de TA < Consumo')
plt.xlabel('Experimentos')
plt.ylabel('Acumulación de personas')
plt.show()

#Análisis de sensibilidad

## CAMBIA LAMBDA DE ARRIBOS

## 0 - SE MANTIENE
nSim = 100
cum_fila = np.zeros(nSim)
param_arribos = 45
param_despachos = 0
co_o_ta = 0

for i in range(1, nSim):
  co_o_ta = np.random.choice(2, p = [0.5, 0.5]) #Misma proba
  gente_arriba = np.random.poisson(param_arribos)
  if co_o_ta == 0:
    gente_despacha = np.random.uniform(15,20)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  elif co_o_ta == 1:
    gente_despacha = np.random.uniform(45,60)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0

#print(cum_fila)
print('Promedio de gente acumulada ' + str(np.mean(cum_fila)))
print('Desviación estándar de gente acumulada ' + str(np.std(cum_fila)))
plt.plot(cum_fila, marker = 'o')
plt.title('Acumulación en la fila si lambda se mantiene')
plt.xlabel('Experimentos')
plt.ylabel('Acumulación de personas')
plt.show()

## 1 - DISMINUYE
nSim = 100
cum_fila = np.zeros(nSim)
param_arribos = 20
param_despachos = 0
co_o_ta = 0

for i in range(1, nSim):
  co_o_ta = np.random.choice(2, p = [0.5, 0.5]) #Misma proba
  gente_arriba = np.random.poisson(param_arribos)
  if co_o_ta == 0:
    gente_despacha = np.random.uniform(15,20)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  elif co_o_ta == 1:
    gente_despacha = np.random.uniform(45,60)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0

#print(cum_fila)
print('Promedio de gente acumulada ' + str(np.mean(cum_fila)))
print('Desviación estándar de gente acumulada ' + str(np.std(cum_fila)))
plt.plot(cum_fila, marker = 'o')
plt.title('Acumulación en la fila si lambda disminuye')
plt.xlabel('Experimentos')
plt.ylabel('Acumulación de personas')
plt.show()

## 2 - AUMENTA
nSim = 100
cum_fila = np.zeros(nSim)
param_arribos = 80
param_despachos = 0
co_o_ta = 0

for i in range(1, nSim):
  co_o_ta = np.random.choice(2, p = [0.5, 0.5]) #Distinta proba
  gente_arriba = np.random.poisson(param_arribos)
  if co_o_ta == 0:
    gente_despacha = np.random.uniform(15,20)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  elif co_o_ta == 1:
    gente_despacha = np.random.uniform(45,60)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0

#print(cum_fila)
print('Promedio de gente acumulada ' + str(np.mean(cum_fila)))
print('Desviación estándar de gente acumulada ' + str(np.std(cum_fila)))
plt.plot(cum_fila, marker = 'o')
plt.title('Acumulación en la fila si lambda aumenta')
plt.xlabel('Experimentos')
plt.ylabel('Acumulación de personas')
plt.show()

"""# Lunes

Baja demanda
"""

## SIMULACIÓN TIEMPO ENTRE ARRIBOS TOTALES PARA LUNES

## BAJA DEMANDA
import numpy as np
import matplotlib.pyplot as plt

experimentos = 100
arribos = 20
param = 18 #Sale del print anterior que muestra arribos en 1 hora
samples = np.zeros((arribos, experimentos))

for j in range(0, experimentos):
  for i in range(0, arribos):
    samples[i, j] = np.random.exponential(1/param)

mean_lun_baja = np.mean(samples)
std_lun_baja = np.std(samples)

print('Promedio: ' + str(mean_lun_baja))
print('Desvío estandar: ' + str(std_lun_baja))

plt.plot(samples[0])
plt.plot(samples[1])
plt.plot(samples[2])
plt.show()

## ACUMULACIÓN DE GENTE EN FILA
nSim = 100 #horas?
cum_fila = np.zeros(nSim)
param_arribos = 18
param_despachos = 0
co_o_ta = 0 #Variable para ver si es consumo o takeaway

## 0 = TAKEAWAY
## 1 = CONSUMO

for i in range(1, nSim):
  co_o_ta = np.random.choice(2, p = [0.7, 0.3]) #Random entre 0 y 1
  gente_arriba = np.random.poisson(param_arribos)
  if co_o_ta == 0:
    gente_despacha = np.random.uniform(15,20)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  elif co_o_ta == 1:
    gente_despacha = np.random.uniform(45,60)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0

#print(cum_fila)
print('Promedio de gente acumulada ' + str(np.mean(cum_fila)))
print('Desviación estándar de gente acumulada ' + str(np.std(cum_fila)))
plt.plot(cum_fila, marker = 'o')
plt.xlabel('Experimentos')
plt.ylabel('Acumulación de personas')
plt.show()

"""Alta demanda"""

## SIMULACIÓN TIEMPO ENTRE ARRIBOS TOTALES PARA LUNES

## ALTA DEMANDA
import numpy as np
import matplotlib.pyplot as plt

experimentos = 100
arribos = 40
param = 56 #Sale del print anterior que muestra arribos en 1 hora
samples = np.zeros((arribos, experimentos))

for j in range(0, experimentos):
  for i in range(0, arribos):
    samples[i, j] = np.random.exponential(1/param)

mean_lun_alta = np.mean(samples)
std_lun_alta = np.std(samples)

print('Promedio: ' + str(mean_lun_alta))
print('Desvío estandar: ' + str(std_lun_alta))

plt.plot(samples[0])
plt.plot(samples[1])
plt.plot(samples[2])
plt.show()

## ACUMULACIÓN DE GENTE EN FILA
nSim = 100 #horas?
cum_fila = np.zeros(nSim)
param_arribos = 56
param_despachos = 0
co_o_ta = 0 #Variable para ver si es consumo o takeaway

## 0 = TAKEAWAY
## 1 = CONSUMO

for i in range(1, nSim):
  co_o_ta = np.random.choice(2, p = [0.7, 0.3]) #Random entre 0 y 1
  gente_arriba = np.random.poisson(param_arribos)
  if co_o_ta == 0:
    gente_despacha = np.random.uniform(15,20)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0
  elif co_o_ta == 1:
    gente_despacha = np.random.uniform(45,60)
    cum_fila[i] = gente_arriba - gente_despacha
    if cum_fila[i]<0:
      cum_fila[i]=0

#print(cum_fila)
print('Promedio de gente acumulada ' + str(np.mean(cum_fila)))
print('Desviación estándar de gente acumulada ' + str(np.std(cum_fila)))
plt.plot(cum_fila, marker = 'o')
plt.xlabel('Experimentos')
plt.ylabel('Acumulación de personas')
plt.show()