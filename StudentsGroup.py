class StudentsGroup:

    # Inicializa los datos del grupo de estudiantes
    def __init__(self, id, name, numberOfStudents):
        self.id = id
        self.name = name
        self.numberOfStudents = numberOfStudents
        self.courseClasses = []
        
    # Vincula el grupo a una clase
    def AddClass(self, courseClass):
        self.courseClasses.append(courseClass)

    # Devuelve el ID del grupo de estudiantes
    def GetId(self):
        return self.id

    # Devuelve el nombre del grupo de estudiantes
    def GetName(self):
        print(str(self.name))
        return str(self.name)

    # Devuelve el número de estudiantes en el grupo
    def GetNumberOfStudents(self):
        return int(self.numberOfStudents)

    # Devuelve una referencia a la lista de clases a las que asiste el grupo
    def GetCourseClasses(self):
        return self.courseClasses

    # Compara los ID de dos objetos que representan grupos de estudiantes
    def __eq__(self, rhs):
        return self.id == rhs.id