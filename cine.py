datos={}
entradas=[]
entradasdispo=50
total=0
codigo=-1
while True:
    print("1. Comprar Entradas")
    print("2. Consultar Entradas vendidas")
    print("3. Eliminar Entradas")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            print(f"Las entradas disponibels son {entradasdispo}")
            cantidad=int(input("Ingrese cantidad de entradas que va a comprar: "))
            for i in range(cantidad):
                codigo+=1
                total+=1
                print(f"Ingrese datos de la entrada n°{total}")
                nombre=input("Ingrese nombre su nombre")
                edad=int(input("Ingrese su edad:"))
                print("1. Spiderman 1")
                print("2. Spiderman 2")
                print("3. Sheak")
                peli=int(input("Ingrese pelicula que desea ir a ver: "))
                if peli ==1:
                    peli="Spiderman 1"
                elif peli==2:
                    peli="Spiderman 2"
                else:
                    peli="Sheak"
                datos={
                    "Total":codigo,
                    "nombre":nombre,
                    "edad":edad,
                    "pelicula":peli
                }
                entradas.append(datos)
            print(F"TOTAL COMPRO {total} Entradas")
        case 2:
            if not entradas:
                print("NO HAY NADA")
            for i in entradas:
                print(f"Codigo: {i["Total"]} Nombre: {i["nombre"]}| Edad: {i["edad"]}| Pelicula: {i["pelicula"]}")
        case 3:
            for i in entradas:
                print(f"Codigo: {i['Total']} Nombre: {i['nombre']}| Edad: {i['edad']}| Pelicula: {i['pelicula']}")
            eliminar = int(input("Ingrese elemento que desea eliminar: "))
            if eliminar==i["Total"]:
                del entradas[eliminar]
                print(f"Se elimino el codigo {i["Total"]}")
            elif eliminar==0:
                del entradas[eliminar]
                