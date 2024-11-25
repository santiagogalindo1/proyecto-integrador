from project.responsable import Responsable
from project.proyecto import Proyecto


class Organizacion:
    def __init__(self, nombre: str, responsable: Responsable):
        self.nombre = nombre
        self.responsable = responsable
        self.proyectos = []
        self.responsables = [responsable]  # Lista de responsables disponibles

    def agregar_responsable(self, responsable: Responsable):
        self.responsables.append(responsable)
        print(f"Responsable {responsable.nombre} agregado exitosamente.")

    def listar_responsables(self):
        print("\nLista de responsables disponibles:")
        for idx, resp in enumerate(self.responsables, 1):
            print(f"{idx}. {resp.nombre} {resp.apellido}, Cédula: {resp.cedula}")

    def asignar_responsable_a_proyecto(self, id_proyecto: int, idx_responsable: int):
        if 0 < idx_responsable <= len(self.responsables):
            responsable = self.responsables[idx_responsable - 1]
            proyecto = next((p for p in self.proyectos if p.id == id_proyecto), None)
            if proyecto:
                proyecto.asignar_responsable(responsable)
                print(f"Responsable {responsable.nombre} asignado al proyecto {proyecto.nombre}.")
            else:
                print("Proyecto no encontrado.")
        else:
            print("Índice de responsable inválido.")

            
    def agregar_proyecto(self, proyecto: Proyecto):
        self.proyectos.append(proyecto)

    def eliminar_proyecto(self, id_proyecto: int):
        """Elimina un proyecto del portafolio por su ID"""
        proyecto = next((p for p in self.proyectos if p.id == id_proyecto), None)
        if proyecto:
            self.proyectos.remove(proyecto)
            print(f"Proyecto con ID {id_proyecto} eliminado exitosamente.")
        else:
            print(f"No se encontró un proyecto con ID {id_proyecto}.")

    def num_proyectos_completados(self) -> int:
        return sum(1 for proyecto in self.proyectos if proyecto.estado.lower() == "completado")

    def ordenar_proyectos_por_emisiones(self):
        """Ordena los proyectos del portafolio por las emisiones reducidas en orden descendente"""
        self.proyectos.sort(key=lambda p: p.emisiones_reducidas, reverse=True)

    def modificar_estado_proyecto(self, id_proyecto: int, nuevo_estado: str):
        """Modifica el estado de un proyecto por su ID"""
        proyecto = next((p for p in self.proyectos if p.id == id_proyecto), None)
        if proyecto:
            proyecto.cambiar_estado(nuevo_estado)
            print(f"Estado del proyecto '{proyecto.nombre}' actualizado a '{nuevo_estado}'.")
        else:
            print(f"No se encontró un proyecto con ID {id_proyecto}.")

    def ordenar_proyectos_por_impacto(self):
        """Ordena los proyectos en función de su impacto."""
        self.proyectos.sort(key=lambda p: p.calcular_impacto(), reverse=True)
        print("\nProyectos ordenados por impacto:")
        for proyecto in self.proyectos:
            print(f"ID: {proyecto.id}, Nombre: {proyecto.nombre}, Impacto: {proyecto.calcular_impacto()}")

    def calcular_total_emisiones_reducidas(self):
        """Calcula el total de emisiones reducidas por todos los proyectos."""
        total_emisiones = sum(p.emisiones_reducidas for p in self.proyectos)
        print(f"El total de emisiones reducidas por todos los proyectos es: {total_emisiones} toneladas.")
        return total_emisiones

    def contar_proyectos_completados(self):
        """Cuenta el número de proyectos completados y muestra un informe."""
        completados = [p for p in self.proyectos if p.estado.lower() == "completado"]
        print(f"\nNúmero de proyectos completados: {len(completados)}")
        for proyecto in completados:
            print(f"ID: {proyecto.id}, Nombre: {proyecto.nombre}")
        return len(completados)
    

    def mostrar_info(self):
        print(f"Organización: {self.nombre}")
        print("Responsable:")
        self.responsable.mostrar_info()
        print("Proyectos:")
        for proyecto in self.proyectos:
            proyecto.mostrar_info()
            print("-" * 40)