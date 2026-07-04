class Producto:
    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Estado: {estado}"