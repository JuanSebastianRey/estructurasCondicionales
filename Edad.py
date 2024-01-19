from time import localtime
t=localtime()
ano=int (input('Dame tu ano de naciemiento:\n'))
mes=int (input('Dame tu mes de naciemiento:\n'))
dia=int (input('Dame el dia tu nacimiento:\n'))
ano_actual=t.tm_year
mes_actual=t.tm_mon
dia_actual=t.tm_mday
edad=ano_actual-ano
if (dia_actual<dia and mes_actual<=mes):
    edad-=1
print(f'Tu edad acutal es: {edad}')
