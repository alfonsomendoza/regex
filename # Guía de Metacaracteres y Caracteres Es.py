# Guía de Metacaracteres y Caracteres Especiales en Regex

## Metacaracteres

Los metacaracteres son símbolos especiales que tienen significados específicos en las expresiones regulares. A continuación se presentan algunos de los metacaracteres más comunes:

### 1. El punto (.)
- **Descripción**: Coincide con cualquier carácter, excepto un salto de línea.
- **Ejemplo**: `H.la` coincide con "Hola", "H$la", "H1la", etc.

### 2. El asterisco (*)
- **Descripción**: Coincide con cero o más repeticiones del carácter anterior.
- **Ejemplo**: `a*` coincide con "", "a", "aa", "aaa", etc.

### 3. El signo más (+)
- **Descripción**: Coincide con una o más repeticiones del carácter anterior.
- **Ejemplo**: `a+` coincide con "a", "aa", "aaa", etc., pero no con "".

### 4. El signo de interrogación (?)
- **Descripción**: Coincide con cero o una repetición del carácter anterior.
- **Ejemplo**: `a?` coincide con "", "a".

### 5. Las llaves ({})
- **Descripción**: Coincide con un número específico de repeticiones del carácter anterior.
- **Ejemplo**: `a{3}` coincide con "aaa".

### 6. Los corchetes ([])
- **Descripción**: Coincide con cualquier carácter dentro de los corchetes.
- **Ejemplo**: `[abc]` coincide con "a", "b", o "c".

### 7. El guion (-)
- **Descripción**: Define un rango de caracteres dentro de los corchetes.
- **Ejemplo**: `[a-z]` coincide con cualquier letra minúscula de la "a" a la "z".

### 8. El circunflejo (^)
- **Descripción**: Coincide con el inicio de una cadena.
- **Ejemplo**: `^Hola` coincide con "Hola mundo" pero no con "Mundo Hola".

### 9. El signo de dólar ($)
- **Descripción**: Coincide con el final de una cadena.
- **Ejemplo**: `mundo$` coincide con "Hola mundo" pero no con "mundo Hola".

### 10. El símbolo de barra invertida (\)
- **Descripción**: Escapa un metacaracter para que sea tratado como un carácter literal.
- **Ejemplo**: `\.` coincide con un punto literal ".".

## Caracteres Especiales

### 1. \d
- **Descripción**: Coincide con cualquier dígito (equivalente a `[0-9]`).
- **Ejemplo**: `\d` coincide con "1", "2", "3", etc.

### 2. \D
- **Descripción**: Coincide con cualquier carácter que no sea un dígito.
- **Ejemplo**: `\D` coincide con "a", "b", "c", etc.

### 3. \w
- **Descripción**: Coincide con cualquier carácter de palabra (letras, dígitos y guiones bajos).
- **Ejemplo**: `\w` coincide con "a", "1", "_", etc.

### 4. \W
- **Descripción**: Coincide con cualquier carácter que no sea de palabra.
- **Ejemplo**: `\W` coincide con " ", "!", "@", etc.

### 5. \s
- **Descripción**: Coincide con cualquier carácter de espacio en blanco (espacios, tabulaciones, saltos de línea).
- **Ejemplo**: `\s` coincide con " ", "\t", "\n", etc.

### 6. \S
- **Descripción**: Coincide con cualquier carácter que no sea un espacio en blanco.
- **Ejemplo**: `\S` coincide con "a", "1", "!", etc.