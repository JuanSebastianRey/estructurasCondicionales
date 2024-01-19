# Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.

# Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

# si acaso el triángulo es inválido; y
# si no lo es, qué tipo de triángulo es.
# 

sA = float(input('Ingrese el lado a: \n'))
sB = float(input('Ingrese el lado b: \n'))
sC = float(input('Ingrese el lado c: \n'))

if sA<sB+sC and sB<sA+sC and sC<sA+sB:
    if sA==sB and sB==sC:
        print('El triángulo es equilatero')
    elif sA==sB or sA==sC or sB==sC:
        print('El triángulo es isoceles')
    else:
        print('El triángulo es escaleno')
else:
    print('No es un triangulo valido')