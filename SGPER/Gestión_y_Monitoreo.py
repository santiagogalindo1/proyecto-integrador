class Organisacion :
    def __init__(self, nombre, responsable, proyectos):
        self.nombre = nombre
        self.responsable = responsable
        self.proyectos = []

    def agregar_proyecto(self, nombre, descripcion):
        nuevo_proyecto = Proyecto(nombre)
        self.proyectos.append(nuevo_proyecto)
        print(f'Proyecto "{nombre}" agregado exitosamente.')    

    



class responsable :
    def __init__(self, DNI, nombre, apellido, email, telefono ):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono


    

    def get_info(self):
          return f"DNI: {self.DNI}, Nombre: {self.nombre} {self.apellido}, Email: {self.email}, Teléfono: {self.telefono}"

          


class Proyecto : 
    def __init__(self, id_proyecto, nombre_proyecto, tipo, ubicación, responsable, emisiones_reducidas, energia_generada, estado):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.tipo = tipo
        self.ubicación = ubicación
        self.responsable = responsable
        self.emisiones_reducidas = emisiones_reducidas
        self.estado = estado
        self.energia_generada = energia_generada