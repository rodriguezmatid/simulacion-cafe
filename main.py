import matplotlib as plt
import numpy as np

###### Assumptions
costo_recepcionista = 3200
costo_chef = 5500
costo_barista = 1200
turno_temprano = 3 # cantidad de hs
turno_tarde = 7 # cantidad de hs

with open('./lunes_9am.csv', 'r') as lunes_9am:
  ta_lun_9 = 0
  consume_lun_9 = 0
  ct_ta_lun_am = 0
  ct_co_lun_am = 0
  for linea in lunes_9am:
    linea = linea.split(',')
    #print(linea)
    linea.pop(0)
    if linea[2] == 'TA' or linea[2] == 'TA\n':
      ta_lun_9 = ta_lun_9 + 1
      despacho_ta = np.random.uniform(15,20)
      consumo_ta = np.random.uniform(300,1600)
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


# with open('./lunes_12pm.csv', 'r') as lunes_12pm:
#   ta_lun_12 = 0
#   consume_lun_12 = 0
#   for linea in lunes_12pm:
#     linea = linea.split(',')
#     linea.pop(0)
#     #print(linea)
#     if linea[2] == 'TA' or linea[2] == 'TA\n':
#       ta_lun_12 = ta_lun_12 + 1
#       despacho_ta = np.random.uniform(15,20)
#       consumo_ta = np.random.uniform(300,1600)
#       linea.append(consumo_ta)
#       linea.append(despacho_ta)
#     elif linea[2] == 'Consume' or linea[2]=='Consume\n':
#       consume_lun_12 = consume_lun_12 + 1
#       despacho_co = np.random.uniform(60,120)
#       consumo_co = np.random.uniform(1500,3000)
#       linea.append(consumo_co)
#       linea.append(despacho_co)

#   arribos_totales_lun_pm = ta_lun_12 + consume_lun_12

# with open('./sab_10am.csv', 'r') as sab_10am:
#   ta_sab_10 = 0
#   consume_sab_10 = 0
#   for linea in sab_10am:
#     linea = linea.split(',')
#     linea.pop(0)
#     #print(linea)
#     if linea[2] == 'TA' or linea[2] == 'TA\n':
#       ta_sab_10 = ta_sab_10 + 1
#       despacho_ta = np.random.uniform(15,20)
#       linea.append(despacho_ta)
#       consumo_ta = np.random.uniform(300,1600)
#       linea.append(consumo_ta)
#       print(linea)
#     elif linea[2] == 'Consume\n' or linea[2]=='Consume\n':
#       consume_sab_10 = consume_sab_10 + 1
#       despacho_co = np.random.uniform(45,60)
#       linea.append(despacho_co)
#       consumo_co = np.random.uniform(1500,3000)
#       linea.append(consumo_co)

#   arribos_totales_sab_am = ta_sab_10 + consume_sab_10

# with open('./sab_12pm.csv', 'r') as sab_12pm:
#   ta_sab_12 = 0
#   consume_sab_12 = 0
#   for linea in sab_12pm:
#     linea = linea.split(',')
#     linea.pop(0)
#     #print(linea)
#     if linea[2] == 'TA' or linea[2] == 'TA\n':
#       ta_sab_12 = ta_sab_12 + 1
#       despacho_ta = np.random.uniform(15,20)
#       consumo_ta = np.random.uniform(300,1600)
#       linea.append(consumo_ta)
#       linea.append(despacho_ta)
#     elif linea[2] == 'Consume\n' or linea[2]=='Consume\n':
#       consume_sab_12 = consume_sab_12 + 1
#       despacho_co = np.random.uniform(60,120)
#       linea.append(despacho_co)
#       consumo_co = np.random.uniform(1500,3000)
#       linea.append(consumo_co)
#       arribos_totales_sab_pm = ta_sab_12 + consume_sab_12


# print('Takeaway Lunes 12pm, personas: ' + str(ta_lun_12))
# print('Consumo Lunes 12pm, personas: ' + str(consume_lun_12))
# print('Takeaway Sabado 10 Am, personas: ' + str(ta_sab_10))
# print('Consumo Sabado 10 Am, personas: ' + str(consume_sab_10))
print('Takeaway Lunes 9 Am, personas: ' + str(ta_lun_9))
print('Consumo Lunes 9 Am, personas: ' + str(consume_lun_9))
print('Ingreso Lunes 9 ta, $: ' + str(ct_ta_lun_am))
print('Ingreso Lunes 9 co, $: ' + str(ct_co_lun_am))
utilidad = ct_co_lun_am + ct_ta_lun_am - costo_recepcionista - costo_chef - costo_barista * 2
print(utilidad)
ganancia_promedio = utilidad / (ta_lun_9 + consume_lun_9)
print(ganancia_promedio)

# crecimiento x hs
lun_9 = ta_lun_9 + consume_lun_9
lun_10 = lun_9 * 1.10
lun_11 = lun_10 * 1.20

#   print('Takeaway Sabado 12pm, personas: ' + str(ta_sab_12))
#   print('Consumo Sabado 12pm, personas: ' + str(consume_sab_12))