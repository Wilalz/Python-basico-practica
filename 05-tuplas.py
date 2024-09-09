# tuple    - Tuplas
## son inmutables
## principalmente para guardar una fecha, coordenadas geograficas
## Los datos de una tupla pueden estar repetidos
tupla = (1, 2, 3, 1, 1, 2)
## tupla[2] = 8 ---- # no se puede reasignar
print("tupla: ", tupla[1])
print("tupla: ", tupla[-1]) # accede de atras para adelante



#### por practicar ----------------------

## Devuelve el número de veces que un determinado ítem aparece en la tupla.
print(tupla.count(1))

## Devuelve el índice de la primera aparición de un ítem.
# tupla.index(item[, start[, stop]])
print(tupla.index(2))



## Se ha indicado que una tupla no se puede modificar, pero veamos el siguiente ejemplo
t = ([0, 1, 2], 101, 102, 103, 104, 105, {"a": 1, "b": 2}, {1, 3, 5})
print(f'tupla original: {t}')

t[0].append(5)
print(f'Lista modificada en una tupla: {t}')
### Como se observa, pudimos modificar los valores de la tupla...
### la explicacion para esto es que no se puede modificar a la tupla, pero si a los objetos que contiene
### es decir, no puedes reemplazar a t[0] con otro objeto, porque no puedes modificar las referencias a los objetos que contiene
### Sin embargo, las listas son mutables, así que si puedes modificar el contenido de la lista

### Otros objetos que son mutables tambien pueden ser modificados dentro de una tupla
#### dict
t[6]['c'] = 3
print(f'Modificando un diccionario en una tupla: {t}')

#### set
t[7].add(8)
print(f'Modificando un set en una tupla: {t}')

#### objetos de clases personalizadas


