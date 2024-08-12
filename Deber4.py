# Eliminar el variable local

exe = 10 # Variable global
def mi_funcion():
  exe = 10
  print(f"Variable global x dentro de la función: {exe}")
mi_funcion()
print(f"Variable global x afuera de la función: {exe}")