#lower()	Convierte a minúsculas.
#upper()	Convierte a mayúsculas.
#capitalize()	Solo la primera letra en mayúscula.
#title()	Primera letra de cada palabra en mayúscula.
#swapcase()	Cambia mayúsculas ↔ minúsculas.
#casefold()	Minúsculas más agresiva (ideal para comparar sin importar el idioma).
#strip()	Elimina espacios (u otros caracteres) al principio y al final.
#lstrip() / rstrip()	Como strip() pero solo a la izquierda / derecha.
#replace(a, b)	Reemplaza todas las ocurrencias de a por b.
#zfill(n)	Rellena con ceros a la izquierda hasta llegar a n caracteres.
#center(n, c)	Centra la cadena y la rellena con el carácter c.
#ljust(n, c) / rjust()	Alinea a izquierda o derecha con relleno.

#letra=input("Ingrese una palabra: ").title()

#letra=input("Ingrese una palabra: ").swapcase()
# Lista base
numeros = [10, 20, 5, 40, 0, -5]

print("📋 Lista original:", numeros)

# 1. len()
print("🔢 Cantidad de elementos:", len(numeros))

# 2. max()
print("⬆️ Valor máximo:", max(numeros))

# 3. min()
print("⬇️ Valor mínimo:", min(numeros))

# 4. sum()
print("➕ Suma total:", sum(numeros))

# 5. sorted()
print("📊 Ordenada (ascendente):", sorted(numeros))

# 6. reversed()
print("↩️ Invertida:", list(reversed(numeros)))

# 7. list() - Convertir un string a lista de letras
palabra = "python"
letras = list(palabra)
print("🔤 Lista de letras:", letras)

# 8. enumerate()
print("📌 Enumerando:")
for i, valor in enumerate(numeros):
    print(f"Índice {i} → {valor}")

# 9. zip() - Combinar dos listas
nombres = ["Ana", "Luis", "Marta"]
edades = [30, 25, 22]
print("👥 Datos combinados con zip:")
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# 10. all() y any()
valores = [True, True, False]
print("✅ Todos son True:", all(valores))
print("❓ Alguno es True:", any(valores))

# 11. map() - Elevar cada número al cuadrado
cuadrados = list(map(lambda x: x**2, numeros))
print("² Cuadrados de cada número:", cuadrados)

# 12. filter() - Filtrar números positivos
positivos = list(filter(lambda x: x > 0, numeros))
print("🟢 Solo positivos:", positivos)

# 13. type()
print("📂 Tipo de variable:", type(numeros))

# 14. isinstance()
print("¿Es una lista?:", isinstance(numeros, list))

# 15. input() (comentado porque interrumpe ejecución)
# entrada = input("Ingresa algo: ")
# print("✍️ Escribiste:", entrada)
