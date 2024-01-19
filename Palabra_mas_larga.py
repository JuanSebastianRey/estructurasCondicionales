#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.
w1 = input('Ingrese la primera palabra:\n ')
w2 = input('Ingrese la segunda palabra:\n ')

if len(w1)>len(w2):
    print(f'La palabra {w1} tiene {len(w1)-len(w2)} letras más que {w2}.')
elif len(w1)==len(w2):
    print('Las dos palabras tienen el mismo largo.')
else:
    print(f'La palabra {w2} tiene {len(w2)-len(w1)} letras más que {w1}.')