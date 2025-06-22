datos={}
import heapq
while True:
    print("1. Agregar Pelicula")
    print("2. Ver List De Peliculas")
    print("3. Comprar Entradas")
    print("4. Eliminar Pelicula")
    print("5. Ver Las Mejores Peliculas")
    op=int(input("Ingrese una op: "))
    match op:
        case 1:
            peli=input("Ingrese nombre de la pelicula").capitalize()
            año=int(input("Ingrese año de la pelicula: "))
            datos[peli]={"año":año,"total":0}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nAño: {i["año"]}")
        case 3:
            for n,i in datos.items():
                print(f"Nombre: {n}\nAño: {i["año"]}")
            elegir=input("Ingrese nombre de pelicula que desea: ").capitalize()
            if elegir in datos:
                entradas=int(input("Ingrese cantidad de entradas: "))
                datos[elegir]["total"]+=entradas
                print(f"Se han comprado {entradas} Entradas Para La Pelicula {n}")
        case 4:
            for n,i in datos.items():
                print(f"Nombre: {n}\nAño: {i["año"]}")
            peli=input("Ingrese pelicula que desa eliminar: ").capitalize()
            if peli in datos:
                del datos[peli]
                print(f"Se ha eliminado la pelicula {peli}")
        case 5:
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["total"])
            for i, (n,v) in enumerate(top,start=1):
                print(f"{i} {n} {v["total"]}")