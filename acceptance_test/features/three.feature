
Feature: Obtener datos detallados de una pelicula
	Como usuario
	quiero obtener los detalles de alguna pelicula,
	para tener mas informacion acerca de ella
	
	
	Scenario: El id "105" de la pelicula 
		Given: Se tiene el id "105" de la pelicula
		When: Se selecciona la pelicula
		then: se obtiene sus datos detallados tal como "Back to the Future"

	Scenario: El id "329" de la pelicula "Jurassic Park"
		Given: Se tiene el id "329" de la pelicula 
		When: Se selecciona la pelicula
		then: se obtiene sus datos detallados tal como "Jurassic Park"

	Scenario: El id "18" de la pelicula "The Fifth Element"
		Given: Se tiene el id "18" de la pelicula 
		When: Se selecciona la pelicula
		then: se obtiene sus datos detallados tal como "The Fifth Element"
		
