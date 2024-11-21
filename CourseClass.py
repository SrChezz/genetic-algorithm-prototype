import Professor
import StudentsGroup
import Course

class CourseClass:

    # Inicializa el objeto de clase
    def __init__(self, professor, course, groups, requiresLab, duration):
        self.professor = professor
        self.course = course
        self.numberOfSeats = 0
        self.requiresLab = requiresLab
        self.duration = duration
        self.groups = groups
        
        # Vincula el profesor a la clase
        self.professor.AddCourseClass(self)

        # Vincula los grupos de estudiantes a la clase
        groupLength = len(self.groups)
        for i in range(groupLength): 
            self.groups[i].AddClass(self)
            self.numberOfSeats = self.numberOfSeats + StudentsGroup.StudentsGroup.GetNumberOfStudents(self.groups[i])
            
    # Devuelve True si otra clase tiene uno o más grupos de estudiantes que se solapan
    def GroupsOverlap(self, c):
        for grKey in self.groups:
            for cKey in c.groups:
                if grKey == cKey:
                    return True
        return False

    # Devuelve True si otra clase tiene el mismo profesor
    def ProfessorOverlaps(self, c):
        return self.professor == c.professor

    # Devuelve el puntero al profesor que imparte la clase
    def GetProfessor(self):
        return self.professor

    # Devuelve el puntero al curso al que pertenece la clase
    def GetCourse(self):
        return self.course

    # Devuelve la referencia a la lista de grupos de estudiantes que asisten a la clase
    def GetGroups(self): 
        return self.groups

    # Devuelve el número de asientos (estudiantes) requeridos en el aula
    def GetNumberOfSeats(self):
        return int(self.numberOfSeats)

    # Devuelve True si la clase requiere computadoras en el aula
    def IsLabRequired(self):
        return self.requiresLab

    # Devuelve la duración de la clase en horas
    def GetDuration(self):
        return int(self.duration)