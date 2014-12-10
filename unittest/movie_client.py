import unittest
import sys
sys.path.append("../")
from src.movie_client import MovieClient, factoryGenericObject

class TestMovieClient(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.client = MovieClient()
        
    def test_obtenPelicula_22(self):
            pelicula = self.client.obtenPelicula(22)
            self.assertEqual("Pirates of the Caribbean: The Curse of the Black Pearl", 
                             pelicula.titulo)
            self.assertEqual(143, pelicula.duracion)

        
    def test_obtenActor_1231(self):    
        actor = self.client.obtenActor(1231)
        self.assertEqual("Julianne Moore", actor.nombre)
        self.assertEqual("1960-12-03", actor.fechaNacimiento)
   
    
    def test_buscarActor_willsmith_1(self):
        resultados = self.client.buscarActor("will smith", 1)
        self.assertTrue(len(resultados) > 10)
       
        
    def test_buscarPelicula_jurassicpark_1(self):
        resultados = self.client.buscarPelicula("jurassic park", 1)
        self.assertTrue(len(resultados) == 6)
    
    def test_obtenReparto_22(self):
        resultados = self.client.obtenRepartoPelicula(22)
        self.assertTrue(len(resultados) > 0)
        johnny = resultados[0]
        self.assertEqual("Jack Sparrow", johnny.papel)
        
    def test_json(self):
        result = self.client.getJSON("api.themoviedb.org", "/3/?api_key=1")
        self.assertEqual('{"status_code":7,"status_message":"Invalid API key: You must be granted a valid key."}',
                         result)
    
    def test_factory(self):
        result = factoryGenericObject({"hola" : "mundo"})
        self.assertEqual(result.hola,"mundo")
        
    
        
if __name__ == "__main__":
    unittest.main()