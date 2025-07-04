datos = {
    "E001": ["Ana", 15, [6.5, 6.0, 6.8], "8A"],
    "E002": ["Luis", 14, [5.0, 5.5, 6.0], "8B"],
    "E003": ["Carla", 15, [6.8, 6.9, 7.0], "8A"],
    "E004": ["Marco", 14, [4.5, 5.0, 5.2], "8C"],
    "E005": ["Sofia", 15, [6.2, 6.3, 6.1], "8B"],
    "E006": ["Pedro", 14, [5.8, 6.0, 5.9], "8A"],
    "E007": ["Elena", 15, [4.0, 4.5, 4.2], "8C"],
    "E008": ["Jorge", 14, [6.9, 7.0, 6.8], "8B"],
    "E009": ["Lucia", 15, [5.5, 5.6, 5.7], "8A"],
    "E010": ["Diego", 14, [3.8, 4.0, 4.2], "8C"]
}
promedios={}
while True:
    print(promedios)
    print("1. Ver Lista de estudiantes")
    print("2. Buscar Estudiante Por Nombre")
    print("3. Top 3")
    print("4. Listar Estudiantes Por Curso")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            ordenados=sorted(datos.items(),key= lambda x:x[1][0])
            for n,i in datos.items():
                if n:
                    promedio=(sum(datos[n][2]))/3
                    promedio=round(promedio,1)
                    promedios[n]=[i[0],promedio]
                print(f"{n} Nombre: {i[0]}|Edad: {i[1]}| Promedio: {promedio}| Curso: {i[3]}")
        case 2:
            name=input("Ingrese nombre de estudiante a buscar: ").title()
            dispo=[valor[0] for valor in datos.values()]
            if name in dispo:
                for n,i in datos.items():
                    if name==i[0]:
                        promedio=(sum(datos[n][2]))/3
                        promedio=round(promedio,1)
                        print(f"{n} Nombre: {i[0]}|Edad: {i[1]}| Promedio: {promedio}| Curso: {i[3]}")
            else:
                print("Estudiante Ingresado No Existe")
        case 3:
            import heapq
            if promedios:
                top=heapq.nlargest(3,promedios.items(),key= lambda x:x[1][1])
                for i,(n,v) in enumerate(top,start=1):
                    print(f"{i}- {v[0]} Promedio: {v[1]}")
            else:
                for n,i in datos.items():
                    if n:
                        promedio=(sum(datos[n][2]))/3
                        promedio=round(promedio,1)
                        promedios[n]=[i[0],promedio]
                top=heapq.nlargest(3,promedios.items(),key= lambda x:x[1][1])
                for i,(n,v) in enumerate(top,start=1):
                    print(f"{i}- {v[0]} Promedio: {v[1]}")
        case 4:
            curso=input("Ingrese curso que desea filtrar: ").upper()
            dispo=[valor[3] for valor in datos.values()]
            if curso in dispo:
                print(f"Estudiantes de el curso {curso}")
                for n,i in datos.items():
                    if curso==i[3]:
                        promedio=(sum(datos[n][2]))/3
                        promedio=round(promedio,1)
                        promedios[n]=[i[0],promedio]
                        print(f"{n} Nombre: {i[0]}|Edad: {i[1]}| Promedio: {promedio}")
            else:
                print("No hay coincidencias")
            