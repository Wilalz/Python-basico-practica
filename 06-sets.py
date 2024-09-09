# Conjuntos - set
## Colección desordenada de elementos únicos

## Crear un set
mi_set = set()  # crea un set vacio

otro_set = {1, 2, 3, 4}   # se usan { } y poner directamente los elementos

otro_set_mas = {1, 2, 3, 4, 4}  # esto dará el mismo set de arriba {1, 2, 3, 4} eliminando los duplicados

## Convetir una lista en un set   --- elimina los duplicados
mi_lista = [5, 8, 9, 2, 2, 5, 1, 9, 6]
print(f'lista original: {mi_lista}')
new_set = set(mi_lista)
print(f'set() convertido a set: {new_set}')


## Añade un ítem al conjunto    # usar .add()   # si ya existe no pasa nada
new_set.add(3)
print(f'add() añadido elemento "3" al set: {new_set}')


## Elimina un ítem del conjunto   # usar .remove()  # genera un error si el ítem no existe.
new_set.remove(8)
print(f'remove() eliminado elemento "8" del set: {new_set}')

### Si el elemento no existe mostrará un error
### new_set.remove(8)


## Elimina un ítem del conjunto si existe    # usar .discard()  # si no existe no pasa nada
new_set.discard(8)
print(f'discard() eliminado elemento "8" del set: {new_set}')
new_set.discard(9)
print(f'discard() eliminado elemento "9" del set: {new_set}')


## Elimina un ítem (aleatorio) del conjunto y devuelve el item eliminado   # usar .pop()  
### Nota: parece que siempre elimina el primer elemento
elemento_eliminado = new_set.pop()
print('elemento eliminado', elemento_eliminado)
print('set despues de elimar con pop(): ', new_set)


# Operaciones con los set (conjuntos)
## Unión de conjuntos     # usar .union()  # agrupa varios conjuntos en uno solo
print('\nunion de conjuntos ----------')
setUnion = new_set.union(otro_set)
print(f'new_set: {new_set}')
print(f'otro_set: {otro_set}')
print(f'union entre new_set y otro_set: {setUnion}')


## Intersección entre conjuntos    # usar .intesection()  # agrupa los elementos presentes en ambos conjuntos
print('\ninterseccion de conjuntos ----------')
setInterseccion = new_set.intersection(otro_set)
print(f'new_set: {new_set}')
print(f'otro_set: {otro_set}')
print(f'union entre new_set y otro_set: {setInterseccion}')


## Diferencia de conjuntos     # usar .difference()  
print('\nDiferencia de conjuntos ---------------')
new_setDiferenciaOtro_set = new_set.difference(otro_set)   # Los elementos del primer conjunto que no están en el segundo
otro_setDiferenciaNew_set = otro_set.difference(new_set)   # Los elementos del segundo conjunto que no están en el primero

print(f'new_set: {new_set}')
print(f'otro_set: {otro_set}')
print(f'diferencia entre new_set y otro_set (presentes solo en el primer set): {new_setDiferenciaOtro_set}')
print(f'diferencia entre otro_set y new_set (presentes solo en el segundo set): {otro_setDiferenciaNew_set}')







