from .UnitArchetype import Unit

class Catapult(Unit):
    def __init__(self):
        super().__init__(health=10, attack=4, defense=0, movement=1, range=3, cost=8, traits = [])

