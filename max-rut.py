datos={}
while True:
    print("1. Agregar Estudiantes")
    print("2. Buscar Estudiante Por Rut")
    print("3. Mostrar Estudiantes Por Carrera")
    print("4. Contar Cuantos Estduaintes Por Carrera Hay")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            Conteo=0
            rut=input("Ingrese rut de estudiante: ")
            if rut in datos:
                print("Rut Usado")
            nombre=input("Ingrese nombre de estudiante: ").capitalize()
            print()
            print("1. Ingenieria Informatica")
            print("2. Odontologia")
            print("3. Medicina")
            carrera=input("Ingrese Carrera del estudiante").capitalize()
            if carrera == "Ingenieria informatica" or "Odontologia" or "Medicina":
                datos[rut]={"nombre":nombre,"carrera":carrera,"conteo":Conteo,"conteo":Conteo,"conteo":Conteo}
                for n,i in datos.items():
                    if carrera==i["carrera"]:
                        i["conteo"]+=1
            print("REGISTRADO")
            print()
        case 2:
            b=input("Ingrese rut de estudiante para buscar: ")
            for n,i in datos.items():
                if b==n:
                    print(f"Rut: {n}\nNombre: {i["nombre"]}\nCarrera: {i["carrera"]}")
                    print()
        case 3:
            print("1. Ingenieria Informatica")
            print("2. Odontologia")
            print("3. Medicina")
            buscar=input("Ingrese Carrera Que Desea Buscar: ").capitalize()
            for n,i in datos.items():
                if buscar==i["carrera"]:
                    print(f"Rut: {n}\nNombre: {i["nombre"]}\nCarrera: {i["carrera"]}")
        case 4:
            for n,i in datos.items():
                si=0
                if i["carrera"]=="Ingenieria informatica"and si==0:
                    print(f"En Informatica Hay: {i["conteo"]}")
                    si+=1
                elif i["carrera"]=="Odontologia"and si==0:
                    si+=1
                    print(f"En Odontologia Hay: {i["conteo"]}")
                elif i["carrera"]=="Medicina" and si==0:
                    si+=1
                    print(f"En Medicina Hay: {i["conteo"]}")                