from project.responsable import Responsable

class Proyecto:
    def __init__(self, id: int, nombre: str, tipo: str, ubicacion: str, responsable: Responsable, emisiones_reducidas: float, energia_generada: float, estado: str):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.responsable = responsable  # Asignación dinámica del responsable
        self.emisiones_reducidas = emisiones_reducidas
        self.energia_generada = energia_generada
        self.estado = estado

    def actualizar_emisiones(self, emisiones: float):
        self.emisiones_reducidas = emisiones

    def cambiar_estado(self, estado: str):
        self.estado = estado

    def asignar_responsable(self, responsable: Responsable):
        self.responsable = responsable  # Método para asignar un responsable a un proyecto

    def calcular_impacto(self):
        """Calcula el impacto del proyecto como la suma de emisiones reducidas y energía generada."""
        return self.emisiones_reducidas + self.energia_generada

    def mostrar_info(self):
        print(f"Proyecto: {self.nombre} (ID: {self.id})")
        print(f"Tipo: {self.tipo}, Ubicación: {self.ubicacion}")
        print(f"Emisiones reducidas: {self.emisiones_reducidas}, Energía generada: {self.energia_generada}")
        print(f"Estado: {self.estado}")
        print
        self.responsable.mostrar_info()
