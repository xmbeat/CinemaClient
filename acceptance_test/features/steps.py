#!/usr/bin/python
# -*- coding: utf-8 -*-

from lettuce import step, world
from src.movie_client import MovieClient

@step(u'Given: que se tiene "([^"]*)"')
def given_los_numeros(step, patron):
    world.patron = patron
    
@step(u'When: se realiza la busqueda de ([^"]*)')
def when_se_realiza_la_busqueda(step, method):
    client = MovieClient()
    if method == "actor":
        world.resultado = client.buscarActor(world.patron, 1)
    else:
        world.resultado = client.buscarPelicula(world.patron, 1)

@step(u'then: obtengo una lista ([^"]*) a "([^"]*)" elementos')
def then_obtengo(step, comparacion, cantidad):
    cantidad = int(cantidad)
    if comparacion == "mayor":
        assert len(world.resultado) > cantidad
    elif comparacion == "menor":
        assert len(world.resultado) < cantidad
    else:
        assert  len(world.resultado) == cantidad

