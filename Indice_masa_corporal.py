h = float(input('Ingrese su altura en centimetros:\n '))
w = float(input('Ingrese su peso en kilos:\n '))
a = int(input('Ingrese su edad:\n '))
imc = (w)/((h/100)**2)
if a>=45:
    if imc>=22:
        print('Riesgo alto')
    else:
        print('Riesgo medio')
elif 0<a<45:
    if imc>=22:
        print('Riesgo medio')
    else:
        print('Riesgo bajo')
else:
    print('Ingrese una edad valida')