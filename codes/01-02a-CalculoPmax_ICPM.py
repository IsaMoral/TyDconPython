import math
import cmath

#Script para calcular el Potencia Maxima a Contratar e intencidad por el ICPM
#Datos de la Acometida
#Potencia Aparente Maxima[VA]
W=40000
#Factor de Potencia
fp=0.75
#Frecuencia[Hertz]
frec=50

P_max=W*fp

print("\n")
print("Tension minima del ICPM")
print(220*(1-0.005))

print("\n")
print("Potencia Maxima a contratar")
print(P_max)

I_ICPM=P_max/(220*(1-0.005))

print("\n")
print("Intenciad minima del ICPM")
print(I_ICPM)


