
## Tipos de datos
numero = 5     # int    # inmutable
decimal = 5.2  # float con punto
marca = 'Samsung'      # inmutable
booleano = True
atributo = None  # especial cuando no se que tipo de valor se va a asignar a la variable

## Tipos de datos de secuencia
mi_lista = [4, 6, 8]   # list [ ] -> mutable, separados por coma y tienen indice
mi_tupla = (9, 8, 7)   # tuple ( ) # inmutable
mi_range = range(10)


## Tipo Range   - rango
### es una secuencia inmutable de numeros enteros, normalmente usada dentro de un for

a = range(0,10,1) # inicial(incluido), final(NO incluido, incremento)
b = range(10)   # Forma abreviada, se asume inicio en 0 y paso de 1
print(type(a))

for i in range(10):
    print(i)


## Tipos de mapeo
## Dict   -  Diccionario, tiene clave y valor (es como un objeto)
mi_diccionario = {
    'nombre': 'Juan',
    'a': 2, 
    'b': 5,
    1 : 'uno',
    'cedula': 498616,
    'isHuman': True
}

user = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}
categoria = {1: 'uno', 2: 'dos', 3: 'tres'}

print(f'Ciudad del usuario: {user['ciudad']}')
print(categoria[2])


## Tipos de conjuntos
## Set     -  coleccion de elementos unicos e inmutables y ordenada alfabeticamente
otro_set = {1, 2, 3, 4} 



## Conocer el tipo de dato  - usar type()
print(type(decimal))


## Variables algunas pueden ser:
## mutables: se pueden cambiar de valor, mientras que otras son 
## inmutables: no se pueden modificar
camb = 'mazda'
camb = 6
print(camb)

## Nombrar variables
### usar snake_case "_" guion bajo
### no se permite usar "-" guion medio

nombre_variable = 2
# nombre-variable = 2  # esto no es permitido, entiende el "-" como una resta


## Nombrar clases
### usar CamelCase
#class MiClase:


# Switch 2 variables
x = 3
y = 4
x, y = y, x # switch

print("x switched: ", x)
print("y switched: ", y)



# Recibir datos del usuario
"""
name = input('What is your name?\n')
print (name)

edad = input('Cual es tu edad?\n')
print (type(edad))  # el tipo de dato generado en el imput siempre es string
int(edad)   # convertir a numero
print (type(edad))  
"""


# Concatenar texto y variables
name = "Camilo"
print ('Hi,', name)   # concatenar con coma
print (f'Hi, {name}')   # concatenar con f''
print ('Hola, {user}'.format(user=name))    # concatenar con el metodo .format()




## Encadenar metodos


## Esto no funciona ya que ambos elementos devuelven un objeto None
# new_set.add(11).discard(3)
# print(new_set)



## desempaquetado
### se generan varias variables para que se les asigne cada uno de los valores de la tupla
print('\ndesempaquetado -----------')
user, edad, otra = ('eduardo', 27, 'carro')  # la regla es que para cada valor de la tupla debe definirse una variable

print(f'user en la tupla: {user}')
print(f'edad en la tupla: {edad}')
