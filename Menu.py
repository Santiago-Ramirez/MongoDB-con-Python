import Interface
import Cliente
from ConexionMongo import mongoConexion

# clase Menu
class Menu:
    def __init__(self):
        self.stop = False
        self.interface = Interface.Interface()
        self.mongo = mongoConexion()

    def agregarEmpresa(self):
        nombreEmpresa = input('Ingrese el nombre de la empresa:\n').upper()
        direccionEmpresa = input('Ingrese la dirección de la empresa:\n').upper()
        rfcEmpresa = input('Ingrese el rfc de la empresa:\n').upper()

        self.interface.setEmpresa(nombreEmpresa, direccionEmpresa, rfcEmpresa)
        ultimaEmpresa = self.interface.getLastEmpresa()

        print(f'''

        Se agrego la empresa: {ultimaEmpresa.getNombre()}
        con direccion: {ultimaEmpresa.getDireccion()}
        RFC: {ultimaEmpresa.getRfc()}

        ''')

        empresa = self.mongo.guardarEmpresa(nombreEmpresa,direccionEmpresa,rfcEmpresa)

        #self.mongo.guardarClient(nombre,direccion,rfc)
        print(empresa['_id'])
        self.agregarClientesEmpresa(ultimaEmpresa, empresa['_id'])

    def agregarClientesEmpresa(self, empresaAgregarClientes, idempresa ):

        stopLlenadoClientes = False
        empresa = empresaAgregarClientes
        print('Proceda a ingresar los clientes')

        while not stopLlenadoClientes:
            cancelar = False

            if empresa.getCantidadClientes() > 0:

                respuestaCorrecta = False

                while not respuestaCorrecta:
                    _input = input('Desea seguir agregando más clientes(S/N):\n').upper()

                    if _input == 'N':
                        cancelar = True
                        stopLlenadoClientes = True
                        respuestaCorrecta = True
                    elif _input == 'S':
                        respuestaCorrecta = True

            if not cancelar:
                nombreCliente = input('Ingrese el nombre del cliente:\n').upper()
                direccionCliente = input('Ingrese la direccion del cliente:\n').upper()
                rfcCliente = input('Ingrese el rfc del cliente:\n').upper()
                cliente = Cliente.Cliente(nombreCliente,direccionCliente,rfcCliente)
                empresa.setCliente(cliente)
                print(f'''
                Se ingresó al cliente:

                {cliente.getDatos()}

                ''')
                self.mongo.guardarClient(nombreCliente, direccionCliente, rfcCliente, idempresa)

    def setOperacion(self):
        _input = input()

        if _input.upper() == '1':
            self.agregarEmpresa()


        elif _input.upper() == '2':

            if len(self.interface.getEmpresas()) > 0:
                for empresa in self.interface.getEmpresas():
                    print(f'''
                    Empresa: {empresa.nombre}.
                    Direccion: {empresa.direccion}.
                    Clientes:''')
                    for cliente in empresa.getClientes():
                        print(f'{cliente.getDatos()}')
            else:
                print('No hay empresas registradas. Regístre una/varias empresa(s) antes de visualizarla(s).')

        elif _input.upper() == '3':
            cancelar = False

            while not cancelar:
                continuar = False
                while not continuar:
                    nombreCliente = input('Ingrese el nombre del cliente:\n')

                    cliente = self.mongo.verificarCliente(nombreCliente)

                    if cliente[0]:
                        continuar = True
                    else:
                        print('Cliente no existe')
                        continuar = False

                listoProducto = False
                productosComprados = []
                while not listoProducto:
                    self.mongo.mostrarProduco()
                    producto = input('Ingrese el nombre del producto a comprar:\n')
                    productosComprados.append(producto)
                    condicion = input('Desea comprar mas productos?: (s/n)\n').upper()

                    if condicion == 'n' or condicion == 'N':
                        listoProducto = True
                        cancelar = True
                    elif condicion == 's' or condicion == 'S':
                        listoProducto = False
            self.mongo.comprarProducto(cliente[1], productosComprados)

        elif _input.upper() == '4':
            self.stop = True
            print('Adios')

    def getMenu(self):
        print('''
            ¿Qué desea hacer? Ingrese el numero para
            1) Agregar empresa
            2) Imprimir empresas
            3) Comprar productos
            4) Salir
        ''')

    def getDBPrompt(self):

        respuestaCorrecta = False


        while not respuestaCorrecta:
            _input = input('''
            ¿Qué base de datos desea utilizar?
            1) Mysql
            2) MongoDB
            ''').upper()

            if _input == '1' or _input == '2':
                respuestaCorrecta = True

        self.interface.startConnection(_input)

    def run(self):
        while not self.stop:
            self.getDBPrompt()
            self.getMenu()
            self.setOperacion()

