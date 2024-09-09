# conversor de temperaturas
print('Conversor de temperaturas')

temperatura_inicio = float(input('Ingrese la temperatura a convetir: '))
escala_inicio = input('Ingrese el tipo de escala: (F)Farenheit, (C)Celcius: ')
#escala_objetivo = input('Convertir a: Farenheit(F), Celcius(C)')
temperatura_objetivo = 0

if escala_inicio == 'F' or escala_inicio == 'f':
    temperatura_objetivo = (temperatura_inicio - 32) * (5/9)
    print(f'{temperatura_inicio}°{escala_inicio} son {temperatura_objetivo}°C')
elif escala_inicio == 'C' or escala_inicio == 'c':
    temperatura_objetivo = (temperatura_inicio * (9/5)) + 32
    print(f'{temperatura_inicio}°{escala_inicio} son {temperatura_objetivo}°F')
else:
    print('La escala no es válida')