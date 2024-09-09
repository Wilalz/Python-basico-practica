# POO - Programacion Orientada a Objetos

## Objeto
### Es la representacion de un objeto real, con caracteristicas y funciones definidas

## Atributos
### se nombran con snake_case
### atributos de instancia, son especificos dentro de cada objeto, se definen dentro del metodo __init__ y se accede a ellos usando "self"

### atributos de clase, son compartidos por todas las instacias de la clase, se definen directamente en la clase y se accede a ellos usando "self"


## Metodos
### Son funciones definidad dentro de una clase y describen los comportamientos de los objetos que se instancien de dicha clase

### de instancia
### de clase
### estaticos

## Clase
### se nombran con CamelCase
### es como un molde para crear objetos

class Persona:
    nombre = ""
    edad = 0
    nacionalidad = ""

    def __init__(self, nombre, edad, nacionalidad):   # siempre que se crea un metodo debe tener el parametro "self" que hace referecia al propio objeto creado
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def presentarse(self):  # los metodos siempre llevan "self"
        return f'Me llamo {self.nombre}, tengo {self.edad} años y soy {self.nacionalidad}.'
    
## Instanciar una clase Persona
persona1 = Persona("Wilson", 35, "colombiano")

persona2 = Persona("Carmen", 30, "mexicana")


print(persona1.presentarse())
print(persona2.presentarse())




## Abstraccion  # Oculta los detalles complejos y muestra solo las características esenciales.


## Encapsulamiento  # Agrupa datos y métodos en una clase.


## Herencia  # Permite crear nuevas clases basadas en clases existentes.


## Polimorfismo  # Permite que diferentes clases sean tratadas como instancias de una clase base común.

