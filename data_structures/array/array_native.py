import array

arrIntegers = array.array('i', [1, 2, 3, 4])  # 'i' indica enteros con signo
arrIntegers.append(5)  # Agregar elemento
print(arrIntegers[2])  # Acceder al índice 2

arrCars = ["Porsche", "Volvo", "BMW"] # arreglo de strings
arrCars.append("Lambo")
print(arrCars[1])

arrCars[1]="Maserati"

for c in arrCars:
  print(c)

for l in arrCars[0]:
    print(l)

