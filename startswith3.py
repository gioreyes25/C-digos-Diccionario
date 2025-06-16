datos={}
total=0
while True:
    print("1. Agender Contactos")
    print("2. Ver Contactos")
    print("3. Filtrar Contactos")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            total+=1
            nombre=input("Ingrese nombre de contacto: ")
            numero=input("Ingrese numero ")
            datos[nombre]={"numero":numero}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nNumero: {i["numero"]}")
                print()
        case 3:
            exit=0
            num=input("Ingrese un numero en cual se mostraran todos los numeeros\nQue comienzen con ese numero")
            print(f"Numeros Que Comienzen Con {num}")
            for n,i in datos.items():
                exit+=1
                if i["numero"].lower().startswith(num):
                    print(f"Nombre: {n}\nNumero: {i["numero"]}")
                    print()
                    break
                elif num not in datos and exit==total:
                    print("NO HAY COINCIDENCIAS")