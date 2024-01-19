

ano=int(input('Ingrese el año:\n'))
if ano<=1599:
    if(ano%4==0):
        print(f'{ano} es bisiesto')
    else:
        print(f'{ano} no es bisiesto')
else:
    if(ano%100==0 and ano%400==0):  
        print(f'{ano} es bisiesto')
    else:
        if (ano%4==0):
            if(ano%100!=0): 
               print(f'{ano} es bisiesto')
            else:
                print(f'{ano} no es bisiesto')
        else:
             print(f'{ano} no es bisiesto')