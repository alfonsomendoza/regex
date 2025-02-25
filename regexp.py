# 1.Importar el modulo de expresiones regulares "re"
import re
# 2. Crear un patron de busqueda
pattern = "hola"
# 3. Crear un texto donde buscar el patron
text=   "hola mundo"
# 4. Usar la funcion match para buscar el patron en el texto que seria re.match(patron, texto)
result = re.match(pattern, text)
# 5. Imprimir el resultado
if result:
    print("He encontrado el patron en el texto")
# 6. Si no se encuentra el patron en el texto, imprimir un mensaje
else:
    print("No he encontrado el patron en el texto") 
    
#group() Devuelve el texto que coincide con el patrón
print(result.group())

#start() Devuelve la posición inicial del texto que coincide con el patrón
print(result.start())

#end() Devuelve la posición final del texto que coincide con el patrón
print(result.end())

# Ejercicio 1
#Encuentra la primera ocurrencia de la palabra "IA" en el siguente texto
#siguiente texto
# E indica la posición inicial y final de la coincidencia

text = "La inteligencia artificial IA está revolucionando múltiples industrias en todo el mundo   Desde la automatización de procesos hasta la mejora de la toma de decisiones,  ofrece una amplia gama de aplicaciones que están transformando la manera en que vivimos y trabajamos.  En el sector de la salud,  está ayudando a los médicos a diagnosticar enfermedades con mayor precisión y a desarrollar tratamientos personalizados.En el ámbito empresarial, las empresas están utilizando la  para analizar grandes volúmenes de datos y obtener información valiosa que les permite tomar decisiones más informadas. Además, está desempeñando un papel crucial en la investigación científica, acelerando el descubrimiento de nuevos conocimientos y tecnologías.A medida que continúa avanzando, es fundamental abordar los desafíos éticos y sociales que surgen con su implementación, a segurando que su desarrollo y uso beneficien a toda la humanidad" 

pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
    print(f"He encontrado el patron en el texto en la posición {found_ia.start()} y {found_ia.end()}")
else:   
    print("No he encontrado el patron en el texto")

#Encontrar todas la coincidencias de una patron 
#findall() Devuelve una lista con todas las coincidencias del patrón en el texto

text= "Me gusta python, me gusta programar en python,python es lo maximo,python no es dificil,ojo con python"

pattern = "python"
matches = re.findall(pattern, text)

print(matches)

print(f"Se han encontrado {len(matches)} coincidencias")

# iter() Devuelve un iterador que produce objetos de coincidencia en el texto
#finditer() Devuelve un iterador que produce objetos de coincidencia en el texto

text= "Me gusta python, me gusta programar en python,python es lo maximo,python no es dificil,ojo con python"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(),match.start(),match.end())
    
# Ejercicio 2

"""Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto
en el siguiente texto e indica la posición inicial y final de cada coincidencia
y cuantas veces se encontró la palabra"""

text="Este es el  curso de python de midudev.! Suscribite a midudev si te gusta este contenido! midu"


# Modificadores
# Los modificadores son opciones que se pueden agregar a un patrón de expresión regular para modificar su comportamiento.
# Los modificadores se colocan después del patrón y se especifican con una letra.

# re.IGNORECASE (o re.I) - Ignora las mayúsculas y minúsculas


text="Este es el  curso de python de MidU.! Suscribite a miDu si te gusta este contenido! mIdu"

pattern = "midu"
found = re.findall(pattern, text, re.IGNORECASE)

if found:
    print(found)
    print(f"Se han encontrado {len(found)} coincidencias")

"""if found_ia:
    print(f"He encontrado el patron en el texto en la posición {found_ia.start()} y {found_ia.end()}")
else:   
    print("No he encontrado el patron en el texto")"""
    
    
    
# Reemplazar texto
# re.sub() - Reemplaza una o varias coincidencias con una cadena

text = "La inteligencia artificial IA está revolucionando múltiples industrias en todo el mundo"
pattern = "IA"
replacement = "Inteligencia Artificial"
new_text = re.sub(pattern, replacement, text)
print(new_text)

