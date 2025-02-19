"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones


# Entradas
L = float(input("Ventas lunes: "))
M = float(input("Ventas martes: "))
X = float(input("Ventas miércoles: "))
J = float(input("Ventas jueves: "))
V = float(input("Ventas viernes: "))
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