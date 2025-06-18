datos={}
while True:
    print(datos)
    print("1. Agregar Ciudades")
    print("2. Ver Tabla")
    print("3. Ver Ciudad Mejor Sostenible")
    print("4. Ver Ciudad Peor Sostenible")
    print("5. Ver Ciudad Con Mejor Transporte Verde")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de la ciudad: ")
            energia=int(input("Ingrese consumo de eenergia: "))
            reciclaje=int(input("Ingrese reciclaje: "))
            verde=int(input("Ingrese Transporte Verde: "))
            contaminacion=int(input("Ingrese contaminacion: "))
            indice=((100-energia/4)/100*0.25)+((reciclaje/100)*0.25)+((verde/100)*0.25)+((100-contaminacion)/100*0.25)
            indice=round(indice,2)
            datos[nombre]={"energia":energia,"reciclaje":reciclaje,"verde":verde,"contaminacion":contaminacion,"indice":indice}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nConsumo De Energia: {i["energia"]}\nReciclaje: {i["reciclaje"]}\nTransporte Verde: {i["verde"]}\nContaminacion: {i["contaminacion"]}\nINDICE: {i["indice"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda nombre:datos[nombre]["indice"])
            print(f"La ciudad {mayor} Tiene El Mejor Indice: {datos[mayor]["indice"]}")
        case 4:
            menor=min(datos,key=lambda nombre:datos[nombre]["indice"])
            print(f"La ciudad {menor} Tiene El Peor Indice: {datos[menor]["indice"]}")
        case 5:
            mas=max(datos,key=lambda nombre:datos[nombre]["verde"])
            print(f"La ciudad {mas} Tiene El Transporte Verde: {datos[mas]["verde"]}")