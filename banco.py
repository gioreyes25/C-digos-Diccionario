datos={}
historial={}
cuentas=0
numero=0
while True:
    print("1. Crear Cuenta")
    print("2. Transferir Entre Cuentas")
    print("3. Ver Saldo")
    print("4. Ver Historial De Transacciones")
    print("5. Retirar Dinero")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            cuentas+=1
            codigo=0
            while True:
                id=input("Cree un codigo para su cuenta: ")
                if id not in datos:
                    break
                else:
                    print("ID YA EXISTE")
            nombre=input("Ingrese nombre: ")
            nombre=nombre.capitalize()
            saldo=1000
            datos[id]={"nombre":nombre,"saldo":saldo,"codigo":codigo}
        case 2:
            exit=0
            if cuentas>=2:
                
                for id,i in datos.items():
                    print(f"ID: {id}\nNombre: {i["nombre"]}\nSaldo: {i["saldo"]}")
                    print()
                buscar=input("Ingrese el ID Desde El Se Tranferira")
                for id,i in datos.items():
                    exit+=1
                    if buscar==id:
                        print(f"Nombre: {i["nombre"]}")
                        i["codigo"]+=1
                        Restar1=int(input("Ingrese el monto que va a transferir: "))
                        if Restar1>i["saldo"]:
                            print("El monto excede el saldo que tiene")
                            break
                        else:
                            destinatario1=i["nombre"]
                            i["saldo"]-=Restar1
                            print
                        for id,i in datos.items():
                            if i["codigo"]==0:
                                print(f"ID: {id}\nNombre: {i["nombre"]}\nSaldo: {i["saldo"]}")
                        buscar2=input("Ingrese El ID Que Recibira El Dinero: ")
                        exit=0
                        for id,i in datos.items():
                            exit+=1
                            if buscar2==id: 
                                i["saldo"]+=Restar1
                                print(f"{destinatario1} Le Transfirio ${Restar1} A {i["nombre"]}")
                                numero+=1
                                historial[numero]={"enviado":destinatario1,"monto":Restar1,"recibido":i["nombre"]}
                                exit=0
                                for id,i in datos.items():
                                    i["codigo"]=0
                                break
                            if exit==cuentas and buscar not in id:
                                print("ID Incorrecto1")
                    if exit==cuentas and buscar not in id:
                        print("ID Incorrecto2")
                        break
            else: 
                print("Se necesitan 2 cuentas como minimo para realizar esta operacion")
        case 3:
            for id,i in datos.items():
                print(f"Nombre: {i["nombre"]}\nSaldo: {i["saldo"]}")
        case 4:
            for numero,i in historial.items():
                print(f"NUMERO DE TRANSACCION: {numero}\n{i["enviado"]} Le transfirio {i["monto"]} a {i["recibido"]}")
                print()
            
                    