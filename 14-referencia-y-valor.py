# Las variables y datos hacen referencia a un espacio en memoria pero pueden hacerlo de formas distintas

# Valor
## Se refiere al contenido real del objeto almacenado en la memoria, en el ejemplo es [1, 5, 8]
## Cuando se trabaja con tipos de datos inmutables, cada vez que cambias el valor se crea un nuevo objeto en memoria

x = 'letra X'
y = x
print(f'variable X: {x}')
print(f'variable Y: {y}')

print(f'cambio el valor de la variable Y -------')
y = 'letra Y'
print(f'variable X: {x}')
print(f'variable Y: {y}')

## Tanto X como Y, siempre tuvieron un espacio propio de almacenamiento en la memoria, por eso al cambiarlos no afectan a otros



# Referencia
## Hace que una variable apune a una direccion en memoria donde se almacena un objeto especifico
## cuando asignas un objeto a una variable, la variable no contiene el objeto en si, sino una referencia al objeto

a = [1, 3, 5]   # 'a' hace referencia al lugar donde está almacenado el objeto [1, 3, 5]
b = a      # b no es un objeto nuevo, ni una copia de a  --> solo apunta al lugar en memoria donde se ubica el objeto


## Por lo anterior, al modificar 'a' o 'b' se modifica el objeto en si y por ende, afecta a todas las variables que hagan referencia al objeto
b.append(8)
print(f'Lista a: {a}')
print(f'Lista b: {b}')

a.remove(3)
print(f'Lista a: {a}')
print(f'Lista b: {b}')



# Clasificacion de tipos
## Por valor
### int
### float
### string
### bool
### tuple   - tupla( )


## Por referencia
### list    - list[ ]
### dict    - dict{ }
### set     - set { }
### listas de comprehencion
### objetos personalizados - instancias de clases