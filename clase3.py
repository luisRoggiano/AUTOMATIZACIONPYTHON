#while actúa como un for, pero requiere un contador o limitante que impida que entre en bucle infinito.

i = 1
while i <= 5:
    print(i)
    #i = i+1
    i += 1



#diccionario
#si quisieramos acceder a las claves valor tenemos dos formas
#para acceder a las claves usamos keys
#para acceder a los valores usamos values
#para acceder a ambos usamos items.

personaDic = {
    "nombre": "Luis",
    "apellido":"Roggiano",
    "edad":39
}

print(personaDic.keys())
print(personaDic.values())
print(personaDic.items())


#Listas

listaPersona = ["Luis", "Roggiano", 39]

for i in listaPersona:
    print(i)


#funciones, permite reutilizar un bloque de código a lo largo de todo mi código, utilizando la sintaxis def


def saludo(nombre):
    return print (f"hola {nombre}")

#saludo(input("ingrese su nombre \n"))

gente = ["Luis", "Ramon", "Pedro"]

for i in gente:
    saludo(i)

#Calculadora mejor

def calculadora(a, operacion, b):
    if operacion == "+":
        resultado = a + b
    elif operacion == "-":
        resultado = a - b
    elif operacion == "*":
        resultado = a * b
    elif operacion == "/":
        resultado = a / b
    else : 
        print(f"el operador {operacion} no es conocido")
        return None
    return resultado    

#calculadora(float(input()), input(), float(input()))

#manejo de errores, el primero es bastante especifico
#ZeroDivisionError, division por 0 obviamente no se puede
#ValueError: error en el valor
#KeyError: error en la key de un diccionario.

try:
    resultado = 0/0
except ZeroDivisionError as e: #as e es convencion para ver el error
    print(f"Error: {e}")

try:
    numero = int("doce")
except ValueError as e:
    print(f"Error: {e}")

try:
    print(personaDic['nacionalidad'])
except KeyError as e:
    print(f"Error: {e}")