pacientes=[]

def ingreso(nombre, direccion, dias, valor_dia, hospitalizacion, monto_insumos, total_dias, bonificacion, valor_bonificacion, total_pagar ):
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
    