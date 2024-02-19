import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

#Sea una distribución trifásica que dispone de 5 receptores dispuestos
# según la figura. Calcular la sección necesaria, conociendo que el 
#conductor instalado es de aluminio, y la caída de tensión compuesta
# máxima sea 12 V. Calcular también la intensidad en el CT,
# así como la potencia activa, reactiva y aparente.
# Sabiendo que la instalación es trifásica y la tensión es de 400 V.
# (factor de impedancia K=1,12)

#pagina 208
V=400
K=1.12
DeltaV=12
rho=0.028
print('Tension = V: {:.2f}'.format(V))
print('\n')

P=[1,1,1,1,1]
I=[1,1,1,1,1]
cos=[1,1,1,1,1]

cos[0]=0.65
P[0]=15*1000*cos[0];
I[0]=P[0]/V/math.sqrt(3)/cos[0]
print('Potencia 1 = P_1: {:.2f}'.format(P[0]))

cos[1]=0.85
P[1]=math.sqrt(3)*400*20*cos[1]
I[1]=P[1]/V/math.sqrt(3)/cos[1]
print('Potencia 2 = P_2: {:.2f}'.format(P[1]))

cos[2]=0.75
P[2]=12*1000
phi=math.acos(cos[2])
S_20=P[2]/cos[2]
print('Q 3 Inicial = S_30: {:.2f}'.format(S_20))
print('Sen 3 Inicial = sin_30: {:.2f}'.format(math.sin(phi)))
W_R=S_20*math.sin(phi)-math.sqrt(3)*V**2*50e-6*2*math.pi*50
print('Potencia Reac = Q_3: {:.2f}'.format(W_R))
S_2=math.sqrt(P[2]**2+W_R**2)
I[2]=abs(S_2)/V/math.sqrt(3)
cos[2]=P[2]/abs(S_2)
print('COS phi 3 = P/|S| = : {:.2f}'.format(cos[2]))
print('Potencia 3 = P_3: {:.2f}'.format(P[2]))

print('\n')
Z=10+1j*2*math.pi*50*5e-3
print('Z = R +j XL =  : {:.2f}'.format(Z))
I_4=V/Z
print('I=V/Z =: {:.2f}'.format(I_4))
S=math.sqrt(3)*V*I_4.conjugate()
print('S = sqrt(3)*V*I.conjugate(): {:.2f}'.format(S))
P[3]=S.real
cos[3]=P[3]/abs(S)
I[3]=P[3]/V/math.sqrt(3)/cos[3]
print('COS phi 4 = P/|S| = : {:.2f}'.format(cos[3]))
print('\n')
print('Potencia 4 = P_4: {:.2f}'.format(P[3]))


cos[4]=0.95
P[4]=math.sqrt(3)*400*30*cos[4]
I[4]=P[4]/V/math.sqrt(3)/cos[4]
print('Potencia 5 = P_5: {:.2f}'.format(P[4]))

#Longitudes[m]          
L=[20,30,60,75,95] 
#Linea de Fuga [mm]

print(I)
print(cos)

#La caida de tension sera
aux=[1,1,1,1,1]
for i in range(0, 5):
    aux[i]=L[i]*I[i]*cos[i] # prints: -1, 0, 1, 2, 3, 4, 
print(aux)
sumatoria=sum(aux)
print('Sumatoria = : {:.2f}'.format(sumatoria))
S_min=math.sqrt(3)*rho/DeltaV*sumatoria

print('Seccion Minima = S: {:.2f}'.format(S_min))

S_c=35
print('Seccion Comercial = S: {:.2f}'.format(S_c))
D_V_final=math.sqrt(3)*rho/S_c*sumatoria
print('Caida Con Seccion Comercia = S: {:.2f}'.format(D_V_final))

#Tension compuesta Mas elevada [kV]


# print('DATOS:')
# print('Grado de Aislamiento     GA: %.2f        [cm/kV]' % GA)
# print('Linea de Fuga            LF: %.2f        [mm]' % LF)
# print('Tension                  E : %.2f        [kV]' % E)
# print("\n")


# print('RESULTADOS:')
# print('n = GA   E')
# print('    -------')
# print('       LF')
# print('Numero de Aisladores     n : %.2f' % n)