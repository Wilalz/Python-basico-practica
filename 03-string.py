# Trabajando con Strings
## Son un tipo de datos inmutable
texto = ''   # comillas simples
texto2 = ""  # comillas dobles
nombre = 'Felipe'


## Escape de comillas  # usar con "\" back-slash (alt + 92)
comi = 'don\'t give up'
print("comillas: ", comi)


# Formateo de strings
edad = 35
altura = 1.75

## operador %   # es el mas antiguo y menos recomendado hoy en dia
print('\nFormato con % ------------------')
mensaje1 = "Hola, %s. Tienes %d años y mides %f metros de altura" % (nombre, edad, altura)
mensaje1_1 = "Hola, %s. Tienes %d años y mides %.2f metros de altura" % (nombre, edad, altura)
print(mensaje1)
print(mensaje1_1)

# %s: Cadena de texto (string)
# %d: Entero (integer)
# %f: Número de punto flotante (float)
# %e: Número de punto flotante en notación científica (lowercase)
# %c: Carácter (character)

## str.format()  - # mas moderno y flexible que %
print('\nFormato con .format() ------------------')
mensaje2 = "Hola, {}. Tienes {} años y mides {} metros de altura".format(nombre, edad, altura)
mensaje2_1 = "Hola, {0}. Tienes {1} años y mides {2} metros de altura".format(nombre, edad, altura) # usando indices
mensaje2_2 = "Hola, {no}. Tienes {ed} años y mides {al} metros de altura".format(no=nombre, ed=edad, al=altura) # usando variables
print(mensaje2)
print(mensaje2_1)
print(mensaje2_2)


## f-strings   - # Desde Python 3.6, son modernas y las mas recomendadas por su legibilidad y eficiencia
print('\nFormato con f-strings ------------------')
mensaje3 = f"Hola, {nombre}. Tienes {edad} años y mides {altura} metros de altura".format(nombre, edad, altura)
print(mensaje3)
# Metodos de string
## Mayusculas   # usar upper()
print('\nMetodos ----------------')
print(nombre.upper())

## Minusculas   # usar lower()
print(nombre.lower())

## Encontrar la posición (indice) de una letra o cadena   # usar find()
print(nombre.find('p'))   # indice = 4  (recordar que inicia con 0 cero)
print(nombre.find('ana'))   # como no existe muestra -1
print(nombre.find('fel'))   # como no existe muestra -1

## Verificar si una cadeda tiene un texto especifico
print('ipe' in nombre)

## Reemplazar parte de una cadena de texto   # usar replace()
texto_reemplazado = ''
texto_reemplazado = nombre.replace('pe', 'berto')
print(texto_reemplazado)

## Conocer el largo de un texto
print(len(nombre))

## Dividir una cadena en una lista separada por un caracter   # usar split()
nombre_completo = 'Felipe Perez Porras'
dato = 'felipe,perez,15,moto,bi'
print(nombre_completo.split(' '))
print(dato.split(','))




