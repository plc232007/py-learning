"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

RADAR_1 = 60 
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade = 61
local_carro = 101

if (LOCAL_1 - RADAR_RANGE < local_carro <= LOCAL_1 + RADAR_RANGE) and (velocidade > RADAR_1):
    print ("Velocidade acima do limite ao passar no radar.")
else:
    print ("Velocidade OK!")
    