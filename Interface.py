import Empresa
import MysqlConnection


# clase Interface
class Interface:

    connection: None

    def __init__(self):
        self.empresas = []
        self.empresasCount = len(self.empresas)

    def setEmpresa(self, nombreEmpresa: str, direccionEmpresa: str, rfcEmpresa: str):
        empresa = Empresa.Empresa(nombreEmpresa, direccionEmpresa, rfcEmpresa, self.empresasCount)
        self.empresas.append(empresa)

    def getLastEmpresa(self) -> Empresa:
        ultimaEmpresa = self.empresas[self.empresasCount]
        self.empresasCount += 1
        return ultimaEmpresa

    def getEmpresas(self):
        return self.empresas

    def startConnection(self, eleccion: str):

        if eleccion == '1':

            self.connection = MysqlConnection.MysqlConnection.get_instance()
            self.connection.set_connection('localhost','root','','ejercicio3')

            # esperando la clase de ubaldo
            # elif eleccion == '2':
            # self.connection = clase de ubaldo para mongodb
            pass
