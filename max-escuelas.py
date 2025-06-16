datos={}
while True:
    print("1. Agregar Escuela")
    print("2. Votar Por Escuela")
    print("3. Ver Resultados")
    print("4. Ver Escuela Ganadora")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de la escuela")
            nombre=nombre.capitalize()
            futbol=0
            Basket=0
            natacion=0
            total=0
            datos[nombre]={"futbol":futbol,"basket":Basket,"natacion":natacion,"total":total}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}")
                print()
            buscar=input("Ingrese nombre de la escuela que votara: ")
            for n,i in datos.items():
                if buscar.capitalize() == n:
                    print(f"Futbol: {i["futbol"]}\nBasket: {i["basket"]}\nNatacion: {i["natacion"]}\nVotos Totales: {i["total"]}")
                    print()
                    escuela=input("Ingrese Rama Que Votara: ")
                    if escuela.capitalize() == "Futbol":
                        votos=int(input("Ingrese Cantidad de votos: "))
                        i["futbol"]+=votos
                        i["total"]+=votos
                    elif escuela.capitalize() == "Basket":
                        votos=int(input("Ingrese Cantidad de votos: "))
                        i["basket"]+=votos
                        i["total"]+=votos
                    elif escuela.capitalize()== "Natacion":
                        votos=int(input("Ingrese Cantidad de votos: "))
                        i["natacion"]+=votos
                        i["total"]+=votos
                        
        case 3:
            for n,i in datos.items():
                print(f"Escuela: {n}\nFutbol: {i["futbol"]}\nBasket: {i["basket"]}\nNatacion: {i["natacion"]}\nVotos Totales: {i["total"]}")
                print()
        case 4:
            mayor=max(datos,key=lambda x:datos[x]["total"])
            print(f"La Escuela Ganadora es: {mayor} Con {datos[mayor]["total"]} Votos Totales")
            print() 