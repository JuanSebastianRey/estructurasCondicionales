numbers = []
array_l = int(input('Ingrese la cantidad de números que desea ordenar: '))

def bubble_sort(array):
    """ Bubble sort implementation """
    for i in range(len(array)-1):
        swapped=False
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
                swapped=True
                if swapped==False:
                    break
    return array
        

for i in range(array_l):
    placeholder = int(input('Ingrese numero: '))
    numbers.append(placeholder)

bubble_sort(numbers)

for number in numbers:
    print(number, end=' ')
