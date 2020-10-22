class ingreso:
    def __init__(self, ingreso):
        self.ingreso = ingreso

    def getIngreso(self):
        return self.ingreso

    def showIngreso(self):
        print(f"se ingresaron {self.ingreso} dolares en la cuenta")
