
# Listas

## Creacion de listas   # se recomiena que una lista solo tenga valores del mismo tipo de dato
languages = ['Ruby', 'JavaScript', 'Java', 'Go', 'PHP']
arr = [1, 6, 9, 6, 8, 3]

## acceder a un indice de la lista
print(f'--- La lista original es: {arr} ---')
print(f'el indice 3 del la lista es: {arr[3]}')
print(f'el ultimo indice de la lista es: {arr[-1]}')

## son mutables, sus valores se pueden cambiar (a diferencia de una tupla que es inmutable)
print("lista de lenguajes: ", languages)
languages[0] = 'Python'   # cambia el valor de la posicion 0 de la lista
print("Lista de lenguajes modificada: ", languages)

## Acceder a elementos de la lista
print('lenguje # 1 de la lista:', languages[0])
print("ultimo lenguje de la lista:", languages[-1]) # muestra el ultimo elelmento de la lista, de atraás para adelante
print("rango de lenguajes [1:3]:", languages[1:3]) # muestra desde el indice-inicial(incluido) hasta ":" el indice-final (NO incluido)
print("rango de lenguajes [:3]:", languages[:3]) # Si se omite el indice-inicial, entonces asume 0
print("rango de lenguajes [1:]:", languages[1:]) # Si se omite el indice-final, entonces asume hasta el ultimo indice
print("rango de lenguajes [1:2:1]:", languages[1:2:1]) # inicio : fin () : salto (default es 1)


## Saber si hay un elemento en una lista
print('PHP' in languages)

# Metodos de listas
## Conocer el largo de una lista
print(f'la lista languages tiene {len(languages)} elementos')

## Ordenar una lista   # de forma ascendente
arr.sort()
print('lista ordenada:', arr)
languages.sort(reverse=True)
print('lenguajes ordenada: ', languages)

### Orden descendente
languages.sort(reverse=True)
print('lenguajes orden descendente: ', languages)


### el metodo sort() no puede ordenar una lista si esta está conformada de varios tipos de datos [1, 2, 'Perro', 'Casa', False]

## agregar elementos en una lista   # usar .insert(<indice>, <elemento>)
### Los demás elementos se conservan, no se sobreescriben
languages.insert(4, 'Ruby')
print(f'Insertado Ruby en el indece 4: {languages}')

languages.insert(0, 'C#')
print(f'Insertado C# al inicio de la lista: {languages}')


## agregar al final  # usar .append()
arr.append(5)
print(f'arr ingresando el 5 al final: {arr}')

## eliminar un elemento especifico de la lista  # usar .remove(<elemento>)
languages.remove('Ruby')
print(f'metodo remove para eliminar ruby: {languages}')

arr.remove(max(arr))
print(f'lista eliminando el numero maximo: {arr}')

## eliminar un indice de la lista # usar .del(<indice-elemento>)
del arr[4]  # 
print(f'lista eliminando el indice 4: {arr}')


## Eliminar todos los elementos de una lista
languages.clear()
print(f'Eliminados todos los elementos de la lista languages: {languages}')