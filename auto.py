class Auto:
    def __init__(self, placa, marca, modelo, descripcion, precio_unitario):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.disponible = True

    def __str__(self):
        return f"{self.placa}, {self.marca}, {self.modelo}, Q{self.precio_unitario:.2f}, {self.descripcion}"
