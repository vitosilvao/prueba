pacientes=[]



while(True):
    print("Hospital Nacional")
    print("Menu")
    print("1.- Registrar cobro")
    print("2.- Listar cobros registrados")
    print("3.- Definir sector de despacho")
    print("4.- Salir del programa")

    opc=int(input("Ingrese una opcion valida: "))


    if (opc==1):


        
        nombre=input("Ingrese el nombre: ")
        direccion=input("ingrese la direccion de domicilio: ")
        dias=int(input("ingrese los dias hospitalizados: "))
        valor_dia=90000
        hospitalizacion=dias*valor_dia
        valor_hospitalizacion=print(f"el monto por concepto de hospitalizaion es: ${hospitalizacion}")
        monto_insumos=int(input("ingrese valor de insumos: $"))
        total_dias=monto_insumos + hospitalizacion
        total_dias_hospi=print(f"El valor total de la hospitalizacion: ${total_dias} ")
            
        bonificacion=int(input("Cual es su porcentaje de bonificacion? "))
        bonificacion=bonificacion/100
        valor_bonificacion=total_dias*bonificacion
        total_pagar=total_dias-(total_dias*bonificacion)
        print(f"el total a pagar es: ${total_pagar}")

        paciente={
                "Nombre": nombre,
                "Direccion": direccion,
                "Hospitalizacion": hospitalizacion,
                "Insumos": monto_insumos,
                "Bonificacion": valor_bonificacion,
                "Total": total_pagar

                }
        pacientes.append(paciente)
        

        paciente={
                "Nombre": nombre,
                "Direccion": direccion,
                "Hospitalizacion": hospitalizacion,
                "Insumos": monto_insumos,
                "Bonificacion": valor_bonificacion,
                "Total": total_pagar

                }
        pacientes.append(paciente)
        

    paciente={
            "Nombre": nombre,
            "Direccion": direccion,
            "Hospitalizacion": hospitalizacion,
            "Insumos": monto_insumos,
            "Bonificacion": valor_bonificacion,
            "Total": total_pagar

            }
    pacientes.append(paciente)
    

    if (opc==2):
        print("Lista de cobros registrados")
        print(pacientes)
    
    if (opc==3):
        
        paciente_buscado=input("ingrese el nombre del paciente" )
        sector=input("ingrese el sector de cobro: C: Centro N: Norte S: Sur").upper()
        
            
        for i in range(pacientes):
            if paciente_buscado==[i][pacientes]:
                if sector=="C":
                archivo.write(paciente.txt)
        

        