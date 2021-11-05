# Python-basico

## Campos de la tecnología:

- Frontend: Se encarga de llevar el diseño de una aplicación o sitio web a código
- IoT: Se encarga de darle la capacidad de conectarse a internet a elementos que pueden estar a nuestro alrededor.
- IA: Se encarga de enseñarle a la computadora a resolver un determinado problema sin la necesidad de estar involucrados constantemente.
- Backend: Se encarga de crear la lógica con la cual va a funcionar una determinada aplicación y que va a ser almacenada en un servidor.
- DevOps: Se encarga de manejar la información almacenada en la nube de una determinada aplicación.
- Data Science: Se encarga de tomar la información relevante de un determinado ambiente y poder sacar conclusiones al respecto.
- Video juegos: Se encarga de combinar la programación, el diseño y la música para generar grandes experiencias a los usuarios.
- Desarrollo móvil: Se encarga de crear aplicaciones que serán almacenadas en la PlayStore o AppStore, y que podremos hacer uso de ellas desde nuestros smartphones.

## funciones con la clase math

```python
import math

# raiz cuadrada
math.sqrt(4) #2

# PI
math.pi #3.1415926535897931

# funciones trigonométricas
math.sin(180) #-0.8011526357338304

# logaritmos
math.log(20) #2.995732273553991
```

## Variables

Type of variables do not need to be declared
Los tipos de variables no necesitan ser declarados

a = 28 → int
b = 1.5 → float
c = “Hello” → str
d = True → boolean
e = None → NoneType
f = “5” → str (5 y “5” no son lo mismo)

## Los primitivos: tipos de datos sencillos

### Objetos

Un objeto es una forma de modelar el mundo, en los lenguajes de programación se caracterizan por tener métodos y atributos. En python todo es un objeto.

### Tipos de datos

Podemos encontrar cuatros tipo de datos que vienen definidos por defecto en python, a estos tipos de datos los conocemos como primitivos.

- Integers → Números Enteros
- Floats → Números de punto flotantes (decimales)
- Strings → Cadena de caracteres (texto)
- Boolean → Boolenaos (Verdadero o Falso)

### Notas

Algunos operadores aritméticos pueden funcionar para operar con otros tipos de datos, por ejemplo: podemos sumar strings, lo que concatena el texto o multiplicar un entero por un strings lo que repetirá el string las veces que indique el entero

```python
"hola" + " " + "mundo" = "hola mundo"
"hola" * 4 = "holaholaholahola"
```

## Convertir un dato a un tipo diferente

Pasar de un tipo de dato a otro

- `int(var)` variable a entero
- `float(var)` variable a flotante
- `str(var)` variable a texto
- `bool(var)` variable a booleano
- `abs(var)` variable a valor absoluto

Ejemplo:

```python
>>> number1 = input("Escribe un número: ")
Escribe un número: 4
>>> number2 = input("Escribe otro número: ")
Escribe un número: 5
>>> numero1 + numero 2
=> '45' <== Se concatenan
```

Solución:

```python
>>> number1 = int(input("Escribe un numero: "))
Escribe un numero: 100
>>> number2 = int(input("Escribe otro numero: "))
Escribe otro numero: 300
>>> number1 + number2
=> 400
```
