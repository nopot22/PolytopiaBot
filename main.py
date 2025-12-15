from Units.UnitArchetype import get_unit_class

# Get the class object
unit_class = get_unit_class("WArrior")
if unit_class:
    # Call the constructor to create an instance
    warrior_unit = unit_class()
    print(f"Warrior health: {warrior_unit.health}")  # Output: Warrior health: 10