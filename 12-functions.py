# Funciones
name = 'Wilson'
#name = input('Ingrese su nombre:\n')

## Estructura de una funcion
def nombre_de_la_funcion (parametros):
    # Bloque de codigo a ejecutar
    return valor_de_retorno # type: ignore


## Definir una funcion llamada greet la cual imprime un mensaje
def greet (name="Camilo"):
    print("Bienvenido,", name)

## Llamar a una funcion  #escribir su nombre y ( )
### en este caso la funcion recibe 1 "parametro"
### los valores pasados a los "parametros" se llaman "argumentos"
greet(name)
greet('Juan')
greet('Pedro')
greet()



## Parametros y argumentos

### Parametros por defecto u opcionales
print('\nParametros por defecto u opcionales -------')
### Ubicarlos a la derecha del listado de parametros, es decir, primero al ultimo parametro, luego al penultimo, luego al antepenultimo....etc
def suma (numero_uno, numero_dos=100):   # por defecto el parametro numero_dos tiene un valor, al llamar la funcion lo podemos enviar o no enviar
    print(f'La suma es {numero_uno + numero_dos}')

suma (5, 8)   # si llegan los 2 argumentos se asignan a los parametros
suma (315)    # el segundo argumento es opcional enviarlo, ya que desde la función se le asginó un valor por defecto de 100
#### si en este ejmplo ambos parametros tuvieran valores por defecto podriamos llegar a la llamar a la fucnion sin definir ningun argumento así: "suma()"
suma(numero_dos=15, numero_uno=14) # puedo asignar los argumentos llamando directamente a los parametros, así no usaremos la asignacion por orden, sino directo al parametro




### Argumentos arbitrarios
# para pasar muchos argumentos (puede que ni siquiera conozca la cantidad)
#### *args    (tupla)
print('\nparametros por arbitrarios -- args --')
def promedio (*args):  # denota una tupla() - "args" es un nombre de convension, sirve con cualquier otro nombre
    print(args)
    print(type(args))
    return sum(args) / len(args)

print(promedio(4, 15, 36, 8, 3, 8, 2, 16))  # n cantidad de argumentos y luego se convertirá en una tupla
# esto funciona incluso si incremento la cantidad de argumentos



#### **kwargs    (diccionario)
print('\nparametros por arbitrarios -- kwargs --')
def greeting_kwargs (**personas):   # denota un dict{}
    print(personas)
    print(type(personas))
    for nombre, apellido in personas.items():
        print(f'Hola {nombre}, {apellido}.')

greeting_kwargs(wilson='alzate', francisco='garcia')  # se llama la funcion pasando parametros y definiendo sus valores



## Funciones lambda
### Son funciones anonimas y pequeñas que se definen unsando la palabra clave lambda. Son utiles para operaciones simples y rapidas

sumar = lambda a, b: a + b
print(sumar(3,5))


## Docuemntación de funciones
### Se documenta justo debajo de la deficion de una funcion y se usa docstrings """  -  ''' (tres comillas simples o dobles)

def calcular_descuento (visitas, cantidad):
    """
    Esta funcion define el valor del descuento para la compra actual teniendo en cuenta la frecuencia de visitas y la cantidad de producto que va llevar el cliente
    
    Parametros:
    visitas (int): Cantidad de visitas en el mes
    cantidad (int): Cantidad de producto en la compra actual

    Retorna:
    int: El valor del descuento
    """
    descuento = 0
    # acá se define el bloque de codigo a ejecutar
    return descuento


variable = 0
"""
Esta es un variables
"""



### TODO pydocs ---- averigurar como fnciona la herramienta de documentación