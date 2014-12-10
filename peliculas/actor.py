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
        
class PeliculaReducida:
    def __init__(self, idPelicula = 0, tituloPelicula = ""):
        self.id = idPelicula
        self.titulo = tituloPelicula

class Pelicula:
    def __init__(self):
        self.id = 0
        self.titulo = ""
        self.duracion = 0
        self.fechaEstreno = ""
        self.urlImagen = ""
        self.urlPelicula = ""
        self.companias = []
        self.generos = []
        self.reparto = []

class InfoCompania:
    def __init__(self):
        self.id = 0
        self.nombre = ""

class InfoGenero:
    def __init__(self):
        self.id = 0
        self.nombre = ""

class InfoReparto:
    def __init__(self):
        self.idActor = 0
        self.papel = ""