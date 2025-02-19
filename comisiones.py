"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones


# Entradas
L = int(input("Ventas lunes: "))
M = int(input("Ventas martes: "))
X = int(input("Ventas miércoles: "))
J = int(input("Ventas jueves: "))
V = int(input("Ventas viernes: "))
# Proceso
ventas = (L+M+X+J+V)

#comisión

if ventas <= 20000:
    comision = ventas * 0.05

elif ventas > 20000:
    comision = ventas * 0.06 

# Salidas
print("Ventas totales: " + str(ventas))
print ("Comisión: " + str(comision))