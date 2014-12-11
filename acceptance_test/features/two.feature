
Feature: Obtener datos detallados de un actor
	Como usuario
	quiero obtener los detalles de un actor,
	para tener mas informacion de el
	
	
	Scenario: El id "1100" del actor
		Given: Se tiene el id "1100" del actor
		When: Se selecciona el actor
		then: se obtiene sus datos detallados como "Arnold Schwarzenegger"

	Scenario: El id "31" del actor
		Given: Se tiene el id "31" del actor
		When: Se selecciona el actor
		then: se obtiene sus datos detallados como "Tom Hanks"

	Scenario: El id "521" del actor
		Given: Se tiene el id "521" del actor 
		When: Se selecciona el actor
		then: se obtiene sus datos detallados como "Michael J. Fox"
		
