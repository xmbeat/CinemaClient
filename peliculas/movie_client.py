import httplib
import json
from actor import ActorReducido, Actor

class BusquedaActor(object):
    def __init__(self):
        self.page = 0
        self.results = []
        self.total_pages = 0
        self.total_results = 0
        
def factoryBusquedaActor(dictionary):
    busqueda = BusquedaActor()
    busqueda.__dict__.update(dictionary)
    return busqueda

class MDBActor(object):
    def __init__(self):
        self.adult = False
        self.also_known_as = []
        self.biography = ""
        self.birthday = ""
        self.deathday = ""
        self.homepage = ""
        self.id = 0
        self.name = ""
        self.place_of_birth = ""
        self.profile_path = ""
    pass

def factoryMDBActor(dictionary):
    actor = MDBActor()
    actor.__dict__.update(dictionary)
    return actor
        
class MovieClient:
    def __init__(self):
        self.apiKey = "1f7b1044674d95c01a599c156ce2140f"
        self.host = "api.themoviedb.org"
        self.imagePath = "http://cf2.imgobject.com/t/p/w500"
        
    def getJSON(self, host, resource):
        conn = httplib.HTTPConnection(host, 80)
        conn.request("GET", resource)       
        #conn.putheader("Accept:", "application/json")
        res = conn.getresponse()
        data = res.read()
        conn.close()
        print data
        return data
    
    def obtenActor(self, idActor):
        actor = None
        try:
            respuesta = self.getJSON(self.host, "/3/person/" + str(idActor) + "?api_key=" + self.apiKey)
            otroActor = json.loads(respuesta, object_hook=factoryMDBActor)
            if not otroActor is None:
                actor = Actor()
                actor.id = otroActor.id
                actor.lugar = otroActor.place_of_birth
                actor.urlActor = otroActor.homepage
                actor.nombre = otroActor.name
                if otroActor.profile_path != "":
                    actor.urlImagen = self.imagePath + otroActor.profile_path
                actor.fechaNacimiento = otroActor.birthday
                actor.fechaMuerte = otroActor.deathday
                
        except Exception as error:
            print error
            
        return actor
        
    
    def buscarActor(self, nombre, page):
        results = []
        try:
            respuesta = self.getJSON(self.host, "/3/search/person?api_key=" + self.apiKey + 
                                 "&query=" + nombre + "&page=" + str(page))
            busqueda = json.loads(respuesta, object_hook=factoryBusquedaActor)
            
            for actor in busqueda.results:
                results.append(ActorReducido(actor.id, actor.name))
                
        except Exception as error:
            print error
        return results
        
        
if __name__ == "__main__":
    cliente = MovieClient()
    cliente.buscarActor("Eminem", 1)
