#1)

# def ordenar_lista(Lista):
#     lista_sin_duplicados = list(set(Lista))
#     lista_sin_duplicados.sort()
#     return lista_sin_duplicados
# numeros = [5, 3, 8, 3, 1, 5, 2]
# resultado = ordenar_lista(numeros)
# print(resultado)



#2)

# mi_conjunto = set()

# cantidad = int(input("¿Cuántos elementos querés agregar al conjunto? "))
# for i in range(cantidad):
#     elemento = input(f"Ingresá el elemento {i+1}: ")
#     mi_conjunto.add(elemento)

# print("Conjunto actual:", mi_conjunto)

# while True:
#     eliminar = input("¿Qué elemento querés eliminar del conjunto? ")

#     if eliminar in mi_conjunto:
#         mi_conjunto.remove(eliminar)
#         print(f"Elemento '{eliminar}' eliminado.")
#         break
#     else:
#         print(f"El elemento '{eliminar}' no está en el conjunto.")
        
# print("Conjunto final:", mi_conjunto)



#3)

# entrada1 = input("Ingrese los números del primer conjunto separados por espacios: ")
# conjunto1 = set(map(int, entrada1.split()))

# entrada2 = input("Ingrese los números del segundo conjunto separados por espacios: ")
# conjunto2 = set(map(int, entrada2.split()))

# solo_en_1 = conjunto1 - conjunto2
# solo_en_2 = conjunto2 - conjunto1

# print("Números que están en el primer conjunto pero no en el segundo:", solo_en_1)
# print("Números que están en el segundo conjunto pero no en el primero:", solo_en_2)



#4)

# def eliminar_duplicados(lista):
#     return list(set(lista))

# cadenas = ["hola", "mundo", "hola", "python", "mundo"]
# resultado = eliminar_duplicados(cadenas)
# print("Lista sin duplicados:", resultado)



#5)

# def factorial(n):
#     resultado = 1
#     for i in range(1, n + 1):
#          resultado *= i
#     return resultado

# numero = int(input("Ingresá un número: "))
# resultado = factorial(numero)
# print("El factorial de", numero, "es", resultado)


#6)

# def fibonacci(n):
#     serie = []

#     for i in range(n):
#         if i == 0:
#             serie.append(0)
#         elif i == 1:
#             serie.append(1)
#         else:
#             nuevo = serie[i - 1] + serie[i - 2]
#             serie.append(nuevo)
    
#     return serie
# print(fibonacci(9))



#7)

# def suma_recursiva(n):
#     for i in range(n):
#         if n == 1:
#             return 1
#         else:
#             return n + suma_recursiva(n - 1)
# print (suma_recursiva(5))



#8)

# class Libro:
#     def __init__(self, titulo, autor, año_publicacion):
#         self.titulo = titulo
#         self.autor = autor
#         self.año_publicacion = año_publicacion

#     def mostrar_info(self):
#         print(f"Título: {self.titulo}")
#         print(f"Autor: {self.autor}")
#         print(f"Año de publicación: {self.año_publicacion}")

# class LibroDigital(Libro):
#     def __init__(self, titulo, autor, año_publicacion, formato):
#         super().__init__(titulo, autor, año_publicacion)
#         self.formato = formato

#     def mostrar_info(self):
#         super().mostrar_info()
#         print(f"Formato digital: {self.formato}")

# libro1 = Libro("Harry Potter", "J.K. Rowling", 1997)
# libro1.mostrar_info()

# print("------")

# libro_digital = LibroDigital("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "PDF")
# libro_digital.mostrar_info()



#9)

# def slicing_function(texto):
#     diccionario = {}

#     partes = texto.split("|")

#     for parte in partes:
#         parte = parte.strip()

#         posicion_dos_puntos = parte.find(":")

#         clave = parte[:posicion_dos_puntos].strip().lower()
#         valor = parte[posicion_dos_puntos + 1:].strip()

#         if valor.isdigit():
#             valor = int(valor)

#         diccionario[clave] = valor

#     return diccionario

# text = "Nombre: Juan Pérez | Edad: 30 | Ciudad: Salta"
# resultado = slicing_function(text)
# print(resultado)