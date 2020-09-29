"""
cliente:
    quiero escribir un programa python que reciba de input del usuario
    un nombre, un producto, costo
    y se guarde en una lista con diccinarios, el registro es un diccionario
    y va a ser guardado en una lista
programador:
    vaya

cliente:
    mira me gusta pero cada vez que inicio el programa, me borra el cliente anterior
    y solo puedo guardar el que he ingresado en ese momento, no habria forma de
    que se guarde a los 3 clientes que tengo?
programador:
    vaya
mente:
    y pollo no queres?

cliente:
    mira esta buenisimo peeeerroooooo, fijate que mi clientela a aumentado a veces tengo
    3 a veces 5  a veces 10 osea ya no se cuantos clientes tendre en un dia, podrias
    agregarle alguna forma de que yo le diga cuando quiero que se detenga y que me muestre
    el reporte de lo que llevo en costo total hasta ese momento.
programador:
    vaya
mente:
    no te pide nada el gusto mono


"""
listaRegistro = []
respuesta = ""
costoTotal = 0

cliente = input("nombre del cliente: ")
producto = input("producto: ")
costo = float(input("costo ($0.00): "))
registro = dict(cliente=cliente, producto=producto, costo=costo)
listaRegistro.append(registro)
costoTotal += costo

while respuesta != "no":
    print("¿quieres colocar alguien nuevo en tu lista?")
    respuesta = input("escribe si o no: ")

    if respuesta == "si":

        cliente = input("nombre del cliente: ")
        producto = input("producto: ")
        costo = float(input("costo ($0.00): "))
        registro = dict(cliente=cliente, producto=producto, costo=costo)
        listaRegistro.append(registro)
        costoTotal += costo

    if respuesta != "si" and respuesta != "no": 

        print("no te he entendido, por favor escribelo de nuevo")
        

for registro in listaRegistro:
    print(registro)
print("el costo total ha sido de " + str(costoTotal))

#en mi programa el usuario tiene la capacidad de decidir si habra otro cliente o no. 
# sin embargo,si su respuesta es diferente a si o no porque tuvo un error de dedo,
# el prgrama le señala el error y pregunta hasta que se coloca correctamente 
