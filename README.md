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

## Operadores lógicos y de comparación

**Operadores Lógicos**

- `and`( y ) -> compara dos valores, y si ambos son verdaderos, devuelve True.
- `or` ( ó ) -> si al comparar dos valores y uno de los dos se cumple, devuelve True. Solo devuelve falso cuando los dos valores no se complen.
- `not` ( no) -> invierte el valor de una variable, dando el valor contrario al de la variable evaluada.

**Operadores de Comparación**

- `==` ( igual qué ) -> Determina si dos valores son iguales o no.
- `!=` (distinto de) -> Determina si dos valores son distintos o no. Si los valores son diferentes devuelve True, si son iguales devuelve False.
- `>` (mayor que) -> Compara dos valores, y determina si es mayor que el otro.
- `<` (menor que) -> Compara dos valores y determina si es menor que el otro.
- `>=` (mayor o igual) -> compara dos valores y determinas si es mayor o igual que el otro.
- `<=` (menor o igual) -> compara dos valores y determinas si es menor o igual que el otro.

## Trabajando con texto: cadenas de caracteres

- .len() = nos ayuda a saber cuantas caracteres tiene mi spring
- .upper() = Todos las letras pasan a estar mayúsculas.
- .capitalize() = La primera letra pasa a estar en mayúscula.
- .lower() = se transforma todo a minúsculas.
- .strip() = Elimina los espacios basura al inicio como al final.
- .replace() = remplaza las letras. si nuestra variable nombre contiene Antonio
- **nombre.replace(“i”, “o” ) ** (En este paso cambiará todas las letras “i” en “o”) así que el resultado sería Antonoo.
- texto[1] → indica la letra seleccionada

**IMPORTANTE**
Al hacerlo de la forma anterior solo cambiará la forma en que nos imprime el texto, si queremos cambiar la variable deberemos poner primero el nombre de la variable y la función ej:

```python
nombre = nombre.upper()
nombre = nombre.capitalize()
nombre = nombre.lower()
nombre = nombre.strip()
nombre = nombre.replace()
```

Si ejecutamos:

```python
dir(variable)
```

Obtendremos todos los métodos disponibles para ejecutar de un objeto, variable o tipo de dato.

y si ejecutamos:

```python
help(variable)
```

Nos entregará la documentación disponible para esa variable.
