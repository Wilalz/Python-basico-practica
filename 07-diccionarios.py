# Diccionarios

## No se identifican los valores guardados por indice sino por medio de una etiqueta llamada clave (key)

mi_diccionario = {
    'nombre': 'Juan',
    'a': 2, 
    'b': 5,
    1 : 'uno',
    'cedula': 498616,
    'isHuman': True
}


## Ver las keys y/o elementos que tiene el dict
print(f'Keys que tiene el diccionario: {mi_diccionario.keys()}')    # solo claves

print(f'Values que tiene el diccionario: {mi_diccionario.values()}')   # solo valores

print(f'items que tiene el diccionario: {mi_diccionario.items()}')    # claves y valores


## Obtener los elementos del dict
print('a: ', mi_diccionario['a'])
print('cedula: ', mi_diccionario.get('cedula'))



#### por practicar ----------------------

## Actualiza el diccionario con los pares clave-valor de otro diccionario u otro iterable de pares clave-valor.
# dict.update([other])
### si lo tiene lo reemplaza, si no lo tiene lo agrega

## Elimina la clave y devuelve su valor, o devuelve un valor por defecto si la clave no existe.
# dict.pop(key[, default])