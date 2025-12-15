from .UnitArchetype import Unit

class Knight(Unit):
    def __init__(self):
        super().__init__(health=10, attack=3.5, defense=1, movement=3, range=1, cost=8, traits = [])

