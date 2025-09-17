#rango

nombre = ["ramon", "pedro", "david", "jonyfinder"]
edad = [49, 28, 35, 32]
profesion = ["plomero", "programador", "vendedor", "rappi"]
for each in range(len(nombre)):
    print(f"buenas tardes mi nombre es {nombre[each]} tengo {edad[each]} y soy {profesion[each]}")

pares = []
#range(start, stop, step)
for n in range (0,21,2):
    if n % 2 == 0:
        pares.append(n)
print(pares)

while n < 22:
    for n in range (0,21,2):

        print(n)
    break
