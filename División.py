#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.
dividendo=int(input('Dividendo: '))
divisor=int(input('Divisor: '))

quo=dividendo//divisor
remain=dividendo%divisor

if remain==0:
    print('La división es exacta\n')
    print(f'El cociente es: {quo}')
    print(f'El resto es: {remain}')
else:
    print('La división no es exacta\n')
    print(f'El cociente es: {quo}')
    print(f'El resto es: {remain}')
    