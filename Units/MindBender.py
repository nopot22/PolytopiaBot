from .UnitArchetype import Unit

class MindBender(Unit):
    def __init__(self):
        super().__init__(health=10, attack=0, defense=1, movement=1, range=1, cost=5, traits = [])

