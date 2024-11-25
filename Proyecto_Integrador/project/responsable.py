class Responsable:
    def __init__(self, nombre: str, apellido: str, cedula: str):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def modificar_datos(self, nombre=None, apellido=None, cedula=None):
        """Permite modificar los datos del responsable."""
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if cedula:
            self.cedula = cedula

    def mostrar_info(self):
        print(f"Responsable: {self.nombre} {self.apellido}, Cédula: {self.cedula}")
