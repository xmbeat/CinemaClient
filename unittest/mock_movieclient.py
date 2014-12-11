import unittest
import mock 
import sys
sys.path.append("../src/")
from movie_client import MovieClient
from identidad import Actor, Pelicula
class MockTest(unittest.TestCase):
    
    @mock.patch('movie_client.MovieClient')
    def test_updateActor_21(self, mock_cliente ):
        mock_cliente.updateActor.return_value = True
        val = mock_cliente.updateActor({"idActor":"21", "nombre": "Juan Hebert"})
        self.assertEqual(val, True)
        
    def test_obtenPelicula_22(self):
        cliente = MovieClient()
        cliente.obtenRepartoPelicula = mock.Mock(return_value = [{"idActor" : 31, "papel" : "tom hanks"}])
        
        pelicula = cliente.obtenPelicula(22)
        self.assertEqual(31, pelicula.reparto[0]["idActor"])
        
    @mock.patch('movie_client.MovieClient.getJSON')    
    def test_obtenActor_1231(self, mock_read):
        cliente = MovieClient()
        mock_read.return_value = '{"id": "1", "place_of_birth" : "Veracruz","name" : "Juan Hebert", "homepage" : "", "birthday" : "1992-11-12", "deathday":"", "profile_path": ""}'
        actor = cliente.obtenActor(1231)
        self.assertEqual("Juan Hebert", actor.nombre)
        self.assertEqual("1992-11-12", actor.fechaNacimiento)
    
    @mock.patch('movie_client.MovieClient.updateActor')
    def test_updateActor_1(self, mock_update):
        cliente = MovieClient()
        mock_update.return_value = True
        actor = Actor()
        actor.nombre = "Juan"
        actor.id = 1
        self.assertTrue(cliente.updateActor(actor))
        
    @mock.patch('movie_client.MovieClient.updatePelicula')
    def test_udpatePelicula_22(self, mock_update):
        cliente = MovieClient()
        mock_update.return_value = True
        pelicula = Pelicula()
        pelicula.id = 22
        pelicula.titulo = "Back to the future"
        self.assertTrue(cliente.updatePelicula(pelicula))
if __name__ == "__main__":
    unittest.main()
