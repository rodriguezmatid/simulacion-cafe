
#holis
import matplotlib as plt
import numpy as np

###### Asumo este costo por turno para cada uno de los recursos humanos.
costo_recepcionista = 2800
costo_chef = 5000
costo_barista = 1200

with open('./lunes_9am.csv', 'r') as lunes_9am:
  ta_lun_9 = 0
  consume_lun_9 = 0
  ct_ta_lun_am = 0
  ct_co_lun_am = 0
  ct_ta_lun_pm = 0
  ct_co_lun_pm = 0
  ct_ta_sab_am = 0
  ct_co_sab_am = 0
  ct_ta_sab_pm = 0
  ct_co_sab_pm = 0

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


with open('./lunes_12pm.csv', 'r') as lunes_12pm:
   ta_lun_12 = 0
   consume_lun_12 = 0
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
   ta_sab_10 = 0
   consume_sab_10 = 0
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

with open('./sab_12pm.csv', 'r') as sab_12pm:
   ta_sab_12 = 0
   consume_sab_12 = 0
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


print('Takeaway Lunes 12pm, personas: ' + str(ta_lun_12))
print('Consumo Lunes 12pm, personas: ' + str(consume_lun_12))
print('Takeaway Sabado 10 Am, personas: ' + str(ta_sab_10))
print('Consumo Sabado 10 Am, personas: ' + str(consume_sab_10))
print('Takeaway Lunes 9 Am, personas: ' + str(ta_lun_9))
print('Consumo Lunes 9 Am, personas: ' + str(consume_lun_9))
print('Takeaway Sabado 12pm, personas: ' + str(ta_sab_12))
print('Consumo Sabado 12pm, personas: ' + str(consume_sab_12))
#Sumo consumos por dias y por turno
ct_lunes = ct_co_lun_am + ct_ta_lun_am + ct_co_lun_pm + ct_ta_lun_pm
ct_sabado = ct_co_sab_am + ct_ta_sab_am + ct_co_sab_pm + ct_ta_sab_pm
ct_am =  ct_co_lun_am + ct_ta_lun_am +  ct_co_sab_am + ct_ta_sab_am
ct_pm = ct_co_lun_pm + ct_ta_lun_pm + ct_co_sab_pm + ct_ta_sab_pm
#sumarizo el total
consumos_totales = ct_co_lun_am + ct_ta_lun_am + ct_co_lun_pm + ct_ta_lun_pm + ct_co_sab_am + ct_ta_sab_am + ct_co_sab_pm + ct_ta_sab_pm
#Sumo los costos por turno
costos_totales_am = costo_recepcionista + costo_chef + costo_barista * 2
costos_totales_pm = costo_recepcionista + costo_chef * 2 + costo_barista * 2

#Sumo los costos por dia
costo_diario = costos_totales_am + costos_totales_pm

#utilidades
#Multiplico el costo diario por dos, ya que tengo los  datos de consumo de dos dias, y el costo_diario solo considera uno.
utilidad_total = consumos_totales - costo_diario*2
utilidad_sabado = ct_sabado - costo_diario
utilidad_lunes  = ct_lunes - costo_diario
utilidad_am = ct_am -costos_totales_am
utilidad_pm = ct_pm -costos_totales_pm

ganancia_promedio_am = utilidad_am/(arribos_totales_lun_am + arribos_totales_sab_am)
ganancia_promedio_pm = utilidad_pm/(arribos_totales_lun_pm + arribos_totales_sab_pm)
ganancia_promedio_sab = utilidad_sabado/(arribos_totales_sab_am + arribos_totales_sab_pm)
ganancia_promedio_lun = utilidad_lunes/(arribos_totales_lun_am + arribos_totales_lun_pm)

print("ganancia_promedio_am",ganancia_promedio_am)
print("ganancia_promedio_pm",ganancia_promedio_pm)
print("ganancia_promedio_sab",ganancia_promedio_sab)
print("ganancia_promedio_lun",ganancia_promedio_lun)
print("utilidad total: $",utilidad_total)

"""# Sábado"""

## SIMULACIÓN TIEMPO ENTRE ARRIBOS TOTALES PARA SABADO

## BAJA DEMANDA
import numpy as np
import matplotlib.pyplot as plt

experimentos = 100
arribos = 20
param = 24 #Sale del print anterior que muestra arribos en 1 hora del sabado Am
samples = np.zeros((arribos, experimentos))

for j in range(0, experimentos):
  for i in range(0, arribos):
    samples[i, j] = np.random.exponential(1/param)

mean_sab_baja = np.mean(samples)
std_sab_baja = np.std(samples)

print('Promedio: ' + str(mean_sab_baja))
print('Desvío estandar: ' + str(std_sab_baja))

# plt.bar(samples,height)
plt.show()

## SIMULACIÓN TIEMPO ENTRE ARRIBOS TOTALES PARA SABADO

## ALTA DEMANDA
import numpy as np
import matplotlib.pyplot as plt

experimentos = 100
arribos = 40
param = 30 #Sale del print anterior que muestra arribos en 1 hora
samples = np.zeros((arribos, experimentos))

for j in range(0, experimentos):
  for i in range(0, arribos):
    samples[i, j] = np.random.exponential(1/param)

mean_sab_alta = np.mean(samples)
std_sab_alta = np.std(samples)

print('Promedio: ' + str(mean_sab_alta))
print('Desvío estandar: ' + str(std_sab_alta))
"""
plt.bar(samples, height=1)
plt.show()"""

samples

import matplotlib.pyplot as plt
plt.plot(np.cumsum(samples[:,0]))
plt.plot(np.cumsum(samples[:,1]))
plt.plot(np.cumsum(samples[:,2]))
plt.plot(np.cumsum(samples[:,3]))
plt.plot(np.cumsum(samples[:,4]))

"""# Lunes

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
"""
plt.bar(samples, height=1)
plt.show()"""

## SIMULACIÓN TIEMPO ENTRE ARRIBOS TOTALES PARA LUNES

## ALTA DEMANDA
import numpy as np
import matplotlib.pyplot as plt

experimentos = 100
arribos = 20
param = 24  #Sale del print anterior que muestra arribos en 1 hora
samples = np.zeros((arribos, experimentos))

for j in range(0, experimentos):
  for i in range(0, arribos):
    samples[i, j] = np.random.exponential(1/param)

mean_lun_alta = np.mean(samples)
std_lun_alta = np.std(samples)

print('Promedio: ' + str(mean_lun_alta))
print('Desvío estandar: ' + str(std_lun_alta))
"""
plt.bar(samples, height=1)
plt.show()"""