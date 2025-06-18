datos={}
while True:
    print("1. Votar Proyecto")
    print("2. Ver Proyectos")
    print("3. Ver Resultado Ganador")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            print("1. Spiderman ")
            print("2. Robocop")
            print("3. IronMan")
            op=int(input("Vote Por Un Proyecto: "))
            if op==1:
                proyecto="Spiderman"
            elif op==2:
                proyecto="Robocop"
            elif op==3:
                proyecto="IronMan"
            if proyecto not in datos:
                voto=1
            else:
                voto+=1
            datos[proyecto]={"voto":voto}
        case 2:
            for n,i in datos.items():
                print(f"Proyecto: {n}\nCantidad de votos: {i["voto"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda x:datos[x]["voto"])
            print(f"El Proyecto Ganador es: {mayor} Con {datos[mayor]["voto"]} Votos")
            