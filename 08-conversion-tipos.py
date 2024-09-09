# Conversion entre tipos de datos
print('----- Conversion entre tipos ------')

## Convertir a integer   # usar int()
num_str = '123'
print(f'num_str {num_str} es {type(num_str)}')
strToInt = int(num_str)
print(f'strToInt {strToInt} es {type(strToInt)}')
print(f'float a integer {int(123.45)} es {type(int(123.45))}') # elimina los decimales

## Convertir a float   # usar float()
intToFloat = float(strToInt)
print(f'intToFloat {intToFloat} es {type(intToFloat)}')

## Convertir a String   # usar str()
intToStr = str(strToInt)
print(f'intToStr {intToStr} es {type(intToStr)}')
print(f'float a string {str(123.45)} es {type(str(123.45))}')


## Convertir de List a String   # usar .join(<list>)
abc_list = ['a', 'b', 'c']
listToString = ''.join(abc_list)
print('listToString:', abc_list, 'is:', listToString)

## Convertir a list   # usar list()
name = 'Wilson'
stringToList = list(name)
print(f'stringToList es {stringToList}')

tuplaToList = list(name)
print(f'tuplaToList es {tuplaToList}')


# Convertir a tupla
name = 'Wilson'
stringToTupla = tuple(name)
print(f'stringToTupla es {stringToTupla}')

nameList = ['W', 'i', 'l', 's', 'o', 'n']
listToTupla = tuple(nameList)
print(f'listToTupla es {listToTupla}')


## Convertir a booleano
print(bool('hola')) # Evalua True, es decir hay texto

### Solo 4 opciones evaluan False
### Un booleano que sea False
### El numero 0 cero
### Un string vacio
### Un objeto None
print(bool(False))
print(bool(0))
print(bool(''))
print(bool(None))