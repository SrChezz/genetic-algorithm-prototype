class Professor:
    # Inicializa los datos del profesor
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courseClasses = []

    # Devuelve el ID del profesor
    def GetId(self):
        return self.id

    # Devuelve el nombre del profesor
    def GetName(self):
        return self.name

    # Vincula el profesor al curso
    def AddCourseClass(self, courseClass):
        self.courseClasses.append(courseClass)

    # Devuelve la referencia a la lista de clases que imparte el profesor
    def GetCourseClasses(self):
        return self.courseClasses
    
    # Compara los ID de dos objetos que representan profesores
    def __eq__(self, rhs):
        return self.id == rhs.id