#Sea una línea de 132 KV que está situada en una zona forestal y agrícola.
# Justifica el número de aisladores de la cadena suponiendo que se instalan
#aisladores con LF = 291 mm. Justifica el tipo de aislador más adecuado, 
#para este tipo de instalaciones.

#Grado de Aislamiento [cm/kV]
GA=2
#Linea de Fuga [mm]
LF=291
#Tension compuesta Mas elevada [kV]
E=132


print('DATOS:')
print('Grado de Aislamiento     GA: %.2f        [cm/kV]' % GA)
print('Linea de Fuga            LF: %.2f        [mm]' % LF)
print('Tension                  E : %.2f        [kV]' % E)
print("\n")

n=GA*10*E/LF

print('RESULTADOS:')
print('n = GA   E')
print('    -------')
print('       LF')
print('Numero de Aisladores     n : %.2f' % n)