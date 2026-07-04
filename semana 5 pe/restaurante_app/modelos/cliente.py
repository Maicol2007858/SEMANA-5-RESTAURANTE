class Cliente:
    def __init__(self, nombre: str, edad: int, socio: bool):
        self.nombre = nombre
        self.edad = edad
        self.socio = socio

    def __str__(self):
        tipo = "Socio" if self.socio else "Cliente normal"
        return f"Cliente: {self.nombre} | Edad: {self.edad} | Tipo: {tipo}"