import random
from dino_runner.components.obstacle import Obstacle


class Cactus(Obstacle):     #Hereda el comportamiento de Obstacle
    def __init__(self, image):
        self.type = random.randint(0,2)                 #Genera un numero random(aleatorio) de 0 a 2 incluyendo el mismo
        super().__init__(image, self.type)              #Llama al constructor de la clase padre(Obstacle)

