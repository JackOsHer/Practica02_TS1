#Desarrolle una aplicación que solicite al usuario 6 números distintos entre 1 y 10. 
# Luego haga que el sistema genere 6 números aleatorios distintos entre los números 1 y 10
#  y compare cuántos aciertos tuvo el usuario. Si el usuario acertó los 6 números, muestre el 
# mensaje: "Ha ganado 6 millones de soles". Para 5 aciertos: 
# "Ha ganado 100 mil soles". Para 4 aciertos o menos: "Siga intentado".
import random
a = []
while (len(a)<6):
    num = int(input("Ingrese un número: "))
    if 1<=num<=10 and a.count(num)==0:
        a.append(num)
    else: 
        print("Numero inválido")

n = []
for i in range(1, 11):
    n.append(i)

m=[]
while len(m)<6:
    b = random.choice(n)
    m.append(b)
    n.remove(b)
print(a)
print(m)

sum=0

for i in a:
    if m.count(i)==1:
        sum += 1

if sum==6:
    print("Ha ganado 6 millones de soles :D")
elif sum==5:
    print("Ha ganado 100 mil soles xD")
else:
    print("Siga intentando")