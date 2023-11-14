import pygame
from figur import Figur

class Entity(Figur):
    def __init__(self, bildesti: str,liv:int, navn: str):
        super().__init__(bildesti)

        self.liv = liv
        self.navn = navn


        def mist_liv(self):
            if self.navn == "boss":
                self.liv -= 5
            else:
                self.liv -=1