# clase Cliente
class Cliente:
    def __init__(self, nombre, direccion, rfc):
        self.nombre = nombre
        self.direccion = direccion
        self.rfc = rfc

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def getRfc(self):
        return self.rfc

    def getDatos(self):
        return f'Nombre cliente: {self.nombre}\n' \
               f'Direccion cliente: {self.direccion}\n' \
               f'RFC  cliente: {self.rfc}'
