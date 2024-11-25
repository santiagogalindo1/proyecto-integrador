from project.responsable import Responsable
from project.proyecto import Proyecto
from project.organizacion import Organizacion

# Crear un responsable por defecto
responsable_principal = Responsable("Sam", "Ortiz", "12345")
organizacion = Organizacion("*GreenTech Global*", responsable_principal)

def mostrar_menu():
    print("\n**** GreenTech Global ****")
    print("  **** Menú principal ****")
    print("1. Crear un proyecto")
    print("2. Mostrar proyectos creados")
    print("3. Actualizar el estado de un proyecto")
    print("4. Eliminar un proyecto")
    print("5. Agregar un nuevo responsable")
    print("6. Asignar responsable a un proyecto")
    print("7. Ordenar proyectos por impacto")
    print("8. Calcular el total de emisiones reducidas")
    print("9. Total proyectos completados")
    print("10. Salir")
    return input("Seleccione una opción: ")

def crear_proyecto():
    try:
        id = int(input("Ingrese el ID del proyecto: "))
        nombre = input("Ingrese el nombre del proyecto: ").strip()
        tipo = input("Ingrese el tipo de proyecto (solar, eólica, geotérmica): ").strip()
        ubicacion = input("Ingrese la ubicación del proyecto: ").strip()
        emisiones_reducidas = float(input("Ingrese las emisiones reducidas para el proyecto: "))
        energia_generada = float(input("Ingrese la energía generada para el proyecto: "))
        estado = input("Ingrese el estado inicial del proyecto (en curso, completado, pendiente): ").strip()

        if any(p.id == id for p in organizacion.proyectos):
            raise ValueError(f"El ID {id} ya está asignado a otro proyecto.")

        if not nombre or not tipo or not ubicacion or not estado:
            raise ValueError("Todos los campos son obligatorios.")
        
        # Listar responsables disponibles
        print("\nResponsables disponibles:")
        organizacion.listar_responsables()

        # Seleccionar responsable
        idx_responsable = int(input("Seleccione el número del responsable para el proyecto: "))
        if not (1 <= idx_responsable <= len(organizacion.responsables)):
            raise ValueError("Número de responsable no válido.")
        
        responsable = organizacion.responsables[idx_responsable - 1]

        # Crear y agregar el proyecto
        nuevo_proyecto = Proyecto(id, nombre, tipo, ubicacion, responsable, emisiones_reducidas, energia_generada, estado)
        organizacion.agregar_proyecto(nuevo_proyecto)
        print(f"Proyecto '{nombre}' creado exitosamente con el responsable '{responsable.nombre} {responsable.apellido}'.")
    except ValueError as ve:
        print(f"Error: {ve}. Por favor, intente nuevamente.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def revisar_proyectos():
    try:
        if not organizacion.proyectos:
            print("No hay proyectos registrados.")
        else:
            organizacion.mostrar_info()
    except Exception as e:
        print(f"Error al revisar proyectos: {e}")

def modificar_estado():
    try:
        id_proyecto = int(input("Ingrese el ID del proyecto a modificar: "))
        nuevo_estado = input("Ingrese el nuevo estado (en curso, completado, pendiente): ").strip()
        if nuevo_estado not in ["en curso", "completado", "pendiente"]:
            raise ValueError("El estado ingresado no es válido.")

        organizacion.modificar_estado_proyecto(id_proyecto, nuevo_estado)
    except ValueError as ve:
        print(f"Error: {ve}. Por favor, intente nuevamente.")

    except Exception as e:
        print(f"Error inesperado: {e}")

def eliminar_proyecto():
    try:
        id_proyecto = int(input("Ingrese el ID del proyecto a eliminar: "))
        organizacion.eliminar_proyecto(id_proyecto)
    except ValueError as ve:
        print(f"Error: {ve}. Por favor, intente nuevamente.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def agregar_responsable():
    try:
        nombre = input("Ingrese el nombre del nuevo responsable: ").strip()
        apellido = input("Ingrese el apellido: ").strip()
        cedula = input("Ingrese la cédula: ").strip()

        if not nombre or not apellido or not cedula:
            raise ValueError("Todos los campos son obligatorios.")

        nuevo_responsable = Responsable(nombre, apellido, cedula)
        organizacion.agregar_responsable(nuevo_responsable)
    except ValueError as ve:
        print(f"Error: {ve}. Por favor, intente nuevamente.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def asignar_responsable_a_proyecto():
    try:
        organizacion.listar_responsables()
        id_proyecto = int(input("\nIngrese el ID del proyecto: "))
        idx_responsable = int(input("Seleccione el número del responsable a asignar: "))
        organizacion.asignar_responsable_a_proyecto(id_proyecto, idx_responsable)
    except ValueError as ve:
        print(f"Error: {ve}. Por favor, intente nuevamente.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def procesar_opcion(opcion):
    if opcion == "1":
        crear_proyecto()
    elif opcion == "2":
        revisar_proyectos()
    elif opcion == "3":
        modificar_estado()
    elif opcion == "4":
        eliminar_proyecto()
    elif opcion == "5":
        agregar_responsable()
    elif opcion == "6":
        asignar_responsable_a_proyecto()
    elif opcion == "7":
        organizacion.ordenar_proyectos_por_impacto()
    elif opcion == "8":
        organizacion.calcular_total_emisiones_reducidas()
    elif opcion == "9":
        organizacion.contar_proyectos_completados()
    elif opcion == "10":
        print("¡Hasta luego!")
        return False
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
    return True

# Ciclo principal 
while True:
    opcion = mostrar_menu()
    if not procesar_opcion(opcion):
        break
