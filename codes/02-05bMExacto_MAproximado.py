import math
import cmath

#Hallar la caída de tensión por el método exacto y por el aproximado
#en una línea monofásica de las siguientes características:(15%)

#tension salida de linea [V]
U2 = 220
#corriente de linea [A]
I = 15
#Factor de potencia
cos_2= 0.8
#Longitud [m]
L = 300
#Resistencia y Reluctancia por km [Ω / Km]
RK = 0.4 
XK = 0.2

print('DATOS:')
print('Tension Salida = V: {:.2f} [V]'.format(U2))
print('Corriente = I: {:.2f} [A]'.format(I))
print('Factor de Potencia = fp: {:.2f}'.format(cos_2))
print('Longitud = L: {:.2f} [m]'.format(L))
print('Resistencia = R_k: {:.2f} [Ω / Km]'.format(RK))
print('Reluctancia = X_k: {:.2f} [Ω / Km]'.format(XK))
print('\n')

print('Metodo Exacto:')
RT=L*RK/1000
print('RT=L*RK/1000: {:.4f} [Ω]'.format(RT))
XT=L*XK/1000
print('XT=L*XK/1000: {:.4f} [Ω]'.format(XT))
phi2=math.acos(cos_2)
print('phi2=math.acos(cos_2): {:.4f}'.format(phi2))
U1=math.sqrt((U2*math.cos(phi2)+2*RT*I)**2+(U2*math.sin(phi2)+2*XT*I)**2)

print('Tension Entrada (ME): {:.4f} [V]'.format(U1))

print('Metodo Aproximado:')
U1=U2+2*RT*I*math.cos(phi2)+2*XT*I*math.sin(phi2)
print('Tension Entrada (MA): {:.4f} [V]'.format(U1))