
def factura():
    monto=float(input("Ingrese su monto a pagar: $"))
    IVA=int(input("Ingrese el valor del IVA: "))
    if IVA != 0:
        if IVA>0:
            totalPagar=((monto*IVA) / 100) + monto
            return totalPagar
        else:
            print("¡Lo siento!, el IVA no puede ser negativo.")
    else:
        totalPagar=(monto*0.21) + monto
        return totalPagar
print("El total de su factura es de: $",factura())




