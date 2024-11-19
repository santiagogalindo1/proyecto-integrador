class Responsable:
    def __init__(self, dni: str, nombre: str, apellido: str, email: str, telefono: str):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def mostrar_info(self):
        print(f"DNI: {self.dni}, Nombre: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}")
