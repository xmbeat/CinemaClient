#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("src")
from lettuce import step, world
from movie_client import MovieClient

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

@step(u'Given: Se tiene el id "([^"]*)" del actor')
def given_los_numeros(step, Id):
    world.Id = Id
    
@step(u'When: se selecciona el actor')
def when_se_obtiene_actor(step):
    client = MovieClient()
    world.resultado = client.obtenActor(world.Id)

@step(u'then: se obtiene sus datos detallados como "([^"]*)"')
def then_obtengo(step,comparacion):       
	assert world.resultado.nombre == comparacion,'Esperado: {0}, Obtenido: {1}'.format(world.resultado.nombre,comparacion)


@step(u'Given: Se tiene el id "([^"]*)" de la pelicula')
def given_los_numeros(step, Id):
    world.Id = Id
    
@step(u'When: Se selecciona la pelicula')
def when_se_obtiene_actor(step):
    client = MovieClient()
    world.resultado = client.obtenPelicula(world.Id)

@step(u'then: se obtiene sus datos detallados tal como "([^"]*)"')
def then_obtengo(step,comparacion):       
	assert world.resultado.titulo == comparacion,'Esperado: {0}, Obtenido: {1}'.format(world.resultado.titulo,comparacion)


