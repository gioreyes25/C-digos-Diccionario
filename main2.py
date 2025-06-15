
frutas = {
    1:{ "nombre": "Manzana", "valor":150},
    2:{ "nombre": "Platano", "valor":200},
    3:{ "nombre": "Pera", "valor":120},
    4:{ "nombre": "Melon", "valor":400},
    5:{ "nombre": "Sandia", "valor":500}
}

galletas={
    "1": "Triton",
    "2": "Frac",
    "3": "Oreo"
}

listaprodu=[]
listacanti=[]
listavalor=[]
lista=[]
saldo=2000
total=0
cantidad=0
veces=0
op=2
while op!=0:
    print("1. Frutas")
    print("2. Galletas")
    print("3. Resumen De Compra")
    print("0. Salir")
    op=int(input("Ingrese Opcion: "))
    if op==1:
        for codigo,datos in frutas.items():
            print(f"{codigo}. {datos['nombre']} - ${datos['valor']}")
        print
        ele=int(input("Ingrese un producto"))
        if ele==codigo:
            cantidad=int(input("Ingrese Cantidad que desea: "))
            producto=frutas[ele]["nombre"]
            valora=frutas[ele]["valor"]
            lista.append((producto,cantidad,valora))
            total+=valora*cantidad
            veces+=cantidad
            print(f"Cantidad: {veces} Producto: {producto} Valor: {valora}")
            print(f"SUBOTAL: {total}")
        elif ele>5:
                print("Producto No Encontrado")
    elif op==3:
        for item in lista:
            print(f"Producto: {item[0]}, Cantidad: {item[1]}, Valor unitario: {item[2]}, Subtotal: {item[1] * item[2]}")