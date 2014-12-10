class ActorReducido:
    def __init__(self, idActor = 0, nombreActor = ""):
        self.id = idActor
        self.nombre = nombreActor

class Actor:
    def __init__(self):
        self.id = 0;
        self.nombre = ""
        self.urlActor = ""
        self.urlImagen = ""
        self.lugar = ""
        self.fechaNacimiento = None
        self.fechaMuerte = None