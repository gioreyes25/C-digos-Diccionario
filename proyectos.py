datos=[]
proyectos={}
codigo=0
while True:
    print("1. Crear Proyectos")
    print("2. Ver Proyectos")
    print("3. Actualizar Estado Del Proyecto")
    print("4. Ver Proyectos por prioridad")
    
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            codigo+=1
            nombre=input("Ingrese Nombre del proyecto: ")
            fechaini=input("Ingrese fecha de inicio: ")
            fechafin=input("Ingrese fecha de finalizacion estimada: ")
            print("1. Pendiente")
            print("2. En Progreso")
            print("3. Finalizado")
            estado=int(input("Ingrese el estado: "))
            if estado==1:
                estado="Pendiente"
            elif estado==2:
                estado="En Progreso"
            elif estado==3:
                estado="Finalizado"
            print("1. Baja")
            print("2. Media")
            print("3. Alta")
            prioridad=int(input("Ingrese Prioridad de el proyecto: "))
            if prioridad==1:
                prioridad="Baja"
            elif prioridad==2:
                prioridad="Media"
            elif prioridad==3:
                prioridad="Alta"
            proyectos={
                "codigo":codigo,
                "nombre":nombre,
                "fechaini":fechaini,
                "fechafin":fechafin,
                "estado":estado,
                "prioridad":prioridad
            }
            datos.append(proyectos)
        case 2:
            for i in datos:
                print(f"Nombre: {i["nombre"]}\n-Codigo: {i["codigo"]}\n-Fecha Inicio: {i["fechaini"]}\n-Fecha Finalizacion Estimada: {i["fechafin"]}\n-Estado: {i["estado"]}\n-Prioridad: {i["prioridad"]}")
        case 3:
            for i in datos: 
                (f"Nombre: {i["nombre"]}\n-Codigo: {i["codigo"]}\n-Fecha Inicio: {i["fechaini"]}\n-Fecha Finalizacion Estimada: {i["fechafin"]}\n-Estado: {i["estado"]}\n-Prioridad: {i["prioridad"]}")
            codigo=int(input("Ingrese el codigo del proyecto que desea actualizar"))
            if i["codigo"]==codigo:
                print(f"Nombre: {i["nombre"]} Estado actual: {i["estado"]}")
                print("1. Pendiente")
                print("2. En Progreso")
                print("3. Finalizado")
                op=int(input("Ingrese una opcion: "))
                if op==1:
                    op="Pendiente"
                elif op==2:
                    op="En Progreso"
                elif op==3:
                    op="Finalizado"
                i["estado"]=op
                print()
                print(f"Ahora el estado es: {i["estado"]}")
                print(f"Nombre: {i["nombre"]} Prioridad Actual: {i["estado"]}")
                print("1. Baja")
                print("2. Media")
                print("3. Alta")
                op=int(input("Ingrese una opcion: "))
                if op==1:
                    op="Baja"
                elif op==2:
                    op="Media"
                elif op==3:
                    op="Alta"
                i["prioridad"]=op
                print(f"Ahora el Prioirdad es: {i["prioridad"]}")
        case 4:
            
                for i in datos:
                    if i["prioridad"]=="Alta":
                        print(f"Nombre: {i["nombre"]}\n-Codigo: {i["codigo"]}\n-Fecha Inicio: {i["fechaini"]}\n-Fecha Finalizacion Estimada: {i["fechafin"]}\n-Estado: {i["estado"]}\n-Prioridad: {i["prioridad"]}")
                    elif i["prioridad"]=="Media":
                        print(f"Nombre: {i["nombre"]}\n-Codigo: {i["codigo"]}\n-Fecha Inicio: {i["fechaini"]}\n-Fecha Finalizacion Estimada: {i["fechafin"]}\n-Estado: {i["estado"]}\n-Prioridad: {i["prioridad"]}")
                    elif i["prioridad"]=="Baja":
                        print(f"Nombre: {i["nombre"]}\n-Codigo: {i["codigo"]}\n-Fecha Inicio: {i["fechaini"]}\n-Fecha Finalizacion Estimada: {i["fechafin"]}\n-Estado: {i["estado"]}\n-Prioridad: {i["prioridad"]}")
