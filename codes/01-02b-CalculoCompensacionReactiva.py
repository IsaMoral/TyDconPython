import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

#Script para calcular la Compensancion del factor de potencia

#Datos de la Acometida
#Potencia Aparente Maxima[VA]
W=40000
#Factor de Potencia
fp=0.75
#Factor de Potencia Nuevo
fp_c=0.9
#Frecuencia[Hertz]
frec=50
#Tension
V=220

#Calculo Corriente
phi=math.acos(fp)
U_1=V+0j
I_1=W/math.sqrt(3)/U_1*cmath.rect(1,-phi)
W_1=math.sqrt(3)*U_1*I_1.conjugate()

print("\n")
print("DATOS")
print('Potencia Aparente    W_o: %.2f  < %.2f     [kW]' % (abs(W_1)/1000,cmath.phase(W_1)*180/math.pi))
print('Potencia Aparente    W_o: {:.2f}       [kW]'.format(W_1/1000))
print('Tension              V_o: {:.2f}       [V]'.format(U_1))
print("\n")
print("RESULTADOS")
print('Corriente            I_o: {:.2f}       [A]'.format(I_1))
phi_2=math.acos(fp_c)
Wap1=W_1.real*(1+1j*math.sin(phi_2))
print('Potencia Esperada    W: %.2f  < %.2f     [kW]' % (abs(Wap1)/1000,cmath.phase(Wap1)*180/math.pi))
print('Potencia Esperada    W: {:.2f}           [kW]'.format(Wap1/1000))
print('Potencia Esperada    fp: {:.2f}'.format(math.cos(cmath.phase(Wap1))))

#Calculo Capacitor
W_rc=abs(W_1.imag-Wap1.imag)
C_T=W_rc/(3*abs(U_1)**2*2*math.pi*frec)
print('Potencia Capacitor   W: {:.2f}       [kW]'.format(W_rc/1000))
print('Capacitor Teorico    W: {:.2f}       [uF]'.format(C_T*1e6))

W_2=Wap1

plt.plot([0,W_2.real],[0,W_2.imag],marker='o')
plt.plot([0,W_1.real],[0,W_1.imag],marker='o')
plt.plot([W_1.real,W_2.real],[W_1.imag,W_2.imag],marker='o')
plt.legend(('W Original','W Final','W Capacitor'),loc='upper left')
plt.title('Triangulos de Potencias')
plt.show()
