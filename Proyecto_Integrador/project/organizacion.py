from proyecto import Proyecto
from responsable import Responsable

class Organizacion:
    def __init__(self, nombre: str, responsable: Responsable):
        self.nombre = nombre
        self.responsable = responsable
        self.proyectos = []

    def agregar_proyecto(self, proyecto: Proyecto):
        self.proyectos.append(proyecto)

    def num_proyectos_completados(self) -> int:
        return sum(1 for proyecto in self.proyectos if proyecto.estado.lower() == "completado")

    def ordenar_proyectos_por_emisiones(self):
        self.proyectos.sort(key=lambda p: p.emisiones_reducidas, reverse=True)

    def mostrar_info(self):
        print(f"Organización: {self.nombre}")
        print("Responsable:")
        self.responsable.mostrar_info()
        print("Proyectos:")
        for proyecto in self.proyectos:
            proyecto.mostrar_info()
            print("-" * 40)
