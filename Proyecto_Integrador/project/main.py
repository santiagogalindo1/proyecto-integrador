from responsable import Responsable
from proyecto import Proyecto
from organizacion import Organizacion

# Crear un responsable
responsable_1 = Responsable("12345678", "Juan", "Pérez", "juan.perez@email.com", "123456789")

# Crear proyectos
proyecto_1 = Proyecto(1, "Proyecto Solar", "Energía", "Madrid", responsable_1, 100.0, 500.0, "en curso")
proyecto_2 = Proyecto(2, "Proyecto Eólico", "Energía", "Barcelona", responsable_1, 200.0, 1000.0, "completado")

# Crear organización
organizacion = Organizacion("EcoEnergía", responsable_1)
organizacion.agregar_proyecto(proyecto_1)
organizacion.agregar_proyecto(proyecto_2)

# Mostrar información de la organización
organizacion.mostrar_info()

# Mostrar proyectos completados
print(f"Número de proyectos completados: {organizacion.num_proyectos_completados()}")

# Ordenar y mostrar proyectos por emisiones reducidas
organizacion.ordenar_proyectos_por_emisiones()
organizacion.mostrar_info()
