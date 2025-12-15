from .UnitArchetype import Unit

class Defender(Unit):
    def __init__(self):
        super().__init__(health=15, attack=1, defense=3, movement=1, range=1, cost=3, traits = [])

