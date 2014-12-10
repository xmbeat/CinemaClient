#!/usr/bin/python
# -*- coding: utf-8 -*-

from lettuce import step, world
from src.movie_client import MovieClient

@step(u'Given: que se tiene "([^"]*)"')
def given_los_numeros(step, patron):
    world.patron = patron
    
@step(u'When: se realiza la busqueda')
def when_se_realiza_la_busqueda(step):
    client = MovieClient()
    world.resultado = client.buscarActor(world.patron, 1)
    
@step(u'then: obtengo una lista de cuando menos "([^"]*)" elementos')
def then_obtengo(step, cantidad):
    assert len(world.resultado) >= cantidad
