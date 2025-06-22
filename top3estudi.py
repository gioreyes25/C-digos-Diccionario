import heapq
datos={}
mejores=[]
while True:
    print(mejores)
    print("1. Agregar Estudiante")
    print("2. Ver Todos Los Estudiantes")
    print("3. Ver Mejores Estudiantes")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            name=input("Ingrese nombre de el estudiante: ").capitalize()
            n1=float(input("Ingrese nota de Matematicas"))
            n2=float(input("Ingrese nota de Historia"))
            n3=float(input("Ingrese nota de Ciencias"))
            p=(n1+n2+n3)/3
            p=round(p,1)
            datos[name]={"promedio":p}
            mejores.append((name,p))
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nPromedio: {i["promedio"]}")
                print()
        case 3:
            print("Ver Mejor Estudiante En General")
            print("Ver Top x de estudiantes")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    mayor=max(datos,key=lambda name:datos[name]["promedio"])
                    print(f"El mejor Estudiante es {mayor} Con Promedio de {datos[mayor]["promedio"]}")
                    print()
                case 2:
                    c=int(input("Ingrese cantidad de estudiantes que dese buscar: "))
                    top=heapq.nlargest(c,mejores,key=lambda x:x[1])
                    for i,(name,p) in enumerate(top,start=1):
                        print(f"{i}- {name} Promedio: {p:.1f}")