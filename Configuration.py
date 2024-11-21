import Professor
import StudentsGroup
import Course
import Room
import CourseClass

# Lee el archivo de configuración y analiza objetos
class Configuration:

    global instance
    
    # Initialize data
    def __init__(self):
        self.isEmpty = True
        self.professors = {}
        self.studentGroups = {}
        self.courses = {}
        self.rooms = {}
        self.courseClasses = []

        Room.Room.RestartIDs()

    # Devuelve una referencia a la instancia global de la configuración
    def GetInstance():
        instance = Configuration()
        return instance

    # Analiza archivo y recoge los obejtos
    def Parsefile(self, fileName):
        # Limpia los obejtos anteriormente recogidos
        self.professors = {}
        self.studentGroups = {}
        self.courses = {}
        self.rooms = {}
        self.courseClasses = []

        Room.Room.RestartIDs()

        # abrir archivo
        counter = 0
        with open(fileName, "r") as input:
            for line in input:
                counter = counter + 1
                # Retornar tipo de objeto, transforma objeto y lo guarda
                strippedLine = line.strip()
                if strippedLine == '#prof':
                    p = self.__ParseProfessor(input)
                    if p:
                        self.professors[p.GetId()] = p
                elif strippedLine == '#group':
                    g = self.__ParseStudentsGroup(input)
                    if g:
                        self.studentGroups[g.GetId()] = g
                elif strippedLine == '#course':
                    c = self.__ParseCourse(input)
                    if c:
                        self.courses[c.GetId()] = c
                elif strippedLine == '#room':
                    r = self.__ParseRoom(input)
                    if r:
                        self.rooms[r.GetId()] = r
                elif strippedLine == '#class':
                    c = self.__ParseCourseClass(input)
                    if c:
                        self.courseClasses.append(c)
        input.close()
        self.isEmpty = False
        
    # Retorna puntero hacia el profesor con una ID especifico
    # Si no existe un profesor con ID retona NULL
    def GetProfessorById(self, id):
        if id in self.professors.keys():
            return self.professors[id]
        return None
    
    # Retorna la cantidad de profesores recogidos
    def GetNumberOfProfessors(self):
        return len(self.professors.keys())

    # Retorna puntero hacia el estudiante con una ID especifica
    # Si un grupo de estudiantes no existe con dicha ID, el método retorna NULL
    def GetStudentsGroupById(self, id):
        if id in self.studentGroups.keys():
            return self.studentGroups[id]
        return None    
        
    # Retorna número de grupos de estudiantes recogidos
    def GetNumberOfStudentGroups(self):
        return len(self.studentGroups)
    
    # Retorna puntero hacia el curos con una ID especifica
    # Si un curso con dicha ID no existe, se retona NULL
    def GetCourseById(self, id):
        if id in self.courses.keys():
            return self.courses[id]
        return None

    # Retorna numero de cursos recogidos
    def GetNumberOfCourses(self):
        return len(self.courses)
    
    # Retorna puntero hacia el aula con una ID especifica
    # Si un aula con dicha ID no existe, el método retorna NULL
    def GetRoomById(self, id):
        if id in self.rooms.keys():
            return self.rooms[id]
        return None
    
    # Retorna numero de aulas recogidos
    def GetNumberOfRooms(self):
        return len(self.rooms)
    
    # Retorna una referencia hacia la lista de clases recogidas
    def GetCourseClasses(self):
        return self.courseClasses
    
    # Retorna numero de clases recogidas
    def GetNumberOfCourseClasses(self):
        return len(self.courseClasses)
    
    # Retorna TRUE si la configuración no ha sido recogido todavia
    def isEmpty(self):
        return self.isEmpty

    # Lee los datos del profesor desde el archivo de configuración.
    # Crea un objeto de profesor y devuelve una referencia a él.
    # Devuelve None si no se puede analizar la configuración.
    def __ParseProfessor(self, file):
        newFile = file
        id = 0
        name = ''
        dictConfig  = {}
        while True:
            line = newFile.readline()
            line = line.strip()
            if line == "" or line == '#end':
                break
            key = ''
            value = ''
            p = line.find('=')
            if p != -1:
                # key
                key = line[:p].strip()
                # value
                dictConfig[key] = line[p + 1:].strip()
            
            for key in dictConfig.keys():
                if key == 'id':
                    id = dictConfig[key]
                elif key == 'name':
                    name = dictConfig[key]

        # Crea un objeto y devuelve una referencia.
        if id == 0:
            return None
        
        return Professor.Professor(id, name)

     
    # Lee los datos del profesor desde el archivo de configuración.
    # Crea un objeto de profesor.
    # Devuelve una referencia al objeto creado, o None si hay errores.
    def __ParseStudentsGroup(self, file):
        newFile = file
        id = 0
        number = 0
        name = ''
        dictConfig  = {}
        while True:
            line = newFile.readline()
            line = line.strip()
            if line == "" or line == '#end':
                break
            key = ''
            value = ''
            p = line.find('=')
            if p != -1:
                # key
                key = line[:p].strip()
                # value
                dictConfig[key] = line[p + 1:].strip()
            
            for key in dictConfig.keys():
                if key == 'id':
                    id = dictConfig[key]
                elif key == 'name':
                    name = dictConfig[key]
                elif key == 'size':
                    number = dictConfig[key]

       # Crea un objeto y lo devuelve.
        if id == 0:
            return None
        return StudentsGroup.StudentsGroup( id, name, number )

    # Lee los datos del curso desde el archivo de configuración.
    # Crea un objeto de curso.
    # Devuelve una referencia al objeto creado, o None si hay errores.
    def __ParseCourse(self, file):
        print("parse course")
        newFile = file
        id = 0
        name = ''
        dictConfig = {}
        while True:
            line = newFile.readline()
            line = line.strip()
            if line == "" or line == '#end':
                break
            key = ''
            value = ''
            p = line.find('=')
            if p != -1:
                # key
                key = line[:p].strip()
                # value
                dictConfig[key] = line[p + 1:].strip()
            
            for key in dictConfig.keys():
                if key == 'id':
                    id = dictConfig[key]
                elif key == 'name':
                    name = dictConfig[key]

        # Crea un objeto y lo devuelve.
        if id == 0:
            return None
 
        return Course.Course(id, name)

    # Lee los datos de las salas desde el archivo de configuración.
    # Crea un objeto de sala.
    # Devuelve una referencia al objeto creado, o None si hay errores.
    def __ParseRoom(self, file):
        newFile = file
        number = 0
        lab = False
        name = ''
        dictConfig = {}
        while True:
            line = newFile.readline()
            line = line.strip()
            if line == "" or line == '#end':
                break
            key = ''
            value = ''
            p = line.find('=')
            if p != -1:
                # key
                key = line[:p].strip()
                # value
                dictConfig[key] = line[p + 1:].strip()
            
            for key in dictConfig.keys():
                if key == 'name':
                    name = dictConfig[key]
                elif key == 'lab':
                    lab = dictConfig[key]
                elif key == 'size':
                    number = dictConfig[key]

        # make object and return pointer to it
        if number == 0:
            return None

        return Room.Room( name, lab, number )
    
    # Lee los datos de la clase desde el archivo de configuración.
    # Crea un objeto de clase.
    # Devuelve una referencia al objeto creado, o None si hay errores
    def __ParseCourseClass(self, file):
        newFile = file
        pid = 0
        cid = 0
        dur = 1
        lab = False
        groups = []
        dictConfig = {}
        while True:
            line = newFile.readline()
            line = line.strip()
            if line == "" or line == '#end':
                break
            key = ''
            value = ''
            p = line.find('=')
            if p != -1:
                # key
                key = line[:p].strip()
                # value
                dictConfig[key] = line[p + 1:].strip()
            
            for key in dictConfig.keys():
                if key == 'professor':
                    pid = dictConfig[key]
                elif key == 'course':
                    cid = dictConfig[key]
                elif key == 'lab':
                    lab = dictConfig[key]
                elif key == 'duration':
                    dur = dictConfig[key]
                elif key == 'group':
                    g = self.GetStudentsGroupById(dictConfig[key])
                    if g:
                        groups.append(g)

        # get professor who teaches class and course to which this class belongs
        p = self.GetProfessorById(pid)
        c = self.GetCourseById(cid)

        # does professor and class exists
        if not c or not p:
            return None
        
        # make object and return pointer to it
        return CourseClass.CourseClass( p, c, groups, lab, dur )
