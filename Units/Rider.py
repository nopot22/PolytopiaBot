from .UnitArchetype import Unit

class Rider(Unit):
    def __init__(self):
        super().__init__(health=10, attack=2, defense=1, movement=2, range=1, cost=3, traits = [])

