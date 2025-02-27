import re

# Validar si la edad es mayor de 18
def validar_edad(edad):
    pattern = r"^(1[89]|[2-9]\d)$"
    if re.match(pattern, edad):
        return True
    else:
        return False

# Ejemplos de uso
edades = ["17", "18", "19", "20", "25", "99", "100"]

for edad in edades:
    if validar_edad(edad):
        print(f"La edad {edad} es válida (mayor de 18).")
    else:
        print(f"La edad {edad} no es válida (menor de 18).")
