from unittest import TestCase

from domain.src.screen.screen import Screen

class TestScreen(TestCase):
    def setUp(self) -> None:
        self.__screen = Screen()
    
    def test_shold_be_screen_has_instance_of(self):
        self.assertIsInstance(self.__screen, Screen)
    
    def tearDown(self) -> None:
        self.__screen = None
