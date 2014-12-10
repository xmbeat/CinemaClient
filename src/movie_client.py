import httplib
import json
from identidad import Actor, ActorReducido, InfoCompania
from identidad import InfoReparto, Pelicula, InfoGenero, PeliculaReducida
import urllib


class GenericObject(object):
    pass


def factoryGenericObject(dictionary):
    obj = GenericObject()
    obj.__dict__.update(dictionary)
    return obj


class MovieClient:

    def __init__(self):
        self.apiKey = "1f7b1044674d95c01a599c156ce2140f"
        self.host = "api.themoviedb.org"
        self.imagePath = "http://cf2.imgobject.com/t/p/w500"

    def updateActor(self, actor):
        pass
    
    def updatePelicula(self, pelicula):
        pass

    def getJSON(self, host, resource):
        conn = httplib.HTTPConnection(host, 80)
        conn.request("GET", resource)
        res = conn.getresponse()
        data = res.read()
        conn.close()
        return data

    def obtenPelicula(self, idPelicula):
        pelicula = None
        try:
            respuesta = self.getJSON(self.host, "/3/movie/" + str(idPelicula) +
                                     "?api_key=" + self.apiKey)

            mdbPelicula = json.loads(
                respuesta,
                object_hook=factoryGenericObject)
            if mdbPelicula is not None:
                pelicula = Pelicula()
                pelicula.duracion = mdbPelicula.runtime
                pelicula.fechaEstreno = mdbPelicula.release_date
                pelicula.id = mdbPelicula.id
                pelicula.titulo = mdbPelicula.title
                if mdbPelicula.poster_path is not None:
                    pelicula.urlImagen = self.imagePath + \
                        mdbPelicula.poster_path
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
            print "MovieClient::obtenPelicula::" + str(error)

        return pelicula

    def obtenRepartoPelicula(self, idPelicula):
        lista = []
        try:
            respuesta = self.getJSON(self.host, "/3/movie/" + str(idPelicula) +
                                     "/casts?api_key=" + self.apiKey)

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
            respuesta = self.getJSON(
                self.host,
                "/3/person/" +
                str(idActor) +
                "?api_key=" +
                self.apiKey)

            otroActor = json.loads(respuesta, object_hook=factoryGenericObject)
            if otroActor is not None:
                actor = Actor()
                actor.id = otroActor.id
                actor.lugar = otroActor.place_of_birth
                actor.urlActor = otroActor.homepage
                actor.nombre = otroActor.name

                if otroActor.profile_path is not None and otroActor.profile_path != "":
                    actor.urlImagen = self.imagePath + otroActor.profile_path

                actor.fechaNacimiento = otroActor.birthday
                actor.fechaMuerte = otroActor.deathday

        except Exception as error:
            print "MovieClient::obtenActor::" + str(error)

        return actor

    def buscarActor(self, nombre, page):
        results = []
        try:
            nombre = urllib.quote(nombre)
            respuesta = self.getJSON(self.host, "/3/search/person?api_key=" + self.apiKey +
                                     "&query=" + nombre + "&page=" + str(page))

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

            busqueda = json.loads(respuesta, object_hook=factoryGenericObject)
            for pelicula in busqueda.results:
                results.append(PeliculaReducida(pelicula.id, pelicula.title))
        except Exception as error:
            print "MovieClient::buscarPelicula::" + str(error)
        return results
