parking={}
ocupados={}
filas=["P1-","P2-","P3-","P4-"]
letras=["A","B","C"]
columna=range(1,4)
for filas in filas:
    for col in columna:
        for l in letras:
            lugar=f"{filas}{l}{col}"
            parking[lugar]={"disponible":True,"patente":"","auto":""}
while True:
    print("1. Mostrar Estacionamientos Por Piso")
    print("2. Estacionar Auto")
    print("3. Retirar Auto")
    print("4. Buscar Auto Por Patente")
    print("5. Mostrar Total der espacios ocupados por piso")
    print("6. Ver Porcentaje de ocupacion General")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            piso=input("Ingrese Piso Que desea buscar: ")
            for n,i in parking.items():
                if i["disponible"]==True:
                    if n.startswith(piso):
                        print(f"Lugar: {n}\nDisponible")
        case 2:
            piso=input("Ingrese piso que em cual desea estacionar: ")
            for n,i in parking.items():
                if n.startswith(piso):
                    print(f"Lugar: {n}\nDisponible")
            elegir=input("Eliga Lugar: ")
            for n,i in parking.items():
                if elegir==n:
                    patente=input("Escriba Patente: ")
                    auto=input("Ingrese Marca De Su Vehiculo: ")
                    print(f"Ha estacionado Su vehiculo En EL Lugar: {n}")
                    i["disponible"]=False
                    i["patente"]=patente
                    i["auto"]=auto
                    ocupados[patente]={"patente":auto,"Piso":piso}
        case 3:
            for n,i in parking.items():
                if i["disponible"]==False:
                    print(f"Lugar: {n}\nPatente: {i["patente"]}\nVehiculo: {i["auto"]}\nOcupado")
            retirar=input("Ingrese Patente De Vehiculo: ")
            for n,i in parking.items():
                if retirar==i["patente"]:
                    print(f"Ha retirado Vehiculo De Lugar {n} Con La Patente {i["patente"]}")
                    i["disponible"]=True
                    del ocupados[retirar]
        case 4:
            buscar=input("Ingrese Patente Para Buscar Su Vehiculo: ")
            for n,i in parking.items():
                if buscar==i["patente"]:
                    print(f"Su Vehiculo {i["auto"]} Esta estacionado en el {n}") 
        case 5:
            cadena=str(ocupados)
            conteo=cadena.count("P1-")
            num=int(conteo)
            porcen=(num/9)*100
            porcen=round(porcen,1)
            print(F"En El Piso 1, Hay {conteo} Ocupados De 9\nSe ha ocupado en un {porcen}%")
            cadena=str(ocupados)
            conteo=cadena.count("P2-")
            num=int(conteo)
            porcen=(num/9)*100
            porcen=round(porcen,1)
            print(F"En El Piso 2, Hay {conteo} Ocupados De 9\nSe ha ocupado en un {porcen}%")
            cadena=str(ocupados)
            conteo=cadena.count("P3-")
            num=int(conteo)
            porcen=(num/9)*100
            porcen=round(porcen,1)
            print(F"En El Piso 3, Hay {conteo} Ocupados De 9\nSe ha ocupado en un {porcen}%")
            cadena=str(ocupados)
            conteo=cadena.count("P4-")
            num=int(conteo)
            porcen=(num/9)*100
            porcen=round(porcen,1)
            print(F"En El Piso 4, Hay {conteo} Ocupados De 9\nSe ha ocupado en un {porcen}%")
            
                