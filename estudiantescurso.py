datos={}
mejores={}
conteo=0
while True:
    print("1. Agregar Estudiantes")
    print("2. Ver Promedios ")
    print("3. Ver Mejor Estdudiante")
    print("4. Ver Reporte De Curso")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de el estudiante: ")
            edad=input("Ingrese Edad: ")
            curso=int(input("Ingrese Curso"))
            nota1=float(input("Ingrese Nota De Matematicas: "))
            nota2=float(input("Ingrese Nota De Historia: "))
            nota3=float(input("Ingrese Nota De Ciencias: "))
            promedio=(nota1+nota2+nota3)/3
            promedio=round(promedio,1)
            conteo+=1
            datos[nombre]={"nombre":nombre,"edad":edad,"curso":curso,"promedio":promedio}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {i["nombre"]}\nEdad: {i["edad"]}\nCurso: {i["curso"]}° Basico\nPromedio: {i["promedio"]}")
                print()
        case 3:
            mas=max(datos,key=lambda nombre:datos[nombre]["promedio"])
            print(f"El mejor estudiante en general es: {mas} con promedio de {datos[mas]["promedio"]}")
            for n,i in datos.items():
                if i["curso"]==1:
                    mejores[nombre]={"promedio":i["promedio"]}
                    mayor=max(mejores,key=lambda nombre:mejores[nombre]["promedio"])
                    if i["curso"]==1:
                        print(f"El Mejor Estudiante de 1 es {mayor} Promedio: {mejores[mayor]["promedio"]}")
                if i["curso"]==2:
                    mejores[nombre]={"promedio":i["promedio"]}
                    mayor=max(mejores,key=lambda nombre:mejores[nombre]["promedio"])
                    if i["curso"]==2:
                        print(f"El Mejor Estudiante de 2 es {mayor} Promedio: {mejores[mayor]["promedio"]}")