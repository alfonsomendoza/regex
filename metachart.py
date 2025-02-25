###

# 02 -Metacaracteres

# Los metacaracteres son simbolos especiales con significados especificos
# en las expresiones regulares.

###

import re


# 1. El punto(.)
# Coincidir con cualquier caracter, excepto un salto de linea

text = "Hola mundo, Hola de nuevo,H$la otra vez"

pattern = "H.la"  # Hola, Hola, H$la

found = re.findall(pattern, text)

if found:
    print(found)
    print(f"Se han encontrado {len(found)} coincidencias")
else:
    print("No se han encontrado coincidencias")


text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)

print(matches)

print(f"Se han encontrado {len(matches)} coincidencias")

# \. metacaracter de escape
# Utiliza el metacaracter de escape para buscar caracteres especiales
text = "Mi casa es blanca. Y el coche es negro."

pattern = r"\."

matches = re.findall(pattern, text)

print(matches)

# Como usar \ la barra invertidad para anular el significado especial de un simbolo
# \. metacaracter de escape
# Utiliza el metacaracter de escape para buscar caracteres especiales
text = "Mi casa es blanca. Y el coche es negro."

pattern = r"\."

matches = re.findall(pattern, text)

print(matches)  # Esto imprimirá ['.', '.'] ya que hay dos puntos en el texto

print(f"Se han encontrado {len(matches)} coincidencias")

# \d: coincide con cualquier digito(0-9)

text = "El numero de telefono es 123456789"

found = re.findall(r"\d{9}", text)

print(found)

if found:
    print(f"El número de teléfono es: {found[0]}")

# Ejercicio : Detectar si hay un numero de Espana en el texto gracias al prefijo #34

text = "Mi numero de telefono es +34 688999999 apuntalo vale?"

pattern = r"\+34 \d{9}"

found = re.search(pattern, text)

print(found)

found.group()

if found:
    print(f"El número de teléfono de España es: {found.group()}")
    


# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)



text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualqueir espacio en blanco (espacio, tabulación, salto de línea)
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)


# ^: Coincide con el inicio de una cadena

phone = "+34 123 456 789"
pattern= r"^\+\d{1,3}"

valid = re.search(pattern, phone)
if valid:
    print("Número de teléfono válido")
else:
    print("Número de teléfono no válido")
    

#$: Coincide con el final de una cadena

text="Hola mundo"
pattern = r"mundo$"
valid = re.search(pattern, text)
if valid:
    print("Cadena válida")
else:
    print("Cadena no válida")

#Ejercicio
#validar un correo electronico

email = "miduga@gmail.com"
pattern = r"^\w+@gmail.com$"

valid = re.search(pattern, email)
if valid:
    print("Correo válido")
else:
    print("Correo no válido")


#Ejercicio:
#Tenemos una lista de archivos de texto, queremos saber si un archivo es un archivo de texto
#si el archivo termina en .txt
#
files = "archivo1.txt archivo2.csv archivo3.txt archivo4.jpg"
pattern = r"\b\w+\.txt\b"  # Coincide con palabras que terminan en .txt

valid = re.findall(pattern, files)
print(valid)

# \b: coincide con el inicio o el final de una palabra

text = "casa, coche, perro,cosa, acasa, casada ,casado"
pattern = r"\bc.sa\b" 
found = re.findall(pattern, text)
print(found)

# |: Operador OR coincide con una de las dos opciones

fruits = "platano, manzana, pera, sandia, melon,aguacate,palta"
pattern = r"palta|aguacate|p..a|\b\w{7}|b"   # Coincide con manzana o pera
found = re.findall(pattern, fruits)
print(found)

if found:
    print(f"Se han encontrado {len(found)} coincidencias")
else:
    print("No se han encontrado coincidencias")