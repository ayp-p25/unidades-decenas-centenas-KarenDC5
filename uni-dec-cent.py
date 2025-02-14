"""
Unidades, decenas y centenas que tiene un número 
Karen Durán Cárdenas 
757136
Ingeniería Civil 
Algoritmos y Programación 
ESI232B2
14/02/25
10 min
"""

# Entradas
numero = float(input("Introduzca un número: "))

# Proceso
centenas = numero//100
decenas = (numero - (100*centenas))//10
unidades = numero - 100*centenas - 10*decenas 

# Salidas
print("Centenas: ", centenas)
print("Decenas: ", decenas)
print("Unidades: ", unidades)
