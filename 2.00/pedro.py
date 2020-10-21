from hello import registro
from main import modificadora

Listapersonas = []
Listapersonas.append(registro("alex", "El salvador"))
Listapersonas.append(registro("ricar", "honduras"))
Listapersonas.append(registro("juan", "guatemala"))
Listapersonas.append(registro("jose", "El salvador"))
Listapersonas.append(registro("pedro", "costa rica"))
Listapersonas.append(registro("roberto", "honduras "))
Listapersonas.append(registro("majano", "El salvador"))


# metodo para clasificarlos
modificadora1 = modificadora()
paisDict = modificadora1.meterpersona(Listapersonas)

for registro in paisDict["El salvador"]:
    print(registro.nombre)
