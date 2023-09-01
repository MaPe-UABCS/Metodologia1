# instrucciones: obtener el peso de x alumnos, y obtener el mas pesado, el mas ligero y el promedio

import functools

def getNumberInput(message):
    value = int(input(message))
    return value

def average(studentsWeight):
    total = functools.reduce((lambda t,n:t+n), studentsWeight) 
    return total / len(studentsWeight)

def findMax(studentsWeight):
    # declarado a mano
    max = studentsWeight[0]
    for weight in studentsWeight:
        if weight > max:
            max = weight
    return max; 

def findMin(studentsWeight):
    # declarado a mano
    min = studentsWeight[0]
    for weight in studentsWeight:
        if weight < min:
            min = weight
    return min; 

if __name__ == "__main__":
    students = getNumberInput("ingrese el numero de estudiantes:  ")
    studentsWeight = []

    for i in range(students):
        value = getNumberInput(f"ingrese el peso del estudiante {i + 1}:  ")
        studentsWeight.append(value)
 
    max = findMax(studentsWeight)
    min = findMin(studentsWeight)
    avg = average(studentsWeight)
    print('-'*30)
    print("resultados: ")

    print(f"el mas pesado: {max}")
    print(f"el mas ligero: {min}")
    print(f"pesos promedio: {avg}")




