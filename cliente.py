# ++++ zona de clase *****
# se crea la clase 
class cliente:
    # se crea el metodo contructor de la casa 
    def __init__(self):
        # se crean los atributos de la clase 
        self.nombre_cliente = ""
        self.apellido_cliente = ""
    # crear metodos get set por atributos 
    def get_nombre(self):
        return self.nombre_cliente
    
    def get_apellido(self):
        return self.apellido_cliente
    
    def set_nombre(self, dato_nombre):
        self.nombre_cliente = dato_nombre

    def set_apellido(self,dato_apellido):
        self.apeliido_cliente = dato_apellido

    # se crea el metodos normales de la clase 
    def tomar_datos(self):
        self.nombre_cliente = input(" digite el nombre del cliente: ")
        self.apeliido_cliente = input(" digite el apellido del cliente: ")
    def procesar_dato(self):
        aux = self.nombre_cliente + "" + self.apeliido_cliente
    def  mostra_info_cliente(self):
        print(f" nombre del cliente:{self.nombre_cliente}- apellido del cliente: {self.apeliido_cliente} ") 
    def hacer_saludo(self,datossaludo):
        print(f"{datossaludo} : {self.get_nombre}  {self.get_apellido}")
