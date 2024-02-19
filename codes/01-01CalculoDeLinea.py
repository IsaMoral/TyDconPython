import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

#Script para calcular el rendimiento de una linea trifasica a partir de sus caracteristicas
#Datos de la Linea
#longitud [km]
l=227
#Tnesion Compuesta 2 [V]
V=110000
#Corriente Compuesta 2[A]
I=100
#Factor de Potencia
fp=0.85
#Frecuencia[Hertz]
frec=50

#Caracteristicas de la linea por unidad de Km
#Resistividad[Ohm/km]
R_k=0.245
#Inductancia[H/km]
L_k=1.48e-3
#Capacitancia[F/km]
C_k=9e-9
#Conductancia[S/km]
G_k=5e-7

#Tension Simple (Salida) a partir de la tension compuesta
E_2=V
U_2=E_2/math.sqrt(3)
print("Tension Simple (Salida) a partir de la tension compuesta")
print("U_2 = %.2f" % (U_2))

#Impedancia y Admitancia de la linea
Z=R_k*l+2j*math.pi*frec*L_k*l
print("Impedancia de la linea Z [Ohm]")
print(Z)

A=G_k*l+2j*math.pi*frec*C_k*l
print("Admitancia de la linea A [S]")
print(A)

#Factores Comunes Parametros ecuacion
AUX1=1+Z*A/2
print("1 + Z A/ 2")
print('AUX1: {:.4f}'.format(AUX1))
print(cmath.polar(AUX1))
print(cmath.phase(AUX1)*180/math.pi)

AUX2=1+Z*A/6
print("1 + Z A/ 6")
print('AUX2: {:.4f}'.format(AUX2))
print(abs(AUX2))
print(cmath.phase(AUX2)*180/math.pi)

#Corriente Factorial con U_2 de referencia
print("\n")
print("Corriente de Salida de la Linea")
I_2=I*fp-1j*I*math.sqrt(1-fp**2)
print(abs(I_2))
print(cmath.phase(I_2)*180/math.pi)

#Tension e Intensidad del principio de la Linea
U_1=U_2*AUX1+I_2*Z*AUX2
I_1=I_2*AUX1+U_2*A*AUX2

print("\n")
print("Tension de Entrada de la Linea")
print(abs(U_1))
print(cmath.phase(U_1)*180/math.pi)

print("\n")
print("Corriente de Entrada de la Linea")
print(abs(I_1))
print(cmath.phase(I_1)*180/math.pi)

plt.subplot(212)
plt.plot([0,I_2.real],[0,I_2.imag],marker='o', lw=2)
plt.plot([0,I_1.real],[0,I_1.imag],marker='o', lw=2)
plt.legend(('I_1','I_2'),loc='upper right')
plt.title('Corrientes [A]')
plt.grid(True)

plt.subplot(211)
plt.plot([0,U_2.real/1000],[0,U_2.imag/1000],marker='o', lw=2)
plt.plot([0,U_1.real/1000],[0,U_1.imag/1000],marker='o', lw=2)
plt.legend(('V_2','V_1'),loc='upper left')
plt.title("Tensiones [kV]")
plt.grid(True)
plt.tight_layout()
plt.show()

#RENDIMIENTO
W_1=3*U_1*I_1.conjugate()
W_2=3*U_2*I_2.conjugate()
print("\n")
print("Potencia de Entrada de la Linea")
print(W_1)

print("\n")
print("Potencia de Salida de la Linea")
print(W_2)

eta=W_2.real/W_1.real

print("\n")
print("RENDIMIENTO de la Linea")
print(eta)
