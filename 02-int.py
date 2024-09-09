# Metodos de integers
a = 8
b = 5

## aritmetricas
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # division siempre da un float
print(a // b) # division arroja un entero sin decimales
print(a ** b) # potenciacion
print(a % b)  # modulo -> es el sobrante de la division


# Division
## integer division is defined to round towards minus infinity
## 7 // 3 is 2, but (−7) // 3 is −3
a = -7
b = 3
print(a // b)
print(b * a // b)

# Division / da un float, division con // da un int redondeado al entero mas cercano HACIA ABAJO
div = 3/3
div2 = 7//3
divNegativo = -7//3

print("div / :" , div)
print("div // :", div2)
print("div Negativo // :", divNegativo)


## Calcular el valor absoluto de un numero
print(abs(5))
print(abs(-5))