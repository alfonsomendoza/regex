import re

#[:] coincide con cualquier caracter excepto el salto de linea

username="rub.$ius_69+"
pattern=r"^[\w._%+-]+$"

matches = re.search(pattern, username)
if matches:
    print("Nombre de usuario válido",matches.group())
else: print("Nombre de usuario no válido")

#Buscar todas las vocales de una palabra

text="Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text) 
print(matches)
if matches:
    print("Se encontró la cadena")
    print(matches)
else:   print("No se encontró la cadena")

# Una regex para encontrar las palabras man,fan y ban
# pero ignora el resto

text="man ran fan ñan ban"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
if matches:
    print("Se encontró la cadena")
    print(matches)
else:
    print("No se encontró la cadena")
    
#Ejercicio
# Ejercicto:
# Nos han compticado et asunto, porque ahora hay palabras que
#encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban

text ="omniman fanatico man bandana fanfarron bananero fan  ban"
#\b

pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text) 
if matches:
    print("Se encontró la cadena")
    print(matches)
else:
    print("No se encontró la cadena")

text="22"
pattern=r"{1-2}"

matches = re.findall(pattern, text)
print(matches)
if matches:
    print("Se encontró la cadena")
    print(matches)
else:
    print("No se encontró la cadena")



