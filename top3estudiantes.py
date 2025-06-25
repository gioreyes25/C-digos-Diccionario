datos={}
import heapq
while True:
    print("1. Agregar Estudiantes")
    print("2. Ver Lista De Estudiantes")
    print("3. Ver Mejor Estudiante")
    op=int(input("Ingrese una op: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de estudiante: ").title()
            edad=int(input("Ingrese edad: "))
            curso=input("Ingrese curso: ").title()
            n1=float(input("Ingrese nota de matematicas: "))
            n2=float(input("Ingrese nota de historia: "))
            n3=float(input("Ingrese nota de ciencias: "))
            pro=(n1+n2+n3)/3
            pro=round(pro,1)
            datos[nombre]={"edad":edad,"promedio":pro,"curso":curso}
        case 2:
            for n,i in datos.items():
                print(f"Estudiante: {n}\nEdad: {i["edad"]}\nPromedio: {i["promedio"]}")
                print()
        case 3:
            print("1. Ver Mejores Estudiantes En General")
            print("2. Ver Por Curso")
            op=int(input("Ingrese una op: "))
            match op:
                case 1:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["promedio"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}-Estudiante: {n} Promedio: {v["promedio"]}")
                case 2:
                    for n,i in datos.items():
                        print(f"Curso: {i["curso"]}")
                    elegir=input("Ingrese Curso Que Dese Ver: ").title()
                    filtrados = [(k, v) for k, v in datos.items() if v["curso"] == elegir]
                    top2=heapq.nlargest(3,filtrados,key= lambda x:x[1]["promedio"])
                    print(f"Top 3 Estudiantes De Curso {elegir}")
                    for i,(n,v) in enumerate(top2,start=1):
                        print(f"{i}- {n} Promedio: {v["promedio"]}")