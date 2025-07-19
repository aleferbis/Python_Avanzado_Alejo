1

# def calcu_descuentos(precio, descuento):
#     """
#     Calcula el precio final luego de aplicar un descuento porcentual.

#     Parámetros:
#     -
#     precio (float): El precio original del producto antes de aplicar el descuento.

#     descuento (float): El porcentaje de descuento a aplicar.

#     Retorna:
#      -
#     float: El precio final con el descuento aplicado, redondeado a 2 decimales.

#     str: Si los parámetros son inválidos, retorna un mensaje de error.
#     """
#     if precio <= 0 or descuento <= 0:
#         return "El precio o descuento no pueden ser menores o iguales a 0"
#     else:
#         precio_final = precio-(precio*(descuento/100))
#         return round (precio_final,2)
# precio = float(input("Introduzca el precio original: "))
# descuento = float(input("Introduzca el porcentaje de descuento: "))
# precio_final = calcu_descuentos(precio, descuento)
# print (f"el precio final es {precio_final}")



#2

# def convert_temp(temp_original, unidad_final):
#     """
#     Convierte una temperatura dada en formato string con unidad (°C o °F) a la unidad deseada.

#     Parámetros:
# #     -
# #     temp_original (str): Temperatura original con formato "valor°unidad", por ejemplo "33°C" o "91°F".

# #     unidad_final (str): Unidad a la que se desea convertir la temperatura. Debe ser "C" o "F".

# #     Retorna:
# #     -
# #     str:Temperatura convertida en formato "valor°unidad", sin redondear decimales.
# #         Si la unidad original y final son iguales, devuelve la misma temperatura.
# #         Si la unidad no es soportada, devuelve un mensaje de error.
# #     """
#     temp, unidad = temp_original.split("°")
#     temp = float(temp)
#     if unidad == unidad_final:
#         return str(temp) + "°" + unidad

#     if unidad == "C" and unidad_final == "F":
#         temp_f = str((temp * 9/5) + 32)
#         return temp_f + "°" + "F"
#     elif unidad == "F":
#         temp_c = str((temp - 32) * 5/9)
#         return temp_c + "°" + "C"
#     else:
#         return "Unidad no soportada"

# temp_original = input("Introduzca la temperatura original: ")
# unidad_final = input("Introduzca la unidad a la que desea convertirla: ")
# print (convert_temp (temp_original, unidad_final))



#3

# def verif_palindromo(palabra):
#     """
#     Verifica si una palabra es un palíndromo.

#     Parámetros:
#     -
#     palabra (str): Palabra a verificar.

#     Retorna:
#     -
#     bool: True si la palabra es un palíndromo, False en caso contrario.
#     """
#     palabra = palabra.lower()
#     longitud = len(palabra)
    
#     for i in range(longitud // 2):
#         if palabra[i] != palabra[longitud - 1 - i]:
#             return False
    
#     return True

# palabra = input("Introduzca la palabra a verificar: ")
# resultado = verif_palindromo(palabra)
# if resultado == True:
#     print (f"La palabra {palabra} es un palindromo")
# else:
#     print (f"La palabra {palabra} no es un palindromo")



#4

# def analisis_texto (texto):
#     """
#     Analiza un texto y devuelve cuantos caracteres y palabras posee.

#     Parámetros:
#     -
#     texto (str): El texto a analizar.

#     Retorna:
#     -
#     dict: Un diccionario con:
#         - Cantidad de caracteres
#         - Cantidad de palabras
#     """
#     cant_caracteres = len(texto)
#     cant_palabras = len(texto.split( ))
#     analisis = {
#         "Cantidad de caracteres" : cant_caracteres,
#         "Cantidad de palabras" : cant_palabras
#     }
#     return analisis
# texto = ""
# print (analisis_texto (texto))

# #si lo hago con un input me cuenta toda la direccion de python



#5

# def generar_primos(hasta):
#     """
#     Genera una lista de números primos desde el 2 hasta el número dado.

#     Un número primo es un número mayor que 1 que solo tiene dos divisores positivos: él mismo y el 1.
#     Por ejemplo, 2, 3, 5 y 7 son números primos.

#     Parámetros:
#     -
#     hasta (int): Número entero positivo hasta el cual se desean obtener los números primos.

#     Retorna:
#     -
#     list: Lista de números primos hasta el número dado.
#     """
#     if hasta < 2:
#         return []

#     primos = []
#     for numero in range(2, hasta):
#         es_primo = True
#         for i in range(2, int(numero**0.5)):
#             if numero % i == 0:
#                 es_primo = False
#                 break
#         if es_primo:
#             primos.append(numero)
#     return primos

# print(generar_primos(7))



#6



#7

# def convertir_a_listas_de_caracteres(lista_strings):
#     """
#     Convierte una lista de strings en una lista de listas de caracteres usando map.

#     Parámetros:
#     -
#     lista_strings (list): Lista de palabras (strings).

#     Retorna:
#     -
#     list: Lista donde cada palabra se convierte en una lista de caracteres.
#     """
#     return list(map(list, lista_strings))

# resultado = convertir_a_listas_de_caracteres(["hola", "adios"])
# print(resultado)



#8

# def calcular_estadisticas(numeros):
#     """
#     Calcula la media, mediana y moda de una lista de números.

#     Estadísticas:
#     -
#     Media: Es el promedio de los valores. Se obtiene sumando todos los números 
#              y dividiendo entre la cantidad total de elementos.
#     Mediana: Es el número que está en el centro cuando la lista está ordenada. 
#                Si hay una cantidad par de elementos, se promedian los dos del medio.
#     Moda: Es el valor o los valores que más se repiten en la lista.

#     Parámetros:
#     -
#     numeros (list): Lista de números (int o float).

#     Retorna:
#     -
#     dict: Un diccionario con las claves 'media', 'mediana' y 'moda' y sus valores correspondientes.

#     Ejemplo:
#     -
#     calcular_estadisticas([1, 2, 2, 3, 4])
#     {'media': 2.4, 'mediana': 2, 'moda': [2]}
#     """
#     media = sum(numeros) / len(numeros)
    
#     ordenados = sorted(numeros)
#     n = len(ordenados)
#     mitad = n // 2
#     if n % 2 == 1:
#         mediana = ordenados[mitad]
#     else:
#         mediana = (ordenados[mitad - 1] + ordenados[mitad]) / 2
    
#     frecuencia = {}

#     for valor in numeros:
#         frecuencia[valor] = frecuencia.get(valor, 0) + 1

#     max_frecuencia = max(frecuencia.values())

#     moda = [clave for clave, valor in frecuencia.items() if valor == max_frecuencia]

#     estadisticas = {
#         "media" : media,
#         "mediana" : mediana,
#         "moda" : moda
#     }
    
#     return  estadisticas

# numeros = []
# print(calcular_estadisticas(numeros))
