datos={}
ciu={}
while True:
    print("1. Agregar persona")
    print("2. Ver todas las personas")
    print("3. Ver cuántas personas hay por ciudad")
    print("4. Buscar comidas que comienzan con una letra")
    print("5. Mostrar el nombre más corto registrado")
    print("0. Salir")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese su nombre: ")
            ciudad=input("Ingrese su ciudad")
            ciudad=ciudad.capitalize()
            comida=input("Ingrese una comida: ")
            datos[nombre]={"ciudad":ciudad,"comida":comida}
            ciuda=1
            if ciudad not in ciu:
                ciu[ciudad]={"contador":ciuda}
            elif ciudad in ciu:
                ciuda+=1
                ciu[ciudad]={"contador":ciuda}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nCiudad: {i["ciudad"]}\nComida: {i["comida"]}")
        case 3:
            for c,i in ciu.items():
                print(f"Hay {i["contador"]} En La Ciudad: {c}")
        case 4:
            l=input("Ingrese letra que desea buscar: ")
            for n,i in datos.items():
                if i["comida"].lower.startswith(l):
                    print(f"Nombre: {n}\nCiudad: {i["ciudad"]}\nComida: {i["comida"]}")
        case 5:
            Corto=min(datos,key=len)
            print(f"El Nombre mas corto registrado es: {Corto}")