from .UnitArchetype import Unit

class Archer(Unit):
    def __init__(self):
        super().__init__(health=10, attack=2, defense=1, movement=1, range=2, cost=3, traits = [])

