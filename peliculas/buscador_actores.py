from threading import  Thread
from movie_client import MovieClient
import gtk

class BuscadorActores(Thread):
    
    def __init__(self, who, gui):
        Thread.__init__(self)
        if who is None:
            who = ""
        self.who = who
        self.gui = gui
        
    def run(self):
        try:
            gtk.gdk.threads_enter()
            idMessage = self.gui.pushMessage("Buscando coincidiencias...")
            gtk.gdk.threads_leave()
            client = MovieClient()
            
            self.gui.actoresReducidos = client.buscarActor(self.who, 1)
            gtk.gdk.threads_enter()
            for actor in self.gui.actoresReducidos:
                self.gui.cmbResultadosActor.append_text(actor.nombre)
                
            self.gui.popMessage(idMessage)
            self.gui.btnBuscarActor.set_sensitive(True)
            gtk.gdk.threads_leave()
        except Exception as error:
            
            print "BuscadorActores::" + str(error)
            
class BuscadorPeliculas(Thread):
    def __init__(self, title, gui):
        Thread.__init__(self)
        if title is None:
            title = ""
        self.title = title
        self.gui  = gui
     
    def run(self):
        try:
            gtk.gdk.threads_enter()
            idMessage = self.gui.pushMessage("Buscando coincidiencias...")
            gtk.gdk.threads_leave()
            client = MovieClient() 
            self.gui.peliculasReducidas = client.buscarPelicula(self.title, 1)
            
            gtk.gdk.threads_enter()
            for pelicula in self.gui.peliculasReducidas:
                self.gui.cmbResultadosPelicula.append_text(pelicula.titulo)
                
            self.gui.popMessage(idMessage)
            self.gui.btnBuscarPelicula.set_sensitive(True)
            gtk.gdk.threads_leave()
        except Exception as error:
            print "BuscadorPelicula::run::" + str(error)
        

class CargadorPelicula(Thread):
    def __init__(self, peliculaReducida, gui):
        Thread.__init__(self)
        self.pelicula = peliculaReducida
        self.gui = gui
    
    def run(self):
        try:
            client = MovieClient()
            gtk.gdk.threads_enter()
            idMessage = self.gui.pushMessage("Obteniendo informacion de la pelicula")
            gtk.gdk.threads_leave()
            self.gui.currentPelicula = client.obtenPelicula(self.pelicula.id)
            gtk.gdk.threads_enter()
            self.gui.popMessage(idMessage)
            self.gui.loadCurrentPelicula()
            gtk.gdk.threads_leave()
            self.gui.loadUrlImage(self.gui.imgPelicula, self.gui.currentPelicula.urlImagen, 300)
            gtk.gdk.threads_enter()
            self.gui.frmDetallesPelicula.set_sensitive(True)
            self.gui.btnSeleccionarPelicula.set_sensitive(True) 
            self.gui.btnBuscarPelicula.set_sensitive(True)
            gtk.gdk.threads_leave()
        except Exception as error:
            print "CargadorPelicula::run::" + str(error)
 
class CargadorActor(Thread):
    def __init__(self, actorReducido, gui):
        Thread.__init__(self)
        self.actor = actorReducido
        self.gui = gui
        
    def run(self):
        try:
            client = MovieClient()
            gtk.gdk.threads_enter()
            idMessage = self.gui.pushMessage("Obteniendo informacion del actor")
            gtk.gdk.threads_leave()
            self.gui.currentActor = client.obtenActor(self.actor.id)
            gtk.gdk.threads_enter()
            self.gui.popMessage(idMessage)
            self.gui.loadCurrentActor()
            gtk.gdk.threads_leave()
            self.gui.loadUrlImage(self.gui.imgActor, self.gui.currentActor.urlImagen, 300)
            gtk.gdk.threads_enter()
            self.gui.frmDetallesActor.set_sensitive(True)
            self.gui.btnSeleccionarActor.set_sensitive(True) 
            self.gui.btnBuscarActor.set_sensitive(True)
            gtk.gdk.threads_leave()
        except Exception as error:
            print "CargadorActor::run" + str(error)
    
