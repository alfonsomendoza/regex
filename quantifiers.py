####
## 03-Quantifiers
""" Los Quant cuantas ocurrencias de un caracter o grupo de caracteres se deben
encontrar en una cadena""" 
###


import re


# :* Puede aparecer 0 o mas veces 

text="aaaba"
pattern = r"a*"
matches = re.findall(pattern, text)

print(matches)

# Ejercicio

# Cuantas palabras tienen de 0 a  mas "a" y despues una "b"

# +: Puede aparecer 1 o mas veces

text="dddd aaa ccc ba"

pattern = r"a+"

matches = re.findall(pattern, text)

print(matches)

# ?: Puede aparecer 0 o 1 vez

text="aaabacb"
pattern = r"a?b"

matches = re.findall(pattern, text)
print(matches)

# Ejercicio haz opcional que aparezca un +34 en el siguiente texto

phone = "+34 123456789"

pattern= r"(\+34|00)?\d{9}"
valid = re.search(pattern, phone)
if valid:
    print("Número de teléfono válido")
else:
    print("Número de teléfono no válido")
    
# {n}: Puede aparecer n veces

text="aaaaaaab aa  aaaaab"
pattern = r"a{3}"
matches = re.findall(pattern, text)
if matches:
    print("Se encontró la cadena")
    print(matches)
else:
    print("No se encontró la cadena")
    

#{n, m}: Puede aparecer de n a m veces

text="u uu uuuu uuuuuuu uuuuuuuuuu uuuuuuuu"
pattern = r"wolf{2,3}"
matches = re.findall(pattern, text)
print(matches)


# Ejercicio :
# Encuentra todas las palabras que tengan de 4 a 6 en el siguiente texto

words="ala casa arbol leon cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
if matches:
    print("Se encontró la cadena")
    print(matches)
else:
    print("No se encontró la cadena")
    
#Ejercicio:
#Encuentra todas las palabras que tengan mas de 6 letras en el siguiente texto

words="ala fantastico  casa arbol leon cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
if matches:
    print("Se encontró la cadena")
    print(matches)
else:
    print("No se encontró la cadena")
    







