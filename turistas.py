datos=[]
turistas={}
while True:
   print("MENU PRINCIPAL")
   print("1.Registrar Turistas")
   print("2. Buscar Turistas")
   print("3. Eliminar Turistas")
   print("4. Salir")
   op=int(input("Ingrese una opcion: "))
   if op==1:
        cantidad=int(input("Ingrese la cantidad de turistas que va a ingresar: "))
        for i in range(cantidad):
            nombre=input("Ingrese nombre del turista")
            pais=input("Ingrese pais de el turista: ")
            mes=input("Ingrese Mes De Entrada: ")
            turistas={
                "nombre":nombre,
                "pais":pais,
                "mes":mes
            }
            datos.append(turistas)
   elif op==2:
        for i in datos:
            if i["nombre"]=="g":
                (f"Nombre: {i["nombre"]}\nPais: {i["pais"]} ")
        print("1. Buscar Por Pais")
        print("2. Buscar Por mes")
        op=int(input("Ingrese una opcion: "))
        if op==1:
            pais=input("Ingrese el pais que desea filtrar: ")
            print()
            for i in datos:
                if pais in i["pais"]:
                    print(f"Nombre: {i["nombre"]}\nPais: {i["pais"]}\nMes: {i["mes"]} ")
                    print()
        elif op==2:
            mes=input("Ingrese el mes que desea filtrar: ")
            print()
            for i in datos:
                if mes in i["mes"]:
                    print(f"Nombre: {i["nombre"]}\nPais: {i["pais"]}\nMes: {i["mes"]} ")
                    print()
   elif op==3:
       codigo=0
       for i in datos:
         codigo+=1
         print(f"Numero: {codigo} Nombre: {i["nombre"]}\nPais: {i["pais"]}\nMes: {i["mes"]} ")
         print()
       if datos:
         nombre=int(input("Ingrese el numero de turista que desea eliminar: "))
         nombre-=1
         try:
          del datos[nombre]
         except: IndexError
         print("ERROR, INGRESE EL CODIGO CORRECTAMENTE")
         print(f"Se acaba de eliminar de el registro de turistas: {i["nombre"]}")
         print()
       else:
           print("NO HAY TURISTAS REGISTRADOS")
        

