#!/usr/bin/env python

import urllib2
import pygtk
from movie_client import MovieClient
pygtk.require('2.0')
import gtk
from gobject.constants import TYPE_STRING
from buscadores import BuscadorPeliculas, BuscadorActores
from buscadores import CargadorActor, CargadorPelicula


class GUICinema:

    def __init__(self, gladeFile):
        gtk.gdk.threads_init()
        builder = gtk.Builder()
        builder.add_from_file(gladeFile)
        self.window = builder.get_object("winMain")
        # Enlazando los eventos
        self.btnBuscarActor = builder.get_object("btnBuscarActor")
        self.btnBuscarActor.connect("clicked", self.onPressedBuscarActor)
        self.btnSeleccionarActor = builder.get_object("btnSeleccionarActor")
        self.btnSeleccionarActor.connect(
            "clicked",
            self.onPressedSeleccionarActor)
        self.btnNacimientoActor = builder.get_object("btnNacimientoActor")
        self.btnNacimientoActor.connect(
            "clicked",
            self.onPressedNacimientoActor)
        self.btnMuerteActor = builder.get_object("btnMuerteActor")
        self.btnMuerteActor.connect("clicked", self.onPressedMuerteActor)
        self.btnActualizarActor = builder.get_object("btnActualizarActor")
        self.btnActualizarActor.connect(
            "clicked",
            self.onPressedActualizarActor)
        self.cmbResultadosActor = builder.get_object("cmbResultadosActor")

        self.btnBuscarPelicula = builder.get_object("btnBuscarPelicula")
        self.btnBuscarPelicula.connect("clicked", self.onPressedBuscarPelicula)
        self.btnSeleccionarPelicula = builder.get_object(
            "btnSeleccionarPelicula")
        self.btnSeleccionarPelicula.connect(
            "clicked",
            self.onPressedSeleccionarPelicula)
        self.btnFechaEstreno = builder.get_object("btnFechaEstreno")
        self.btnFechaEstreno.connect("clicked", self.onPressedFechaEstreno)
        self.btnActualizarPelicula = builder.get_object(
            "btnActualizarPelicula")
        self.btnActualizarPelicula.connect(
            "clicked",
            self.onPressedActualizarPelicula)
        self.cmbResultadosPelicula = builder.get_object(
            "cmbResultadosPelicula")

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
        # self.cmbResultadosActor.set_active(0)

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

        self.txtBusquedaPelicula = builder.get_object("txtBusquedaPelicula")
        self.txtTitulo = builder.get_object("txtTitulo")
        self.spbDuracion = builder.get_object("spbDuracion")
        self.txtUrlPelicula = builder.get_object("txtUrlPelicula")
        self.txtImagenPelicula = builder.get_object("txtImagenPelicula")
        self.frmDetallesPelicula = builder.get_object("frmDetallesPelicula")
        self.imgPelicula = gtk.Image()
        self.scrolledPelicula = builder.get_object("scrolledPelicula")
        self.scrolledPelicula.add_with_viewport(self.imgPelicula)

        self.scrolledCompanias = builder.get_object("scrolledCompanias")
        self.lstCompanias = gtk.TreeView()
        store = gtk.ListStore(str)
        self.lstCompanias.set_model(store)
        cell = gtk.CellRendererText()
        col = gtk.TreeViewColumn("Companias", cell, text=0)
        self.lstCompanias.append_column(col)
        self.scrolledCompanias.add_with_viewport(self.lstCompanias)

        self.scrolledGeneros = builder.get_object("scrolledGeneros")
        self.lstGeneros = gtk.TreeView()
        store = gtk.ListStore(str)
        self.lstGeneros.set_model(store)
        cell = gtk.CellRendererText()
        col = gtk.TreeViewColumn("Generos", cell, text=0)
        self.lstGeneros.append_column(col)
        self.scrolledGeneros.add_with_viewport(self.lstGeneros)

        self.scrolledReparto = builder.get_object("scrolledReparto")
        self.lstReparto = gtk.TreeView()
        store = gtk.ListStore(str, str)
        self.lstReparto.set_model(store)
        cell = gtk.CellRendererText()
        col = gtk.TreeViewColumn("Papel", cell, text=0)
        self.lstReparto.append_column(col)
        cell = gtk.CellRendererText()
        col = gtk.TreeViewColumn("Actor", cell, text=1)
        self.lstReparto.append_column(col)
        self.scrolledReparto.add_with_viewport(self.lstReparto)

        self.statusbar = builder.get_object("statusbar")
        self.window.show_all()

        self.currentActor = None
        self.actoresReducidos = None
        self.listaActores = None

        self.window.connect("destroy", gtk.main_quit)
        gtk.main()

    def onPressedActualizarPelicula(self, button):
        pass

    def onPressedSeleccionarActor(self, button):
        if self.actoresReducidos is not None:
            if len(self.actoresReducidos) > 0:
                if self.cmbResultadosActor.get_active() == -1:
                    print "Seleccione uno"
                    return
                self.btnSeleccionarActor.set_sensitive(False)
                self.btnBuscarActor.set_sensitive(False)
                self.frmDetallesActor.set_sensitive(False)
                self.listaActores = None

                indice = self.cmbResultadosActor.get_active()
                cargador = CargadorActor(self.actoresReducidos[indice], self)
                cargador.start()

    def onPressedSeleccionarPelicula(self, button):
        if self.peliculasReducidas is not None:
            if len(self.peliculasReducidas) > 0:
                self.btnSeleccionarPelicula.set_sensitive(False)
                self.btnBuscarPelicula.set_sensitive(False)
                self.frmDetallesPelicula.set_sensitive(False)
                self.listaPeliculas = None

                indice = self.cmbResultadosPelicula.get_active()
                cargador = CargadorPelicula(
                    self.peliculasReducidas[indice],
                    self)
                cargador.start()

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
        button.set_sensitive(False)
        self.removeAllItems(self.cmbResultadosPelicula)
        self.frmDetallesPelicula.set_sensitive(False)
        self.imgPelicula.clear()
        nombre = self.txtBusquedaPelicula.get_text()
        self.currentPelicula = None
        self.peliculasReducidas = None
        buscador = BuscadorPeliculas(nombre, self)
        buscador.start()

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

    def loadCurrentPelicula(self):
        if self.currentPelicula is None:
            return
        locked = False
        try:
            gtk.gdk.threads_enter()
            locked = True
            self.txtTitulo.set_text(self.currentPelicula.titulo)
            self.spbDuracion.set_value(int(self.currentPelicula.duracion))
            self.btnFechaEstreno.set_label(self.currentPelicula.fechaEstreno)
            self.txtUrlPelicula.set_text(self.currentPelicula.urlPelicula)
            self.txtImagenPelicula.set_text(self.currentPelicula.urlImagen)

            self.lstCompanias.get_model().clear()
            for compania in self.currentPelicula.companias:
                self.lstCompanias.get_model().append([compania.nombre])

            self.lstGeneros.get_model().clear()
            for genero in self.currentPelicula.generos:
                self.lstGeneros.get_model().append([genero.nombre])

            self.lstReparto.get_model().clear()
            gtk.gdk.threads_leave()
            locked = False
            client = MovieClient()
            for reparto in self.currentPelicula.reparto:
                try:
                    actor = client.obtenActor(reparto.idActor)
                    gtk.gdk.threads_enter()
                    locked = True
                    self.lstReparto.get_model().append(
                        [reparto.papel, actor.nombre])
                except:
                    pass
                finally:
                    if locked:
                        gtk.gdk.threads_leave()
                        locked = False
        finally:
            if locked:
                gtk.gdk.threads_leave()

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
        locked = False
        try:
            gtk.gdk.threads_enter()
            locked = True
            component.set_from_pixbuf(None)
            idMessage = self.pushMessage("Cargando Imagen...")
            gtk.gdk.threads_leave()
            locked = False
            response = urllib2.urlopen(url)
            loader = gtk.gdk.PixbufLoader()
            loader.write(response.read())
            loader.close()
            gtk.gdk.threads_enter()
            locked = True
            self.popMessage(idMessage)
            component.set_from_pixbuf(loader.get_pixbuf())
            gtk.gdk.threads_leave()
            locked = False
        except Exception as error:
            print "guicinema::loadUrlImage::" + str(error)
        finally:
            if locked:
                gtk.gdk.threads_leave()

    def pushMessage(self, message):
        context = self.statusbar.get_context_id("statusbar")
        return self.statusbar.push(context, message)

    def popMessage(self, idMessage):
        context = self.statusbar.get_context_id("statusbar")
        self.statusbar.remove_message(context, idMessage)


if __name__ == "__main__":
    gui = GUICinema("interface.glade")
