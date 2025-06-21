datos={
    "Santiago":{"futbol":0},
    "Valparaiso":{"futbol":0},
    "Concepcion":{"futbol":0}
}
partidos={}
fecha=0
while True:
    print("1. Ir a eventos")
    print("2. Ver Tabla")
    print("3. Ver La Mejor Ciudad")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            fecha+=1
            partido=input("Ingrese quien jugara contra quien: (vs)").title()
            cantidad=int(input("Ingrese cantidad de asistentes al partido: "))
            print("-Santiago")
            print("-Valparaiso")
            print("-Concepcion")
            ciudad=input("Ingrese Ciudad en la que se jugara: ").capitalize()
            partidos[fecha]={"partido":partido,"cantidad":cantidad,"ciudad":ciudad}
            for n,i in datos.items():
                if ciudad==n:
                    datos[ciudad]["futbol"]+=cantidad
        case 2:
            for n,i in partidos.items():
                if i["ciudad"]:
                    print(f"Fecha: {n}\nPartido: {i["partido"]}\nEntradas Vendidas: {i["cantidad"]}\nCiudad: {i["ciudad"]}")
                    print()
        case 3:
            mayor=max(datos,key=lambda ciudad:datos[ciudad]["futbol"])
            mas=max(partidos,key=lambda fecha:partidos[fecha]["cantidad"])
            print(f"{mayor} es la ciudad con mas entradas vendidas: {datos[mayor]["futbol"]}\nEl partido que mas aporto entradas fue: {partidos[mas]["partido"]} con {partidos[mas]["cantidad"]} Entradas ")