class Unit():
    def __init__(self, health: int, attack: int, defense: int, movement: int, range: int, cost: int, traits = []):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.movement = movement
        self.range = range
        self.cost = cost
        self.traits = traits
    
# Import all unit classes (add imports for each as you define them)
from .Warrior import Warrior
from .Archer import Archer
from .Catapult import Catapult
from .Cloak import Cloak
from .Defender import Defender
from .Knight import Knight
from .MindBender import MindBender
from .Rider import Rider
from .Swordsmen import Swordsmen


# Dictionary mapping unit names to classes
UNIT_CLASSES = {
    "warrior": Warrior,
    "archer": Archer,
    "catapult": Catapult,
    "cloak": Cloak,
    "defender": Defender,
    "knight": Knight,
    "mindbender": MindBender,
    "rider": Rider,
    "swordsmen": Swordsmen,
}

def get_unit_class(unit_name: str):
    """Returns the unit class object for the given name, or None if not found."""
    return UNIT_CLASSES.get(unit_name.lower())