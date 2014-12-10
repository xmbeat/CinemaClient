Feature: Obtener datos generales de un actor o pelicula
	Como usuario
	quiero obtener los actores o peliculas que coincidan con patrones de busqueda
	para saber mas de ellos
	
	
	Scenario: El actor "will"
		Given: que se tiene "will"
		When: se realiza la busqueda de actor
		then: obtengo una lista mayor a "10" elementos
		
	Scenario: La pelicula "Jurassic Park III"
		Given: que se tiene "Jurassic Park III"
		When: se realiza la busqueda de pelicula
		then: obtengo una lista igual a "1" elementos