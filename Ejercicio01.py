# Desarrolle una función que reciba una matriz N y determine si la suma de elementos 
# en su diagonal principal es par o impar. Luego utilice la función con 3 matrices diferentes.

n1 = []

a = int(input("Ingrese el numero de orden de la matriz n: "))

b = a**2
while len(n)<b:
    x = int(input("Ingrese un número: "))
    n1.append(x)


# impar/par
if sum%2==1:
    print("La suma es impar")
else:
    print("La suam es par")
