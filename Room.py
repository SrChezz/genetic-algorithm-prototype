class Room:
    # Contador de ID utilizado para asignar ID automáticamente
    nextRoomId = 0

    # Inicializa los datos de la sala y asigna un ID a la sala
    def __init__(self, name, lab, numberOfSeats):
        global nextRoomId
        self.id = nextRoomId
        self.name = name
        if lab == 'true':
            self.lab = True
        else:
            self.lab = False
        print("laaab: ", name, lab, self.lab, self.id)
        self.numberOfSeats = numberOfSeats
        nextRoomId = nextRoomId + 1

    # Devuelve el ID de la sala
    def GetId(self):
        return self.id

    # Devuelve el nombre de la sala
    def GetName(self):
        return self.name

    # Devuelve TRUE si la sala tiene computadoras, de lo contrario devuelve FALSE
    def IsLab(self):
        return self.lab

    # Devuelve el número de asientos en la sala
    def GetNumberOfSeats(self):
        return int(self.numberOfSeats)

    # Reinicia las asignaciones de ID
    @staticmethod
    def RestartIDs():
        global nextRoomId
        nextRoomId = 0