# Bucles
## Son bloque de que codigo que se ejecutará sobre cada uno de los elementos de una coleccion (objeto iterable)

## Los objetos iterables son:
cadena = 'iterable'
lista = [1, 2, 3]
tupla = ('a', 'b', 'c')
diccionario = {'user': 'Yeison', 'edad': 34, 'direccion':{'uno':1, 'dos':2}}  # se puede mediante el desempaquetado (ver ejemplo)
### Sobre ellos podemos recorrer sus elementos con la ayuda de los bucles

languages = ['C#', 'Python', 'JavaScript', 'Java', 'Go', 'PHP']



## bucle While
### Especialmente util cuando no se cuantas veces deba ejecutarse el ciclo
print('\n--------- Bucle while ---------')
contador = 0
while contador < len(languages):
    print(languages[contador])
    contador += 1

print('\nOtro ejemplo de while')
contador = 0
while contador < len(languages):
    print(f'{contador+1}. {languages[contador]}')
    contador += 1
else:    # puede tener un else, que se ejecutará siempre que el condicinal del while deje de ser verdadero
    print('Se finalizó el ciclo while, luego de imprimir todos los lenguajes')


### Cuando no se la cantidad de veces que se debe repetir la condicion
print('\nEste while se ejecutará siempre que presione una tecla diferente a "q"')
while input('ingrese letra: ') != 'q':
    print('no es q')
else:
    print('presionaste la letra "q", ahora saliste del ciclo while/n')




## Bucle for   # muy parecido a un for-Each en javascript
### Cuando sabemos cuantas veces se va a ejecutar el ciclo
print('\n--------- Bucle for ---------')
for lang in languages:
    print(lang)


print('\nfor sobre una cadena')
for character in cadena:
    print(character)


print('\nfor sobre un lista o tupla')
for elemento in tupla:
    print(elemento)

print('\nfor sobre un diccionario, # por defecto python itera sobre cada una de las keys')
for elemento in diccionario:
    print(elemento)

print('\nfor sobre un diccionario para traer sus valores')
for key in diccionario:      # for itera sobre las keys
    valor = diccionario[key]   # creamos una variable para almacenar su valor,llamando al dict y usando la key obtenida por el for
    print(valor)

print('\nfor sobre un diccionario para obtener clave y valor, se debe usar el desempaquetado')
print(diccionario.items())   # el metodo items() genera una coleccion de tuplas con los elementos clave y valor
for clave, valor in diccionario.items():  # generamos una variable cara cada elemento de la tupla "clave" y "valor"
    print(clave, '-', valor)






### Python no tiene el bucle "Do While", pero se puede implementar algo similar para ejecutar un codigo al menos 1 primera vez
print('\n--------- Bucle Do-While (No oficial) ---------')
contador = 0

while True:
    # Bloque de código que se ejecuta al menos una vez
    print(f"Contador: {contador}")
    contador += 1
    
    # Condición para salir del bucle
    if contador >= 5:
        break
print('termina bucle Do-While')


## Control de flujo de bucles
### break: Termina el bucle inmediatamente.
### continue: Salta a la siguiente iteración del bucle.
### else: Se ejecuta siempre al final de bucle, cuando el bucle termina normalmente (sin un break).
### pass: Hace que siga con la ejecucion   --- TODO pendiente por implementar
print('\n--------- Control de flujo en bucles ---------')
numeros = [1, 2, 3, 4, 5, 6, 8, 9, 10]    # A proposito no existe el numero 7

for numero in numeros:
    if numero % 2 == 0:
        continue   # Si el numero es par, salta a la siguiente iteración
    if numero == 7:
        print("Número 7 encontrado, terminando el bucle.")
        break   # termina el bucle cuando el numero es 7
    print(numero)
else:
    print('Bucle terminado sin encontrar el #7')

### Cuando el numero sea == 5, sale del for, es decir no hace mas iteraciones
### Si es par, no continua con las lineas de abajo "print()", sino que hace una nueva iteracion

