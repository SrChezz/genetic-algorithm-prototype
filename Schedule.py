import CourseClass
import Configuration
import copy
from random import randint
import Algorithm

# Número de horas laborales por día
DAY_HOURS = 12
# Número de días en la semana
DAYS_NUM = 5

# Cromosoma del horario
class Schedule:
        # Inicializa los cromosomas con un bloque de configuración (configuración del cromosoma)
        def _init_(self, numberOfCrossoverPoints, mutationSize, crossoverProbability, mutationProbability):
                # Número de puntos de cruce en las tablas de clases de los padres
                self.numberOfCrossoverPoints = numberOfCrossoverPoints
                # Número de clases que se mueven aleatoriamente en una sola operación de mutación
                self.mutationSize = mutationSize
                # Probabilidad de que ocurra un cruce
                self.crossoverProbability = crossoverProbability
                # Probabilidad de que ocurra una mutación
                self.mutationProbability = mutationProbability
                # Valor de aptitud (fitness) del cromosoma
                self.fitness = 0
                # Espacios de tiempo, cada entrada representa una hora en un aula
                self.slots = []
                # Indicadores de satisfacción de los requisitos de las clases
                self.criteria = []

                self.slots = DAYS_NUM * DAY_HOURS * Algorithm.instance.GetNumberOfRooms() * [None]
                self.criteria = Configuration.instance.GetNumberOfCourseClasses() * 5

        # Imita el constructor de copia en C++
        def copy(self):
                return copy.deepcopy(self)

        # Crea un nuevo cromosoma con la misma configuración pero con un código elegido al azar
        def MakeNewFromPrototype(self):
                # Número de espacios de tiempo
                size = len(self.slots)

                # Crear un nuevo cromosoma copiando la configuración del cromosoma
                newChromosome = self.copy()
                newChromosome.classes = {}
                # Ubicar las clases en posiciones aleatorias
                c = Configuration.instance.GetCourseClasses()
                for it in c:
                        # Determinar la posición aleatoria de la clase
                        nr = Configuration.instance.GetNumberOfRooms()
                        dur = c[it].GetDuration()
                        day = randint(0,32767) % DAYS_NUM
                        room = randint(0, 32767) % nr
                        time = randint(0, 32767) % ( DAY_HOURS + 1 - dur )
                        pos = day * nr * DAY_HOURS + room * DAY_HOURS + time

                        # Llenar espacios de tiempo, para cada hora de clase
                        for i in range(dur - 1, -1, -1):
                                newChromosome.slots[pos + i].push(c[it])

                        # Insertar en la tabla de clases del cromosoma
                        newChromosome.classes[pos] = c[it]

                newChromosome.CalculateFitness()

                # Retornar un puntero inteligente
                return newChromosome

        # Realiza una operación de cruce utilizando dos cromosomas y devuelve un puntero a la descendencia
        def Crossover(self, parent2):
                # Verificar la probabilidad de realizar la operación de cruce
                if randint(0, 32767) % 100 > self.crossoverProbability:
                        # Sin cruce, solo copiar el primer padre
                        return Schedule.Schedule( self, False )

                # Crear un nuevo objeto de cromosoma, copiando la configuración del cromosoma
                n = Schedule.Schedule( self, True )

                # Número de clases
                size = len(self.classes)
                cp = size * [None]

                # Determinar los puntos de cruce (aleatoriamente)
                for i in range(self.numberOfCrossoverPoints, 0, -1):
                        while 1:
                                p = randint(0, 32767) % size
                                if (not cp[p]):
                                        cp[p] = True
                                        break

                j = 0
                it1 = self.classes[j]
                it2 = parent2.classes[j]
                # Crear un nuevo código combinando los códigos de los padres
                first = randint(0, 1) == 0
                for i in range(0, size):
                        if first:
                                # Insertar la clase del primer padre en la tabla de clases del nuevo cromosoma
                                n.classes[j] = it1
                                # Copiar todos los espacios de tiempo de la clase
                                for k in range(it1.GetDuration() - 1, -1, -1):
                                        n.slots[j + k].push(it1)
                        else:
                                # Insertar la clase del segundo padre en la tabla de clases del nuevo cromosoma
                                n.classes[j] = it2
                                # Copiar todos los espacios de tiempo de la clase
                                for k in range(it2.GetDuration() - 1, -1, -1):
                                        n.slots[j + k].push(it2)

                        # Punto de cruce
                        if cp[i]:
                                # Cambiar el cromosoma fuente
                                first = not first

                        j = j + 1

                n.CalculateFitness()

                # Retornar un puntero inteligente a la descendencia
                return n

        # Realiza la operación de mutación en el cromosoma
        def Mutation(self):
                # Verificar la probabilidad de realizar la operación de mutación
                if randint(0, 32767) % 100 > self.mutationProbability:
                        return None

                # Número de clases
                numberOfClasses = len(self.classes)
                # Número de espacios de tiempo
                size = len(self.slots)

                # Mover un número seleccionado de clases a posiciones aleatorias
                for i in range(self.mutationSize, 0, -1):
                        # Seleccionar un cromosoma aleatorio para moverlo
                        mpos = randint(0, 32767) % numberOfClasses
                        pos1 = j = mpos

                        cc1 = self.classes[pos1]

                        # Determinar aleatoriamente la posición de la clase
                        nr = Schedule.instance.GetNumberOfRooms()
                        dur = cc1.GetDuration()
                        day = randint(0, 32767) % DAYS_NUM
                        room = randint(0, 32767) % nr
                        time = randint(0, 32767) % ( DAY_HOURS + 1 - dur )
                        pos2 = day * nr * DAY_HOURS + room * DAY_HOURS + time

                        # Mover todos los espacios de tiempo
                        for j in range(dur - 1, -1, -1):
                                # Eliminar la hora de clase del espacio de tiempo actual
                                c1 = self.slots[pos1 + i]
                                for k in range(0, len(self.slots)):
                                        if c1[k] == cc1:
                                                del c1[k]
                                                break

                                # Mover la hora de clase al nuevo espacio de tiempo
                                self.slots[pos2 + i].push(cc1)

                        # Cambiar la entrada de la tabla de clases para apuntar al nuevo espacio de tiempo
                        self.classes[ cc1 ] = pos2

                self.CalculateFitness()

        # Calcula el valor de aptitud (fitness) del cromosoma
        def CalculateFitness(self):
                # Puntuación del cromosoma
                score = 0
                numberOfRooms = Configuration.instance.GetNumberOfRooms()
                daySize = DAY_HOURS * numberOfRooms

                ci = 0
		
                # Verificar criterios y calcular puntuaciones para cada clase en el horario
                for i in range(0, len(self.classes)):
                        # Coordenadas del espacio de tiempo
                        p = i
                        day = p / daySize
                        time = p % daySize
                        room = time / DAY_HOURS
                        time = time % DAY_HOURS

                        dur = classes[i].GetDuration()

                        # Verificar superposición de clases en una misma sala
                        ro = False
                        for j in range(dur - 1, -1, -1):
                                if self.slots[p + j].size() > 1:
                                        ro = True
                                        break

                        # Si no hay superposición en la sala
                        if not ro:
                                score = score + 1

                        self.criteria[ci + 0 ] = not ro
                        
                        cc = classes[i]
                        r = Configuration.instance.GetRoomById( room )
                        # ¿La sala actual tiene suficientes asientos?
                        self.criteria[ci + 1 ] = r.GetNumberOfSeats() >= cc.GetNumberOfSeats()
                        if self.criteria[ ci + 1 ]:
                                score = score + 1

                        # ¿La sala actual tiene computadoras si se requieren?
                        self.criteria[ ci + 2 ] = (not cc.IsLabRequired()) or (cc.IsLabRequired() and r.IsLab())
                        if self.criteria[ ci + 2 ]:
                                score = score + 1

                        po = False
                        go = False
                        # Verificar superposición de clases para profesores y grupos de estudiantes
                        t = day * daySize + time
                        breakPoint = False
                        for k in range(numberOfRooms, 0, -1):
                                if breakPoint == True: break
                                # Por cada hora de clase
                                for l in range(dur - 1, -1, -1):
                                        if breakPoint == True: break
                                        # Verificar superposición con otras clases al mismo tiempo
                                        cl = self.slots[ t + k ]
                                        for it in range(0, len(cl)):
                                                if cc != cl[it]:
                                                        # ¿Superposición del profesor?
                                                        if not po and cc.ProfessorOverlaps(cl[it]):
                                                                po = True
                                                        # ¿Superposición del grupo?
                                                        if not go and cc.GroupsOverlap(cl[it]):
                                                                go = True
                                                        # 
                                                        if po and go:
                                                                breakPoint = True
                                                                
                                t = t + DAY_HOURS
                        # Si no hay superposición del profesor
                        if not po:
                                score = score + 1
                        self.criteria[ ci + 3 ] = not po

                        # Si no hay superposición del grupo
                        if not go:
                                score = score + 1
                        self.criteria[ ci + 4 ] = not go

                        ci += 5

                # Calcular valor fitnes en base al puntaje
                self.fitness = score / ( Configuration.instance.GetNumberOfCourseClasses() * DAYS_NUM )