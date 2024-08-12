def operaciones_basicas(a, b):
 suma = a + b
 resta = a - b
 multi = a * b
 return suma, resta, multi
resultdosuma, resultdoresta, resultmulti = operaciones_basicas(8, 3)
print(f"Suma: {resultdosuma}, Resta: {resultdoresta}, Multiplicacion: {resultmulti}")