from .UnitArchetype import Unit

class Warrior(Unit):
    def __init__(self):
        super().__init__(health=10, attack=2, defense=2, movement=1, range=1, cost=2, traits = [])

