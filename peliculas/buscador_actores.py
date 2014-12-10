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
        #Thread.run(self)
        try:
            gtk.threads_enter()
            idMessage = self.gui.pushMessage("Buscando coincidiencias...")
            gtk.threads_leave()
            client = MovieClient()
            
            self.gui.actoresReducidos = client.buscarActor(self.who, 1)
            gtk.threads_enter()
            for actor in self.gui.actoresReducidos:
                self.gui.cmbResultadosActor.append_text(actor.nombre)
                
            self.gui.popMessage(idMessage)
            self.gui.btnBuscarActor.set_sensitive(True)
            gtk.threads_leave()
        except Exception as error:
            
            print "BuscadorActores::" + str(error)
            
        
class CargadorActor(Thread):
    def __init__(self, actorReducido, gui):
        Thread.__init__(self)
        self.actor = actorReducido
        self.gui = gui
        
    def run(self):
        Thread.run(self)
        try:
            client = MovieClient()
            gtk.threads_enter()
            idMessage = self.gui.pushMessage("Obteniendo informacion del actor")
            gtk.threads_leave()
            self.gui.currentActor = client.obtenActor(self.actor.id)
            self.gui.popMessage(idMessage)
            gtk.threads_enter()
            self.gui.loadCurrentActor()
            gtk.threads_leave()
            self.gui.loadUrlImage(self.gui.imgActor, self.gui.currentActor.urlImagen, 300)
        except Exception as error:
            print "Error::CargadorActor::" + str(error)
        finally:
            gtk.threads_enter()
            self.gui.frmDetallesActor.set_sensitive(True)
            self.gui.btnSeleccionarActor.set_sensitive(True) 
            self.gui.btnBuscarActor.set_sensitive(True)
            gtk.threads_leave()
    