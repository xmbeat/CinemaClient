import httplib
import json
from actor import ActorReducido, Actor, PeliculaReducida, Pelicula, InfoCompania, InfoGenero, InfoReparto
import urllib

class Busqueda(object):
    def __init__(self):
        self.page = 0
        self.results = []
        self.total_pages = 0
        self.total_results = 0

class GenericObject(object):
    pass

def factoryGenericObject(dictionary):
    obj = GenericObject()
    obj.__dict__.update(dictionary)
    return obj
    
def factoryBusqueda(dictionary):
    busqueda = Busqueda()
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

class MDBPelicula(object):
    pass

def factoryMDBPelicula(dictionary):
    pelicula = MDBPelicula()
    pelicula.__dict__.update(dictionary)
    return pelicula

        
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
        return data
    
    def obtenPelicula(self, idPelicula):
        pelicula = None
        try:
            respuesta = self.getJSON(self.host, "/3/movie/" + str(idPelicula) + "?api_key=" + self.apiKey)
            #mdbPelicula = json.loads(respuesta, object_hook=factoryMDBPelicula)
            mdbPelicula = json.loads(respuesta, object_hook=factoryGenericObject)
            if not mdbPelicula is None:
                pelicula = Pelicula()
                pelicula.duracion = mdbPelicula.runtime
                pelicula.fechaEstreno = mdbPelicula.release_date
                pelicula.id = mdbPelicula.id
                pelicula.titulo = mdbPelicula.title
                if not mdbPelicula.poster_path is None:
                    pelicula.urlImagen = self.imagePath + mdbPelicula.poster_path
                pelicula.urlPelicula = mdbPelicula.homepage
                if len(mdbPelicula.production_companies) > 0:
                    for compania in mdbPelicula.production_companies:
                        infoCompania = InfoCompania()
                        infoCompania.id = compania.id
                        infoCompania.nombre = compania.name
                        pelicula.companias.append(infoCompania)
                        
                if len(mdbPelicula.genres) > 0:
                    for genero in mdbPelicula.genres:
                        infoGenero = InfoGenero()
                        infoGenero.id = genero.id
                        infoGenero.nombre = genero.name
                        pelicula.generos.append(infoGenero)
                
                pelicula.reparto = self.obtenRepartoPelicula(idPelicula)
                         
        except Exception as error:
            print "MovieClient::buscarPelicula::" + str(error)
        
        return pelicula
    
    def obtenRepartoPelicula(self, idPelicula):
        lista = []
        try:
            respuesta = self.getJSON(self.host, "/3/movie/" + str(idPelicula) + 
                                     "/casts?api_key=" + self.apiKey)
            #busqueda = json.loads(respuesta, object_hook=factoryBusqueda)
            busqueda = json.loads(respuesta, object_hook=factoryGenericObject)
            
            for reparto in busqueda.cast:
                infoReparto = InfoReparto()
                infoReparto.idActor = reparto.id
                infoReparto.papel = reparto.character 
                lista.append(infoReparto)
                
        except Exception as error:
            print "MovieClient::obtenRepartoPelicula::" + str(error)
            
        return lista             
                
    def obtenActor(self, idActor):
        actor = None
        try:
            respuesta = self.getJSON(self.host, "/3/person/" + str(idActor) + "?api_key=" + self.apiKey)
            #otroActor = json.loads(respuesta, object_hook=factoryMDBActor)
            otroActor = json.loads(respuesta, object_hook=factoryGenericObject)
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
            nombre = urllib.quote(nombre)
            respuesta = self.getJSON(self.host, "/3/search/person?api_key=" + self.apiKey + 
                                 "&query=" + nombre + "&page=" + str(page))
            #busqueda = json.loads(respuesta, object_hook=factoryBusqueda)
            busqueda = json.loads(respuesta, object_hook=factoryGenericObject)
            for actor in busqueda.results:
                results.append(ActorReducido(actor.id, actor.name))
                
        except Exception as error:
            print "MovieClient::buscarActor::" + str(error)
        return results
        
    def buscarPelicula(self, titulo, page):
        results = []
        try:
            titulo = urllib.quote(titulo)
            respuesta = self.getJSON(self.host, "/3/search/movie?api_key=" + self.apiKey + 
                                     "&query=" + titulo + "&page=" + str(page))
            #busqueda = json.loads(respuesta, object_hook=factoryBusqueda)
            busqueda = json.loads(respuesta, object_hook=factoryGenericObject)
            for pelicula in busqueda.results:
                results.append(PeliculaReducida(pelicula.id, pelicula.title))
        except Exception as error:
            print "MovieClient::buscarPelicula::" + str(error)
        return results
    
if __name__ == "__main__":
    cliente = MovieClient()
    cliente.buscarActor("Eminem", 1)
