
class Course:
    # Inicializa el curso
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # Devuelve el ID del curso
    def GetId(self):
        return self.id

    # Devuelve el nombre del curso
    def GetName(self):
        return self.name