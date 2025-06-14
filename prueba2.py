
libros={}
while True:
    print("1. Agregar Libros")
    print("2. Buscar Libro")
    op=input("Ingrese una opcion: ")
    match op:
        case "1":
            nombre=input("Ingrese el nombre: ")
            while True:
                try:
                    año=int(input("Ingrese año de el libro: "))
                    break
                except: ValueError
                print()
                print("Solo se permiten Numeros")
            codigo=input("Ingrese codigo: ")
            info={
                "codigo":codigo,
                "nombre":nombre,
                "año":año
            }
            print(info)
        case "2":
            codigo=input("Ingrese el codigo de el libro: ")
            for i in info:
                if codigo==i["codigo"]:
                    print(f"Nombre: {i["nombre"]}\nAño: {i["año"]}")
                    print()
                
            