from .UnitArchetype import Unit

class Cloak(Unit):
    def __init__(self):
        super().__init__(health=5, attack=2, defense=0.5, movement=2, range=1, cost=8, traits = [])

