class finanzas:
    def __init__(self, listaIngresos, listaEgresos):
        self.listaEgresos = listaEgresos
        self.listaIngresos = listaIngresos
        self.dineroEnCuenta = self.getDineroTotal

    def displayIngreso(self):
        for ingreso in self.listaIngresos:
            ingreso.showIngreso()

    def displayEgreso(self):
        for egreso in self.listaEgresos:
            egreso.showEgreso()

    def getDineroTotal(self):
        resultado = 0
        for ingreso in self.listaIngresos:
            ingresos = int(ingreso.getIngreso())
            resultado = resultado + ingresos

        for egreso in self.listaEgresos:
            egresos = int(egreso.getEgreso())
            resultado = resultado - egresos

        print(resultado)
