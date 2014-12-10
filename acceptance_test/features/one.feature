Feature: Obtener datos generales de un actor
	Como usuario
	quiero obtener los actores que coincidan con patrones de busqueda
	para saber mas de ellos
	
	
	Scenario: El patron "will smith"
		Given: que se tiene "will smith"
		When: se realiza la busqueda
		then: obtengo una lista de cuando menos "0" elementos
		
	