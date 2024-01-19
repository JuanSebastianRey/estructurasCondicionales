#Desarrolle un programa que determine si A ganó el set de tennis B, el set no termina o el resultado es inválido
pA = int(input('Juegos ganados por A: '))
pB = int(input('Juegos ganados por B: '))

if 0<pA<=5 and 0<pB<=5:
    print('Aun no termina')
elif 5<=pA<=7 and 5<=pB<=7:
    if pA==7:
        print('Gano el jugador A')
    elif pB==7:
        print('Gano el jugadpor B')
    else:
        print('Aun no termina')
elif pA==6 and 0<=pB<5:
    print('Gano A')
elif pB==6 and 0<=pA<5:
    print('Gano el jugador B')
else:
    print('Invalido')