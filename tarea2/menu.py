from egreso import egreso
from ingreso import ingreso
from finanzas import finanzas


listaIngresos = []
listaEgresos = []

while True:

    print(
        "--------------------------------------------------------------------------------------------"
    )
    print("                                 BIENVENIDO A A TU CUENTA PERSONAL")
    print(
        "----------------------------------------------------------------------------------------------"
    )
    print("              1.registrar un ingreso")
    print("              2.registrar un egreso")
    print("              3.mostrar reporte de ingresos")
    print("              4.mostrar reporte de egresos")
    print("              5.mostrar ingresos y egresos")
    print("              6.mostrar el dinero total en la cuenta")
    print("              0.salir")
    print(
        "----------------------------------------------------------------------------------------------"
    )

    respuesta = input("escribe cual de las opciones deseas realizar:")

    print("------------------------------------------------------------")

    finanzas1 = finanzas(listaIngresos, listaEgresos)

    if respuesta == "1":
        cantidad = 0
        cantidad = Cantidad = int(input("cuanto dinero desea abonar a la cuenta:"))
        listaIngresos.append(ingreso(Cantidad))

    if respuesta == "2":
        cantidad = 0
        Cantidad = int(input("cuanto dinero desea retirar:"))
        listaEgresos.append(egreso(Cantidad))

    if respuesta == "3":
        finanzas1.displayIngreso()
        print("                                                        ")

    if respuesta == "4":
        finanzas1.displayEgreso()

    if respuesta == "5":
        print("tus ingresos han sido los siguientes: ")
        finanzas1.displayIngreso()
        print("tus egresos son los siguientes:")
        finanzas1.displayEgreso()

    if respuesta == "6":
        print("el dinero total de la cuenta en dolares es de: ")
        finanzas1.getDineroTotal()

    if respuesta == "0":
        break
