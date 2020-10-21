class modificadora:
    def meterpersona(self, listapersonas):

        casillas = self.clasificarPais()

        for registro in listapersonas:
            if registro.pais == "El salvador":
                casillas["El salvador"].append(registro)

            elif registro.pais == "honduras":
                casillas["honduras"].append(registro)

            elif registro.pais == "Guatemala":
                casillas["guatemala"].append(registro)

            elif registro.pais == "costa rica":
                casillas["costa rica"].append(registro)

        return casillas

    def clasificarPais(self):
        paisDict = {}
        paisDict["El salvador"] = []
        paisDict["honduras"] = []
        paisDict["guatemala"] = []
        paisDict["costa rica"] = []

        return paisDict
