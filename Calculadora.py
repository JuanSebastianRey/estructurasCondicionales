# Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
n1 = float(input('Ingrese el primer numero:\n '))
o = input('Ingrese la operacion que quiere realizar: ')
n2 = float(input('Ingrese el segundo numero:\n '))
if o=='+':
    print(f'{n1} {o} {n2} = {n1+n2}')
elif o=='-':
    print(f'{n1} {o} {n2} = {n1-n2}')
elif o=='*':
    print(f'{n1} {o} {n2} = {n1*n2}')
elif o=='/':
    print(f'{n1} {o} {n2} = {n1/n2}')
else:
    print('Ingrese un operador valido')
