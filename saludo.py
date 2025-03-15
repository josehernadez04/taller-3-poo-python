from cliente import cliente 

class saludo:
    def __init__ (self):
        self.obj_cliente = cliente()
        
    def hacer_saludo_formar(self):
        mensaje=" buenos saludos formales: "
        return mensaje
    def hacer_despedida_formar(self):
        mensaje = " hasta luego formales "
        return mensaje 