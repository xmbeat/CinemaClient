#!/usr/bin/env python

import urllib2
import pygtk
pygtk.require('2.0')
import gtk
from gobject.constants import TYPE_STRING
from buscador_actores import BuscadorActores, CargadorActor

class GUICinema:
    def __init__(self, gladeFile):
        gtk.gdk.threads_init()
        builder = gtk.Builder()
        builder.add_from_file(gladeFile)     
        self.window = builder.get_object("winMain")
        #Enlazando los eventos
        self.btnBuscarActor = builder.get_object("btnBuscarActor")
        self.btnBuscarActor.connect("clicked", self.onPressedBuscarActor)
        self.btnSeleccionarActor = builder.get_object("btnSeleccionarActor")
        self.btnSeleccionarActor.connect("clicked", self.onPressedSeleccionarActor)
        self.btnNacimientoActor = builder.get_object("btnNacimientoActor")
        self.btnNacimientoActor.connect("clicked", self.onPressedNacimientoActor)
        self.btnMuerteActor = builder.get_object("btnMuerteActor")
        self.btnMuerteActor.connect("clicked", self.onPressedMuerteActor)
        self.btnActualizarActor = builder.get_object("btnActualizarActor")
        self.btnActualizarActor.connect("clicked", self.onPressedActualizarActor)
        self.cmbResultadosActor = builder.get_object("cmbResultadosActor")
        
        self.btnBuscarPelicula = builder.get_object("btnBuscarPelicula")
        self.btnBuscarPelicula.connect("clicked", self.onPressedBuscarPelicula)
        self.btnSeleccionarPelicula = builder.get_object("btnSeleccionarPelicula")
        self.btnSeleccionarPelicula.connect("clicked", self.onPressedSeleccionarPelicula)
        self.btnFechaEstreno = builder.get_object("btnFechaEstreno")
        self.btnFechaEstreno.connect("clicked", self.onPressedFechaEstreno)
        self.btnActualizarPelicula = builder.get_object("btnActualizarPelicula")
        self.btnActualizarPelicula.connect("clicked", self.onPressedActualizarPelicula)
        self.cmbResultadosPelicula = builder.get_object("cmbResultadosPelicula")
    
        self.txtTitulo = builder.get_object("txtTitulo")
        self.txtDuracion = builder.get_object("txtDuracion")
        self.txtUrlPelicula = builder.get_object("txtUrlPelicula")
        self.txtImagenPelicula = builder.get_object("txtImagenPelicula")
        
        store = gtk.ListStore(TYPE_STRING)
        self.cmbResultadosActor.set_model(store)
        cell = gtk.CellRendererText()
        self.cmbResultadosActor.pack_start(cell)
        self.cmbResultadosActor.add_attribute(cell, "text", 0)
        
        
        store = gtk.ListStore(TYPE_STRING)
        self.cmbResultadosPelicula.set_model(store)    
        cell = gtk.CellRendererText()
        self.cmbResultadosPelicula.pack_start(cell)
        self.cmbResultadosPelicula.add_attribute(cell, "text", 0)
        #self.cmbResultadosActor.set_active(0)
        
        self.txtBusquedaActor = builder.get_object("txtBusquedaActor")
        self.txtNombreActor = builder.get_object("txtNombreActor")
        self.txtLugarActor = builder.get_object("txtLugarActor")
        self.chkMuerteActor = builder.get_object("chkMuerteActor")
        self.txtUrlActor = builder.get_object("txtUrlActor")
        self.txtImagenActor = builder.get_object("txtImagenActor")
        self.frmDetallesActor = builder.get_object("frmDetallesActor")
        self.imgActor = gtk.Image()
        self.scrolledActor = builder.get_object("scrolledActor")
        self.scrolledActor.add_with_viewport(self.imgActor)
        self.imgPelicula = gtk.Image()
        self.scrolledPelicula = builder.get_object("scrolledPelicula")
        self.scrolledPelicula.add_with_viewport(self.imgPelicula)
        
        self.statusbar = builder.get_object("statusbar")
        self.window.show_all()
        
        self.currentActor = None
        self.actoresReducidos = None
        self.listaActores = None
        
        self.window.connect("destroy", gtk.mainquit)
        gtk.main()
    
    def onPressedActualizarPelicula(self, button):
        pass
    
    def onPressedSeleccionarActor(self, button):
        if not self.actoresReducidos is None:
            if len(self.actoresReducidos) > 0:
                if self.cmbResultadosActor.get_active() == -1:
                    print "Seleccione uno"
                self.btnActualizarActor.set_label("Actualizar")
                self.btnSeleccionarActor.set_sensitive(False)
                self.btnBuscarActor.set_sensitive(False)
                self.frmDetallesActor.set_sensitive(False)
                self.listaActores = None
                
                indice = self.cmbResultadosActor.get_active()
                cargador = CargadorActor(self.actoresReducidos[indice], self)
                cargador.start()
    
    def onPressedSeleccionarPelicula(self, button):
        pass    
        
    def onPressedBuscarActor(self, button):
        button.set_sensitive(False)
        self.removeAllItems(self.cmbResultadosActor)
        self.frmDetallesActor.set_sensitive(False)
        self.imgActor.clear()
        nombre = self.txtBusquedaActor.get_text()
        self.currentActor = None
        self.actoresReducidos = None
        buscador = BuscadorActores(nombre, self)
        buscador.start()
        
    def onPressedBuscarPelicula(self, button):
        pass
    
    def onPressedFechaEstreno(self, button):
        pass
    
    def onPressedNacimientoActor(self, button):
        pass
    
    def onPressedMuerteActor(self, button):
        pass
    
    def onPressedActualizarActor(self, button):
        pass
    
    def removeAllItems(self, cmb):
        model = cmb.get_model()
        model.clear()
    
    def loadCurrentActor(self):
        if self.currentActor is None:
            return
        
        self.txtNombreActor.set_text(self.currentActor.nombre)
        self.txtLugarActor.set_text(self.currentActor.lugar)
        self.btnNacimientoActor.set_label(self.currentActor.fechaNacimiento)
        self.btnMuerteActor.set_label(self.currentActor.fechaMuerte)
        
        if self.currentActor.fechaMuerte == "":
            self.chkMuerteActor.set_active(False)
        else:
            self.chkMuerteActor.set_active(True)
        
        self.txtUrlActor.set_text(self.currentActor.urlActor)    
        self.txtImagenActor.set_text(self.currentActor.urlImagen)   
    
    def loadUrlImage(self, component, url, maxWidth):
        try:
            gtk.gdk.threads_enter()
            self.imgActor.set_from_pixbuf(None)
            gtk.gdk.threads_leave()
            response = urllib2.urlopen(url)
            loader = gtk.gdk.PixbufLoader()
            loader.write(response.read())
            loader.close()
            gtk.gdk.threads_enter()
            self.imgActor.set_from_pixbuf(loader.get_pixbuf())
            gtk.gdk.threads_leave()
        except Exception as error:
            print "guicinema::loadUrlImage::" + str(error)
    
    def pushMessage(self, message):
        context = self.statusbar.get_context_id("statusbar")
        return self.statusbar.push(context, message)
    
    def popMessage(self, idMessage):
        context = self.statusbar.get_context_id("statusbar")
        self.statusbar.remove(context, idMessage)
    
# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    gui = GUICinema("interface.glade")
    