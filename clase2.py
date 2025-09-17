#calculadora

numero1 = float(input(f"introduce el primer numero \n "))
operador = input(f"introduce el operador \n ")
numero2 = float(input(f"introduce el segundo numero \n"))


if operador == '+':
    print(numero1 + numero2)
elif operador == '-':
    print(numero1 - numero2)
elif operador == '*':
    print(numero1 * numero2)
elif operador == '/':
    print(numero1 / numero2)
else:
    print(f"el operador no puede ser procesado")
