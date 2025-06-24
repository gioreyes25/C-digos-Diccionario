datos={}
while True:
    print("1. Agregar Estudiantes")
    print("2. Ver Lista De Estudiantes")
    print("3. Ver Mejor Estudiante")
    op=int(input("Ingrese una op: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de estudiante: ").title()
            edad=int(input("Ingrese edad: "))
            curso=input("Ingrese curso: ")
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
            import heapq
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["promedio"])
            for i,(n,v) in enumerate(top,star=1):
                print(f"{i}-Estudiante: {n} Promedio: {v["promedio"]}")