import unittest
from src.movie_client import MovieClient

class TestMovieClient(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.client = MovieClient()
        
    def test_obtenPelicula_22(self):
        try:
            pelicula = self.client.obtenPelicula(22)
            self.assertEqual("Pirates of the Caribbean: The Curse of the Black Pearl", 
                             pelicula.nombre)
            self.assertEqual(143, pelicula.duracion)
        except Exception as error:
            pass
        
    def test_obtenActor_1231(self):
        try:
            actor = self.client.obtenActor(1231)
            self.assertEqual("Julianne Moore", actor.nombre)
            self.assertEqual("1960-12-03", actor.fechaNacimiento)
        except Exception as error:
            pass
if __name__ == "__main__":
    unittest.main()