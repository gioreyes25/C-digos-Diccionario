import heapq
estudiantes = {
    "Ana": {"edad": 20, "curso": "Matemáticas"},
    "Luis": {"edad": 22, "curso": "Historia"},
    "Sofía": {"edad": 21, "curso": "Biología"}
}

# Obtener los 2 estudiantes con mayor edad
top = heapq.nlargest(3, estudiantes.items(), key=lambda x: x[1]["edad"])

# Mostrar resultados
print("Top 2 estudiantes con mayor edad:")
for i, (nombre, info) in enumerate(top, start=1):
    print(f"{i}. {nombre} - {info['edad']} años - {info['curso']}")