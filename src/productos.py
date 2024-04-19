#Realizado por Juliana Castillo Araujo
#Parcial 2 
#19 de abril 2024

class Productos:
    def __init__(self,  nombre_producto, valor_producto, cantidad_producto, email, password):
        self.nombre_producto = nombre_producto
        self.valor_producto = valor_producto
        self.cantidad_producto = cantidad_producto
        self.email = email
        self.password = password

    def formato_doc(self):
        return {
            'nombre_producto': self.nombre_producto,
            'valor_producto': self.valor_producto,
            'cantidad_producto': self.cantidad_producto,
            'email': self.email,
            'password': self.password

        }
    
