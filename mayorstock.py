inventario = {
    "Sucursal_A": {
        "Laptop": 10,
        "mouse": 25,
        "Teclado": 12
    },
    "Sucursal_B": {
        "Laptop": 5,
        "mouse": 30,
        "Teclado": 10,
    },
    "Sucursal_C": {
        "Laptop": 7,
        "Teclado": 5,
    }
}

datos = {}

while True:
    print(datos)
    print("1. Calcular stock total por producto")
    op = int(input("Ingrese una opción: "))
    
    match op:
        case 1:
            for sucursal, productos in inventario.items():
                for producto, cantidad in productos.items():
                    if producto not in datos:
                        datos[producto] = {"total": 0}
                    datos[producto]["total"] += cantidad
