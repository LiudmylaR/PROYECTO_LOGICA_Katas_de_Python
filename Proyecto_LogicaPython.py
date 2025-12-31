#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no son considerados.

def contar_frecuencias(texto):

    """
    Calcula la frequencia de cada letra en una cadena de texto.

    Args:
        texto (str): cadena de texto que se analiza.

    Return:
        dict: Un diccionario donde las claves son las letras y 
        los valores son la cantidad de veces que aparece cada letra. 
        Los espacios no se tienen en cuenta.
    """

    # Creamos in diccuonario vacío
    frecuencias = {}
    # Convertimos el texto a minúsculas
    texto = texto.lower()
    for caracter in texto:
        # Ignoramos los espacios
        if caracter != " ":
            # Si el carácter ya está en el diccionario, sumamos 1
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            # Si no está, lo inicializamos en 1
            else:
                frecuencias[caracter] = 1
    return frecuencias


# In[9]:


# 1. Ejemplo de uso:

texto = "Ciudad Oviedo"

resultado = contar_frecuencias(texto)
print (resultado)


# In[10]:


# 2. Dada una lista de números, obtenemos una nueva lista con el doble de cada valor. Usamos la función map()

def dobles_lista(numeros):

    """
    Devuelve una lista con el doble de cada número de la lista dada.

    Args:
        numeros (list): Lista de números (int o float) que se duplican.

    Return:
        list: Una nueva lista donde cada elemento es el doble del valor
          correspondiente en la lista dada.
    """

    # Función 'map()' devuelve un iterador, por lo que lo convertimos a lista con función 'list()'
    return list(map(lambda x:x*2, numeros))


# In[29]:


# 2. Ejemplo de uso:

numeros = [1,2,3,4,5,6,7,8,9]

dobles = dobles_lista(numeros)
print(dobles)


# In[12]:


# 3. Una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función devuelve una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def contener_palabra(lista_palabras, objetivo):

    """
    Devuelve una lista con todas las palabras que contienen la palabra objetivo.

    Args:
        lista_palabras (list): Lista de palabras.
        objetivo (str): Palabra que se quiere buscar dentro de cada elemento.

    Return:
        list: Lista de palabras que contienen la palabra objetivo.
    """

    return [palabra for palabra in lista_palabras if objetivo in palabra]


# In[28]:


# 3. Ejemplo de uso:

lista_palabras = ["montaña", "girasol", "soldado", "jupiter", "soledad", "oceano"]

resultado = contener_palabra(lista_palabras, "sol")
print(resultado)


# In[25]:


# 4. Función que calcule la diferencia entre los valores de dos listas. Usamos la función map()

def diferencia_listas(lista1, lista2):

    """
    Calcula la diferencia entre los valores de dos listas numero a numero.

    Args:
        lista1 (list): Lista de valores Nº1
        lista2 (list): Lista de valores Nº2

    Returns:
        list: Lista con la diferencia entre los elementos correspondientes de ambas listas (deben tener la misma cantidad de valores).
    """

    return list(map(lambda x,y:x-y, lista1, lista2))


# In[27]:


# 4. Ejemplo de uso:

lista_x = [10, 15, 23, 25, 70]
lista_y = [3, 17, 20, 24, 64]

resultado = diferencia_listas(lista_x, lista_y)
print (resultado)


# In[31]:


# 5. Función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". 
# La función debe devolver una tupla que contenga la media y el estado.

def calcular_notas_medias (notas, nota_aprobado = 5):
    """
    Calcula la media de una lista y determina si está aprobado.

    Args:
        notas (list): Lista de números (int o float).
        nota_aprobado (int, float, optional): Nota mínima para aprobar. Por defecto es 5.

    Returns:
        tuple: Una tupla con dos elementos:
            media (float): La media de las notas.
            estado (str): "aprobado" si la media es mayor o igual que nota_aprobado, en caso contrario "suspenso".
    """

    # Calculamos la media de las notas
    media = sum(notas)/len(notas)

    # Determinamos el estado
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    # Devolver la media y el estado en una tupla
    return (media, estado)


# In[36]:


# 5. Ejemplo de uso:

notas = [5, 10, 7, 4 ,5]

resultado = calcular_notas_medias(notas)
print (resultado)


# In[50]:


# 6. Función que calcule el factorial de un número de manera recursiva.

def factorial(n):

    """
    Calcula el factorial de un número de forma recursiva.
    Factorial se define como:
    n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
    Por definición !0 = 1; !1 = 1; no está definido para números negativos

    Args:
        n (int): Número entero no negativo

    Returns:
        int: Factorial de número n
    """

    if n < 0:
        return "Factorial no está definido para numeros negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# In[51]:


# 6. Ejemplo de uso:

print (factorial(4))


# In[56]:


# 7. Función que convierta una lista de tuplas a una lista de strings. Usamos la función map()

def convertir_lista (lista_tuplas):

    """
    Convierte una lista de tuplas en una lista de cadenas de texto.

    Args:
        lista_tuplas (list): Lista de tuplas cuyos elementos se convierten a string.

    Returns:
        list: Lista de cadenas de texto generados de las tuplas.
    """

    # Usamos map() para procesar cada tupla.
    # Dentro, usamos otro map() para asegurar que cada elemento de la tupla sea str
    # Unimos con el separador " ".

    return list(map(lambda t:" ".join(map(str,t)), lista_tuplas))


# In[60]:


# 7. Ejemplo de uso:

l_tuplas = [("senior", "Fernando"), ("seniora", "Lucía"), ("señorito", "Marcos")]

print (convertir_lista(l_tuplas))


# In[66]:


# 8. Programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando 
# si la división fue exitosa o no.

while True:

    """
    Programa que pide al usuario dos números y realiza su división.
    El programa se repite hasta que el usuario introduce valores correctos.
    Maneja errores por valores no numéricos y división entre cero.
    """

    try:
        # Pedimos introducir los numeros
        numero1 = float(input("Intriducir el primer número:"))
        numero2 = float(input("Introducir el segundo número:"))

        # Realizamos la división
        resultado = numero1/numero2

        # Mostramos resuldado si división fue exitosa
        print("La división fue exitosa. Resultado:", resultado)

        # Salimos de bucle si división fue exitosa
        break

    except ValueError:
        # Error cuando introducen valores no numericos
        print("La división no fue exitosa. Error: Introducir solo valores numericos")

    except ZeroDivisionError:
        # Error cuando se intenta dividir entre cero
        print("La división no fue exitosa. Error: No es posible dividir entre cero")


# In[72]:


# 9. Función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"]. Usamos la función filter()

def filtrar_mascotas(lista_mascotas):

    """
    Filtra una lista de mascotas excluyendo las que estan prohibidas en España, devuelve una nueva lista.
    Lista de mascotas prohibidas: ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    Args:
        lista_mascotas (list): Lista de mascotas (str).

    Returns:
        list: Lista de mascotas permitidas.
    """

    lista_proibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    # La función lambda devuelve True si la mascota no está en la lista_proibidas.
    # La función filter() conserva los elementos que devuelven True.
    # Convertimos el objeto de filter a una lista con list().
    return list(filter(lambda mascota:mascota not in lista_proibidas, lista_mascotas))


# In[73]:


# 9. Ejemplo de uso:

mascotas = ["Gato", "Cobaya", "Tortuga", "Cocodrilo", "Perro", "Tigre"]

resultado = filtrar_mascotas(mascotas)
print(resultado)


# In[83]:


# 10. Función que reciba una lista de números y calcule su promedio. 
# Si la lista está vacía, lanzamos una excepción personalizada y manejamos el error adecuadamente.

class ListaVaciaError(Exception):
    """ Excepción lanzada cuando la lista de números no tiene elementos"""
    pass

def calcular_promedio(lista_numeros):

    """
    Calcula el promedio de una lista de números.
    Si la lista está vacía, lanza y maneja una excepción personalizada mostrando un mensaje de error.

    Args:
        lista_numeros (list): Lista de números (int o float).

    Returns:
        float|None: Promedio de los números si la lista no está vacía. Devuelve el mensaje de error si la lista está vacía.
    """

    try:
        if not lista_numeros:
            raise ListaVaciaError
        return sum(lista_numeros)/len(lista_numeros)
    except ListaVaciaError:
        print("Error: Lista está vacía")


# In[84]:


# 10. Ejemplo de uso:

numeros = []

resultado = calcular_promedio(numeros)
print(resultado)


# In[ ]:


# 11. Programa que pida al usuario que introduzca su edad. 
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), 
# manejamos las excepciones adecuadamente.

class EdadFueraRango(Exception):
    """Se produce una excepción cuando la edad no está entre 0 y 120."""
    pass

def pedir_edad():

    """
    Programa que solicita al usuario su edad y valida la entrada.
    Comprueba que la edad introducida sea un número entero y que esté dentro del rango válido (entre 0 y 120).
    Maneja errores por valores no numéricos y valores fuera de rango. 
    """

    while True:
        try:
            # Intentamos convertir la entrada a un número entero
            edad = int(input("Introduce tu edad como un numero entero (0-120):"))

            # Comprobamos si está dentro del rango
            if edad <0 or edad > 120:
                raise EdadFueraRango(f"La edad {edad} está fuera del rango")

            # Si la edad es válida
            print("La edad introducida correctamente", edad)
            break

        except ValueError: 
            # Se activa si el usuario escribe valores no numericos
            print ("Error: Introduce un número entero")

        except EdadFueraRango:
            # Se activa si el número no está entre 0 y 120
            print("Error: Introduce edad válida entre 0 y 120")


# In[96]:


# 11. Ejemplo de uso:

pedir_edad()


# In[112]:


# 12. Función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):

    """
    Devuelve una lista con la longitud de cada palabra de una frase.

    Args:
        frase (str): Frase de entrada.

    Returns:
        list: Lista con la longitud de cada palabra.
    """

    # Dividimos la frase en una lista de palabras.
    palabras = frase.split()
    # Usamos map para aplicar la función len a cada elemento y convertimos el resultado en una lista.
    return list(map(len,palabras))


# In[113]:


# 12. Ejemplo de uso:

frase1 = "El código funciona genial"

print(longitud_palabras(frase1))


# In[132]:


# 13. Función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
# Las letras no pueden estar repetidas. Usamos la función map().

def lista_letras_M_m(caracteres):

    """
    Genera una lista de tuplas con cada letra en mayúsculas y minúsculas, sin repetir letras.

    Args:
        caracteres (str): Conjunto de caracteres.

    Returns:
        list: Lista de tuplas con las letras (mayúscula, minúscula).
    """

    # Convertimos a set para eliminar duplicados automáticamente ignorando mayúsculas/minúsculas.
    caracteres_unicos = set(caracteres.lower())

    # Transformamos cada carácter en una tupla. La función lambda toma 'c' y devuelve (C, c).
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))


# In[133]:


# 13. Ejemplo de uso:

caracteres_entrada = "FgdhtfpdlH"

print(lista_letras_M_m(caracteres_entrada))


# In[139]:


# 14. Función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usamos la función filter()

def filtrar_palabras(lista_palabras, letra):

    """
    Devuelve las palabras de una lista que comienzan con una letra específica.

    Args:
        lista_palabras (list): Lista de palabras (str).
        letra (str): Letra con la que deben comenzar las palabras.

    Returns:
        list: Lista de palabras que comienzan con la letra indicada.
    """

    # Aseguramos que la letra esté en minúscula para la comparación
    letra = letra.lower()

    # Usamos filter para seleccionar las palabras (en minúsculas) que empiezan con la letra. 
    return list(filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras))


# In[142]:


# 14. Ejemplo de uso:

lista_p = ["carne", "Pescado", "Fruta", "Verdura", "postre"]

print(filtrar_palabras(lista_p, "p"))


# In[ ]:


# 15. Función lambda que sume 3 a cada número de una lista dada.

def suma_tres(lista_numeros):

    """
    Función que suma 3 a cada número de una lista.

    Args:
        lista_numeros (list): Lista de números (int o float).

    Returns:
        list: Nueva lista con cada número incrementado en 3.
    """

    return list(map(lambda x: x+3, lista_numeros))


# In[ ]:


# 15. Ejemplo de uso:

numeros = [1,2,3,4,5]

resultado = suma_tres(numeros)
print(resultado)


# In[155]:


# 16. Función que tome una cadena de texto y un número entero n como parámetros y devuelva 
# una lista de todas las palabras que sean más largas que n. Usa la función filter()

def filtro_palabras_largas(texto, n):

    """
    Filtra las palabras de un texto que tienen una longitud mayor a n.

    Args:
        texto (str): Cadena de texto de entrada.
        n (int): Longitud mínima que deben superar las palabras.

    Returns:
        list: Lista de palabras que superan los n caracteres.
    """

    # Convertimos el string en una lista de palabras
    palabras_separadas = texto.split()

    # Usamos filter para quedarnos solo con las que cumplen len > n
    # La lambda toma cada palabra y verifica su longitud
    return list(filter(lambda palabra: len(palabra)>n, palabras_separadas))


# In[ ]:


# 16. Ejemplo de uso:

text = "La Navidad es la mejor fiesta del año"

print(filtro_palabras_largas(text,4))


# In[165]:


# 17. Función que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usamos la función reduce()

from functools import reduce

def convertir_numero(lista_digitos):

    """
    Convierte una lista de dígitos en un número entero único.

    Args:
        lista_digitos (list): Lista de dígitos enteros (0 - 9).

    Returns:
        int: Número formado de los dígitos.
    """
    # La función lambda toma el acumulado 'acum' y el siguiente número 'n'.
    # [5, 7, 2] convierte en: ((5 * 10) + 7) = 57 ; ((57 * 10) + 2) = 572.

    return reduce(lambda acum, n: acum*10 + n , lista_digitos)


# In[166]:


# 17. Ejemplo de uso:

digitos = [2, 0, 2, 6]

resultado = convertir_numero(digitos)
print(f"La lista {digitos} se convierte al número: {resultado}")


# In[38]:


# 18. programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter() para extraer a los estudiantes con una calificación mayor o igual a 90.

def gestionar_estudiantes():

    """
    Programa que crea una lista de diccionarios con información de estudiantes 
    y filtra aquellos cuya calificación es mayor o igual a 90.
    """

    # PASO 1: Podemos usar una lista de tuplas con datos para crear los diccionarios
    datos_estudiantes = [
        ("Lucía", 22, 75),
        ("Fernando", 24, 91),
        ("Manuel", 20, 95), 
        ("Darío", 21, 87),
        ("Laura", 25, 92) 
    ]

    # Creamos la lista de diccionarios con la información de los estudiantes usando una comprensión de lista
    estudiantes = [{'nombre': n, 'edad': e, 'calificacion': c} for n, e, c in datos_estudiantes]
    print(f"--La lista creada con la informacion de {len(estudiantes)} estudiantes--")

    # PASO 2: Filtramos los que tienen calificación >= 90. 
    estudiantes_filtrados = list(filter(lambda e: e['calificacion'] >= 90, estudiantes))
    return estudiantes_filtrados


# In[40]:


# 18. Ejemplo de uso:

resultado = gestionar_estudiantes()
print("Estudiantes con calificación mayor o igual a 90:")
print(resultado)


# In[64]:


# 19. Función lambda que filtre los números impares de una lista dada.

def filtrar_impares(lista_numeros):
    """
    Filtra los números impares de una lista dada y devuelve una nueva lista.

    Args:
        lista_numeros (list): Una lista que contiene números (int o float) que se desea procesar.

    Returns:
        list: Una nueva lista que contiene únicamente los números impares extraídos de la lista original
    """

    # Aplicamos filter con la función lambda.
    # La condición x % 2 != 0 devuelve True si el número es impar.
    # Función list() convierte el resultado en una lista.
    lista_impares = list(filter(lambda x: x % 2 != 0, lista_numeros))

    return lista_impares


# In[66]:


# 19. Ejemplo de uso:

lista_dada = [1,2,3,4,5,6,7,8,9,10,11,12]

impares = filtrar_impares(lista_dada)
print("Lista de números original:", lista_dada)
print("Números impares:", impares)


# In[79]:


# 20. Para una lista con elementos tipo integer y string obtenemos una nueva lista sólo con los valores int. Usamos la función filter()

def filtrar_enteros(lista_mix):

    """
    Filtra una lista y extrae solo los elementos que son enteros.

    Args:
        lista_mix (list): Lista con elementos de tipo int y str.

    Returns:
        list: Una lista que contiene únicamente los elementos de tipo integer
    """

    # Función lambda que devuelve True si el elemento x es de tipo entero.
    # Filtramos una lista con filter() para obtener solo los elementos que sean de tipo int
    return list(filter(lambda x: type(x) == int, lista_mix))


# In[80]:


# 20. Ejemplo de uso:

lista = [5, 2.3, 8, "oso", 56, 86.23, "Lola" ]

resultado = filtrar_enteros(lista)
print("Los elementos de tipo 'int' encontrados:",resultado)


# In[87]:


# 21. Función que calcule el cubo de un número dado mediante una función lambda.

# Definimos la función lambda y la asignamos a una variable:
calcular_cubo = lambda x: x**3

# Ejemplo de uso:

x = 5
resultado = calcular_cubo(x)
print(f"El cubo de {x} es: {resultado}")


# In[108]:


# 22. Dada una lista numérica, obtenemos el producto total de los valores de dicha lista. Usamos la función reduce() .

def producto_total(numeros):

    """
     Calcula el producto total de los valores de una lista numérica.

     Args:
        lista_numeros (list): Una lista de números (int y float).
    Returns:
        int|float: El resultado de multiplicar todos los elementos entre sí.
    """

    return reduce(lambda x, y: x * y, numeros)


# In[109]:


# 22. Ejemplo de uso:

lista_num = [1, 2, 3, 4, 5.5]
print (producto_total(lista_num))


# In[110]:


# 23. Concatenamos una lista de palabras. Usamos la función reduce().

def concatenar_palabras(palabras):
    """
    Concatena una lista de strings en una cadena de texto.

    Args:
        palabras (list): Una lista que contiene las palabras (str) a unir.

    Returns:
        str: Cadena resultante de concatenar todas las palabras.
    """

    return reduce(lambda a, b: a + " " + b, palabras)


# In[112]:


# 23. Ejemplo de uso:

lista_palabras = ["En", "invierno", "hace", "frio", "y", "cae", "nieve"]
print(concatenar_palabras(lista_palabras))


# In[116]:


# 24. Calculamos la diferencia total en los valores de una lista. Usamos la función reduce().

def diferencia_total(valores):

    """
    Calcula la resta acumulada de todos los elementos de una lista.

    Args:
        valores (list): Una lista de números (int o float)

    Returns:
        int|float: Resultado de la resta acumulativa.
    """

    return reduce(lambda a, b: a - b, valores)


# In[117]:


# 24. Ejemplo de uso:

lista_valores = [1000, 100, 10, 1]

print(diferencia_total(lista_valores))


# In[118]:


# 25. Función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):

    """
    Cuenta el número de caracteres en una cadena de texto.

    Args:
        texto (str): El texto que se desea medir.

    Returns:
        int: El número total de caracteres (incluyendo espacios y símbolos).
    """

    return len(texto)


# In[119]:


# 25. Ejemplo de uso:

text = "Me encanta Navidad"

print(contar_caracteres(text))


# In[4]:


# 26. Función lambda que calcule el resto de la división entre dos números dados.

# Definimos la función lambda con dos argumentos: el dividendo (a) y el divisor (b)
resto_division = lambda a, b: a % b


# In[6]:


# 26. Ejemplo de uso:

print (resto_division(15, 4))


# In[20]:


# 27. Función que calcule el promedio de una lista de números.

def promedio(lista_numeros):

    """
    Calcula el promedio de una lista de números.

    Args:
        lista_numeros (list): Lista de números (int o float).

    Returns:
        float: Promedio de los números de la lista.
    """

    return sum(lista_numeros)/len(lista_numeros)


# In[21]:


# 27. Ejemplo de uso:

mis_numeros = [2,5,6,7,9]

mi_promedio = promedio(mis_numeros)
print(f"El promedio de los números {mis_numeros} es: {mi_promedio}")


# In[26]:


# 28. Función que busque y devuelva el primer elemento duplicado en una lista dada.

def encontrar_primer_duplicado(lista):

    """
    Busca y devuelve el primer elemento que aparece más de una vez en la lista.

    Args:
        lista (list): Una lista de elementos (números, strings, etc.)

    Returns:
        any: El primer elemento duplicado encontrado
        None: Si no hay elementos duplicados.
    """

    elementos_vistos = set()

    for elemento in lista:

        # Si el elemento ya está en el conjunto, es el primer duplicado:
        if elemento in elementos_vistos:
            return elemento

        # Si no, lo añadimos al conjunto de "elementos_vistos"
        elementos_vistos.add(elemento)

    # Si terminamos el bucle sin retornar, no hay duplicados
    return None


# In[27]:


# 28. Ejemplo de uso:

mi_lista = [5, "gato", 10, 25.5, "perro", 10, "gato"]

print(encontrar_primer_duplicado(mi_lista))


# In[43]:


# 29. Función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', 
# excepto los últimos cuatro.

def enmascarar_datos(variable):

    """
    Convierte una variable a texto y enmascara todos los caracteres 
    con '#' excepto los últimos cuatro.

    Args:
        variable: El dato de entrada (int, str, etc.).

    Returns:
        str: La cadena enmascarada.
    """

    # Paso 1. Convertimos la entrada a cadena de texto
    cadena = str(variable)
    longitud = len(cadena)

    # Paso 2. Si tiene 4 caracteres o menos, no hay nada que enmascarar
    if longitud <= 4:
        return cadena

    # Paso 3. Creamos la máscara: '#' repetido (longitud - 4) veces
    mascara = "#" * (longitud - 4)

    # Paso 4. Concatenamos con los últimos 4 caracteres
    ultimos_cuatro = cadena[-4: ]

    return mascara + ultimos_cuatro


# In[44]:


# 29. Ejemplo de uso:

print(enmascarar_datos(1234567890123432))
print(enmascarar_datos("AABBCCDDEEFF"))
print(enmascarar_datos("Mar"))


# In[55]:


# 30. Función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def es_anagrama(palabra1, palabra2):

    """
    Determina si dos palabras son anagramas.
    Dos palabras son anagramas si usan las mismas letras, pero colocadas en un orden diferente.

    Args:
        palabra1 (str): Primera palabra.
        palabra2 (str): Segunda palabra.

    Returns:
        bool: Devuelve True si son anagramas, False en caso contrario.
    """

    # Comprobamos si tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False

    # Pasamos todas las letras a minúsculas y comparamos las versiones ordenadas
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


# In[56]:


# 30. Ejemplo de uso:

print(es_anagrama("Saco", "Cosa"))
print(es_anagrama("Cola", "Lola"))
print(es_anagrama("Mila", "Milano"))


# In[76]:


# 31. Función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. 
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def gestionar_nombres():

    """
    Solicita al usuario una lista de nombres y un nombre a buscar.
    Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado.
    Si no está, lanza una excepción.

    Raises:
        ValueError: Se lanza cuando el nombre buscado no se encuentra en la lista.
    """

    # PASO 1. Pedimos la lista de nombres de entrada
    entrada = input("Escribe los nombres separados por coma: ")

    # PASO 2. Convertimos la cadena de texto de entrada en una lista, 
    # eliminando espacios extra en cada nombre y separando cada elemento por coma
    lista_nombres = [nombre.strip() for nombre in entrada.split(",")]

    # PASO 3. Pedimos el nombre que queremos encontrar
    busqueda = input("Que nombre buscas?").strip()

    # PASO 4. Comprobamos si está en la lista de entrada
    if busqueda in lista_nombres:
        print(f"El nombre {busqueda} encontrado!")

    # Si no está, lanzamos una excepción
    else:
        raise ValueError(f"El nombre {busqueda} no se encuentra en la lista.")



# In[80]:


# 31. Ejemplo de uso:

try:
    gestionar_nombres()
except ValueError as e:
    print(e)


# In[99]:


# 32. Función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve
# el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def obtener_puesto(nombre_completo, lista_empleados):
    """
    Busca el nombre completo de empleado en una lista de diccionarios y devuelve el puesto.

    Args:
        nombre_completo (str): Nombre completo del empleado a buscar.
        lista_empleados (list): Lista de diccionarios con la información de los empleados.
                            Cada diccionario debe contener las claves 'nombre' y 'puesto'.

    Returns:
        str: Puesto del empleado si está en la lista,
         o un mensaje indicando que la persona no trabaja aquí.
    """

    # Recorremos la lista de empleados uno por uno
    for empleado in lista_empleados:

        # Comprobamos si el nombre del empleado coincide con el nombre buscado
        if empleado["nombre"] == nombre_completo:

            # Si coincide, devolvemos el puesto del empleado
            return empleado["puesto"]

    # Si termina el bucle y no encontró nada devolvemos un mensaje  
    return "La persona no trabaja aquí."


# In[100]:


# 32. Ejemplo de uso:

empleados = [
    {"nombre": "Iván Álvarez", "puesto": "Gerente"},
    {"nombre": "María López", "puesto": "Administrativa"},
    {"nombre": "Juan Cardín", "puesto": "Diseñador"},
    {"nombre": "Pablo García", "puesto": "Analista"}
]

nombre = "Juan Cardín"
puesto = obtener_puesto(nombre, empleados)

print(puesto)


# In[ ]:


# 33. Función lambda que sume elementos correspondientes de dos listas dadas.

# Definimos la lambda que utiliza map para iterar sobre ambas listas a la vez
suma_listas = lambda lista1, lista2: list(map(lambda a,b: a + b, lista1, lista2))

# Ejemplo de uso:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(suma_listas(lista1, lista2))


# In[126]:


# 34. La clase Arbol , define un árbol genérico con un tronco y ramas como atributos.

class Arbol:

    def __init__(self):

        """ Inicializa un árbol con un tronco de longitud 1 y una lista vacía de ramas."""

        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):

        """ Aumenta la longitud del tronco en una unidad."""

        self.tronco +=1

    def nueva_rama(self):

        """ Agrega una nueva rama de longitud 1 a la lista de ramas."""

        self.ramas.append(1)

    def crecer_ramas(self):

        """ Aumenta en una unidad la longitud de todas las ramas existentes."""

        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):

        """ Elimina rama en una posición específica (ajustado a índice 0).
        Args:
            posicion (int): Índice de la rama a eliminar   
        """

        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print(f"No existe una rama en la posición {posicion}.")

    def info_arbol(self):

        """ 
        Devuelve información sobre el árbol.

        Returns:
            str: Información detallada del tronco y las ramas.
        """

        return {
            "Longitud del tronco": self.tronco,
            "Número de las ramas": len(self.ramas),
            "Longitud de las ramas": self.ramas
        }


# In[127]:


    # 34. Ejemplo de uso:

# 1. Crear un árbol.
mi_arbol = Arbol()

# 2. Hacer crecer el tronco una unidad.
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol.
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad.
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol.
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2.
# La posición 2 se refiere al índice 2 (la tercera rama).
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol.
resultado = mi_arbol.info_arbol()

print("Información del árbol:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")


# In[ ]:


# 36. La clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        """ 
        Inicializa un usuario del banco con su nombre, saldo y si tiene o no cuenta corriente.

        Args:
            nombre (str): Nombre del usuario.
            saldo (float|int): Saldo inicial del usuario.
            cuenta_corriente (bool): Indica si tiene cuenta corriente.
        """

        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """
        Retira una cantidad de dinero del saldo del usuario.

        Args:
            cantidad (float|int): Cantidad de dinero a retirar.

        Raises:
            ValueError: Se lanza si el usuario no tiene cuenta corriente
            ValueError: Se lanza si el saldo es insuficiente.
        """

        if not self.cuenta_corriente:
            raise ValueError("El usuario no tiene cuenta corriente")

        if cantidad > self.saldo:
            raise ValueError("El usuario no tiene saldo suficiente")

        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Realiza transferencia desde otro_usuario al usuario actual

        Args:
            otro_usuario (UsuarioBanco): Usuario que envía el dinero.
            cantidad (float|int): Cantidad a transferir.

        Raises:
            ValueError: Se lanza si el usuario remitente no tiene cuenta corriente
            ValueError: Se lanza si el saldo del usuario remitente es insuficiente.
        """

        if not otro_usuario.cuenta_corriente:
            raise ValueError("Error en transferencia. El usuario remitente no tiene cuenta corriente")

        if cantidad > otro_usuario.saldo:
            raise ValueError("Error en transferencia. El usuario remitente tiene saldo insuficiente")

        # Se retira el dinero del otro usuario
        otro_usuario.saldo -= cantidad
        # Se añade el dinero al usuario actual
        self.saldo += cantidad
        print("Transferencia completada con éxito.")

    def agregar_dinero(self, cantidad):
        """
        Agrega el dinero al saldo del usuario.

        Args:
            cantidad (float|int): Cantidad a agregar
        """

        self.saldo += cantidad


# In[189]:


    # 36. Ejemplo de uso:

# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo de "Bob".

bob.agregar_dinero(20)  # Bob ahora tiene 70

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".

try:
    alicia.transferir_dinero(bob, 80)  # Lanzará un ValueError porque Bob solo tiene 70
except ValueError as e:
    print(e)

# 4. Retirar 50 unidades de saldo a "Alicia".

try:
    alicia.retirar_dinero(50)

except ValueError as e:
    print(e)

# Imprimimos saldos finales de los usuarios

print("Saldo de Alicia:", alicia.saldo)
print("Saldo de Bob:", bob.saldo)


# In[216]:


# 37.  Función llamada 'procesar_texto' que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . 
# Estas opciones son otras funciones que definimos primero y llamamos dentro de la función 'procesar_texto'.

    # 1. Función para contar palabras

def contar_palabras(texto):
    """
    Cuenta frecuencia cada palabra en el texto.

    Args:
        texto (str): Texto de entrada

    Returns:
        dict: Diccionario con las palabras como claves y sus frecuencias como valores.
    """
    # Convertimos el texto a minúsculas y lo dividimos en palabras:
    palabras = texto.lower().split()
    # Creamos un diccionario vacío para guardar la frecuencia de cada palabra:
    frecuencia = {}
    # Para cada palabra de la lista:
    for palabra in palabras:
        # Si la palabra ya existe en el diccionario, sumamos 1
        # Si no existe, empezamos el conteo en 0 y sumamos 1
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


    # 2. Función para reemplazar palabras

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza una palabra por otra en el texto.

    Args:
        texto (str): Texto de entrada.
        palabra_original (str): Palabra a reemplazar.
        palabra_nueva (str): Nueva palabra.

    Returns:
        str: Texto con la palabra reemplazada.
    """
    return texto.replace(palabra_original, palabra_nueva)


    # 3. Función para eliminar una palabra

def eliminar_palabra(texto, palabra_eliminar):
    """
    Elimina una palabra del texto.

    Args:
        texto (str): Texto de entrada.
        palabra_eliminar (str): Palabra a eliminar.

    Returns:
        str: Texto sin la palabra eliminada.
    """

    # Dividimos el texto en palabras:
    palabras = texto.split()
    # Filtramos las palabras que no sean la que queremos eliminar:
    filtracion = [p for p in palabras if p != palabra_eliminar]
    # Convertimos la lista de palabras en un texto separado por espacios:
    return " ".join(filtracion)


    # 4. Función principal: procesar texto

def procesar_texto(texto, opcion, *args):
    """
    Procesa un texto según la opción indicada.

    Args:
        texto (str): Texto a procesar.
        opcion (str): Opcion para procesar 
        args (str): Argumentos según la opción.

    Returns:
        dict|str: Resultado del procesamiento.
    """

    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])

    else:
        return "Opción no válida"


# In[217]:


    # 37. Ejemplo de uso:

mi_texto = "Los reyes traen muchos regalos para los padres"

# 1. Contar palabras:
print(procesar_texto(mi_texto, "contar"))

# 2. Reemplazar palabra:
print(procesar_texto(mi_texto, "reemplazar", "padres", "niños"))

# 3. Eliminar palabra:
print(procesar_texto(mi_texto, "eliminar", "muchos"))


# In[238]:


# 38. Programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def evaluar_periodo_dia(hora):
    """
    Determina si es de noche, de día o tarde según la hora proporcionada.

    Args:
        hora (int): La hora del día en formato de 24 horas.

    Returns:
        str: El periodo del día (noche, día o tarde).
    """

    # Comprobamos que la hora sea un número entre 0 y 24
    if hora < 0 or hora > 24:
        return "Hora no válida. Por favor, introduce un número entre 0 y 24."
    # Determinamos rango de día: 6:00 a 12:59
    if 6 <= hora <= 12:
        return "Es de día."
    # Determinamos rango de tarde: 13:00 a 20:59
    elif 13 <= hora <= 20:
        return "Es tarde."
    # El resto es noche: 21:00 a 5:59
    else:
        return "Es de noche."


# In[243]:


# 38. Ejemplo de uso:

try:
    # Pedimos al usuario introducir la hora:
    entrada = int(input("Introduce la hora actual en formato 24 horas:"))

    # Llamamos a la función que evalua el periodo del día
    resultado = evaluar_periodo_dia(entrada)
    print(resultado)

except ValueError:
    print("Error: Por favor, introduce solo números enteros.")


# In[257]:


# 39. Programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

def obtener_calificacion(nota):
    """
    Determina la calificación en texto de un alumno basada en su calificación numérica.

    Args:
        nota (float): La nota del alumno (0-100).

    Returns:
        str: La calificación en texto.
    """

    # Comprobamos el rango:
    if nota < 0 or nota > 100:
        return "Nota no válida. Debe estar entre 0 y 100"

    # Determinamos la calificación:
    if nota <= 69:
        return "Insuficiente"
    elif nota <= 79:
        return "Bien"
    elif nota <= 89:
        return "Muy bien"
    else:
        return "Excelente"


# In[258]:


# 39. Ejemplo de uso:

try:
    # Pedimos introducir la nota:
    entrada = float(input("Introduce la nota numérica del alumno (de 0 a 100):"))
    # LLamamos a la función que determina la calificación:
    resultado = obtener_calificacion(entrada)
    print("La calificación es:", resultado)

except ValueError:
    print("Error: Por favor, introduce un número válido.")


# In[279]:


# 40. Función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") 
# y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    """
    Calcula el área de una figura geométrica.

    Args:
        figura (str): Tipo de figura ("rectangulo", "circulo" o "triangulo").
        datos (tuple): Datos necesarios para el cálculo

    Returns:
        float: Area de figura indicada

    Raises:
        ValueError: Si la figura no es válida.
    """

    if figura == "rectangulo":
        # Datos necesarios para calcular area: (base, altura)
        base, altura = datos
        area = base * altura
        return "El area de rectangulo es", area

    elif figura == "circulo":
        # Datos necesarios para calcular area: (radio,)
        radio = datos[0]
        area = math.pi * (radio ** 2)
        return "El area de circulo es", round(area, 2)

    elif figura == "triangulo":
        # Datos necesarios para calcular area: (base, altura)
        base, altura = datos
        area = (base * altura) / 2
        return "El area de triangulo es", area

    else:
        return "Figura no válida"


# In[278]:


# 40. Ejemplo de uso:

print(calcular_area("rectangulo", (10, 20)))
print(calcular_area("circulo", (2,)))
print(calcular_area("triangulo", (10, 20)))


# In[292]:


# 41. Programa que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.
# El programa debe hacer lo siguiente:
    # 1. Solicita al usuario que ingrese el precio original de un artículo.
    # 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
    # 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
    # 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero).
    # 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.

try:
    # 1. Solicitamos el precio original
    precio_original = float(input("Introduce el precio original del artículo:"))

    # 2. Preguntamos si tiene un cupón de descuento
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no):")

    # 3. Si el usuario tiene cupón, solicitamos el valor del cupón
    if tiene_cupon == "sí":
        descuento = float(input("Introduce el valor del cupón de descuento, €:"))

    # 4. Validamos si el cupón es válido (mayor a cero)
        if descuento > 0:
            # Aplicamos el descuento:
            # Si el cupón es mayor al precio, el precio no puede ser negativo
            if descuento > precio_original:
                precio_final = 0
                print("El cupón cubre el total de la compra. Descuento aplicado: €", precio_original)
            else:
            # Si el cupón es menor al precio, restamos el descuento
                precio_final = precio_original - descuento
                print(f"Descuento € {descuento} aplicado correctamente")
        else:
            print("El valor del cupón no es válido. No se aplicará descuento.")
            precio_final = precio_original

    else:
    # Si no tiene cupón o la opsión no reconocida, el precio final es el original   
        precio_final = precio_original
        print("No se ha aplicado ningún descuento.")

    # 5. Mostramos el precio final
    print("Precio final de la compra: €", precio_final)

except ValueError:
    print("Error: Por favor, introduce valores numéricos")

