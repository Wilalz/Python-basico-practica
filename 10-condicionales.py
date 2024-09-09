# Condicionales
## Son bloque de que codigo que se ejecutará siempre que se cumpla una condicion

## if




## if - else



## if - elif - else
name = 'samara'

if name.capitalize() == 'Carmen':
    print('Está dormida')
elif name.capitalize() == 'Samara':
    print('Está dormida')
else:
    print('Está estudiando Python')



## ternarios
edad = 18
mensaje = 'Eres mayor de edad' if edad >=18 else 'Eres menor de edad'
print(mensaje)

### ternario anidado
a = 5
b = 10
resultado = "a es mayor" if a > b else "a es igual a b" if a == b else "a es menor"
print(resultado)
### En el else, se agrega una nueva condicional