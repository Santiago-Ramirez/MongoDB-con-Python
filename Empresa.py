import Cliente

# clase empresa
class Empresa:
    # constructor
    def __init__(self, nombre, direccion, rfc, id):
        self.clientes = []
        self.nombre = nombre
        self.direccion = direccion
        self.rfc = rfc
        self.id = id

    # traer los clientes de la instancia de la empresa
    def getClientes(self):
        return self.clientes

    # traer el nombre de la empresa
    def getNombre(self):
        return self.nombre

    # traer la dirección de la empresa
    def getDireccion(self):
        return self.direccion

    # traer el rfc de la empresa
    def getRfc(self):
        return self.rfc

    # set (agregar) cliente a la empresa
    def setCliente(self, cliente):
        self.clientes.append(cliente)

    def getCantidadClientes(self) -> int:
        return len(self.clientes)

