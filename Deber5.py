eye = 10
exe = 20
def modificar_global():
 global eye , x
 eye = 20
 exe = 10
 print(f"Variable global y modificada dentro de la función: {eye}")
 print(f"Variable global y modificada dentro de la función: {exe}")
modificar_global()
print(f"Variable global y fuera de la función: {eye}")
print(f"Variable global y fuera de la función: {exe}")