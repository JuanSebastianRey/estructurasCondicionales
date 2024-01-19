# Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.
user = input('Ingresa un caracter:\n ')
while len(user)>1:
    print('Por favor ingrese solo un caracter: \n')
    user = input('Ingrese el caracter:\n ')
if 48<=ord(user)<=57:
    print('Es un numero')
elif 65<=ord(user)<=90:
    print('Es una letra mayuscula')
elif 97<=ord(user)<=122:
    print('Es una letra minuscula')
else:
    print('No ni es letra, ni es un número')