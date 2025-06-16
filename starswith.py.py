datos={}
total=0
while True:
    print("1. Registar Invitados: ")
    print("2. Ver Invitasdos")
    print("3. Filtrar Invitados")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            total+=1
            nombre=input("Ingrese nombre de invitado: ")
            edad=int(input("Ingrese edad de el invitado: "))
            datos[nombre]={"edad":edad}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nEdad: {i["edad"]}")
        case 3:
            exit=0
            l=input("Ingrese la letra por la que va a filtrar a sus invitados: ").lower()
            for n,i in datos.items():
                exit+=1
                if n.lower().startswith(l):
                    print(f"Nombre: {n}\nEdad: {i["edad"]}")
                elif l not in datos and exit==total:
                    print("NO HAY COINCIDENCIAS")
                    