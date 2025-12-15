from .UnitArchetype import Unit

class Swordsmen(Unit):
    def __init__(self):
        super().__init__(health=15, attack=3, defense=3, movement=1, range=1, cost=5, traits = [])

