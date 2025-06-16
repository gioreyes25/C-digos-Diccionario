datos={}
while True:
    print("1. Agregar Mascotas")
    print("2. Ver Mascotas")
    print("3. Filtrar Nombres De Mascotas")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de el dueño")
            nombre=nombre.capitalize()
            mascota=input("Ingrese nombre de la mascota")
            mascota=mascota.capitalize()
            datos[nombre]={"mascota":mascota}
        case 2:
            print(f"Total de mascotas: {len(datos)}")
            for n,i in datos.items():
                print(f"Nombre: {n}\nMascota: {i["mascota"]}")
        case 3:
            l=input("Ingrese letra de la mascota que va a registar: ")
            l=l.capitalize()
            contar=0
            for n,i in datos.items():
                if i["mascota"].startswith(l):
                    contar+=1
                    print(f"Mascota: {i["mascota"]}")
            print(f"Cantidad De Nombres Que Empiezan Con {l}: {contar}")