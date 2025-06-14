datos=[]
info={}
id=0
numeros=[]
while True:
    print("1. Agregar empleado")
    print("2. Editar Datos de empleado")
    print("3. Eliminar Empleado")
    print("4. Buscar Empleado por ID")
    print("5. Mostrar Empleados Mayor a menor")
    op=input("Ingrese una opcion: ")
    match op:
        case "1":
            cantidad=int(input("Ingrese cantidad de empleados que va a registrar: "))
            for i in range(cantidad):
                nombre=input("Ingrese nombre de el empleado: ")
                edad=(input("Ingrese edad : "))
                puesto=input("Ingrese el rango de el empledo: ")
                salario=int(input("Ingrese el salario de el empleado: "))
                id+=1
                info={
                    "id":id,
                    "nombre":nombre,
                    "edad":edad,
                    "puesto":puesto,
                    "salario":salario
                }
                datos.append(info)
        case "2":
            for i in datos:
                id=int(input("Ingrese ID de empleado: "))
                if id in i["id"]:
                    print(f"ID: {i["id"]}\n-Nombre: {i["nombre"]}\n-Edad: {i["edad"]}\n-Puesto: {i["puesto"]}\n-Salario: {i["salario"]}")
                    editar=input("Ingrese elemto que desea editar: ")
                    editar=editar.capitalize()
                    if editar=="Nombre":
                        nombre=input("Ingrese nombre nuevo: ")
                        i["nombre"]=nombre
                    elif editar=="Edad":
                        edad=input("Ingrese la edad nueva: ")
                        i["edad"]=edad
                    elif editar=="Salario":
                        salario=input("Ingrese salario nuevo: ")
                        i["salario"]=salario
                    elif editar=="Puesto":
                        puesto=input("Ingrese nuevo puesto: ")
                        i["puesto"]=editar
        case "3":
            n=0
            for i in datos:
                n+=1
                print(f"ID: {n}\n-Nombre: {i["nombre"]}\n-Edad: {i["edad"]}\n-Puesto: {i["puesto"]}\n-Salario: {i["salario"]}")
                if n==id:
                    eliminar=int(input("Ingrese ID De empleado que desea elimina: "))
                    eliminar-=1
                    if datos:
                        del datos[eliminar]
                        print(f"Se ha eliminado a {i["nombre"]}")
                        n=0
                        id-=1
        case "4":
            n=0
            for i in datos:
                n+=1
                (f"ID: {i["id"]}\n-Nombre: {i["nombre"]}\n-Edad: {i["edad"]}\n-Puesto: {i["puesto"]}\n-Salario: {i["salario"]}")
                i["id"]=str(i["id"])
                print(f"En total hay {id} Empleados")
                if n==id:
                    buscar=input("Ingrese numero de empleado: ")
                    for i in datos:
                        if buscar in i["id"]:
                            print(f"ID: {i["id"]}\n-Nombre: {i["nombre"]}\n-Edad: {i["edad"]}\n-Puesto: {i["puesto"]}\n-Salario: {i["salario"]}")
                        else:
                            print(f"El Empleado numero {buscar} no existe")
                            print()
        case "5":
            for i in datos:
                numeros.append(i["salario"])
            ordenados = sorted(numeros, reverse=True)
            print(ordenados)  # [9, 7, 5, 2, 1]
                            