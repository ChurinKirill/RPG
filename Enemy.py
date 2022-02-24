from abc import ABC, abstractmethod

class Enemy(ABC):
    """Some entity that knows how to attack and be attacked."""
    def __init__(self, hp : int, damage : int, armor : int, name : str, specialty : str):
        self.HP = hp
        self.Armor = armor
        self.Damage = damage
        self.Name = name
        self.Specialty = specialty

    def Attack(self, enemy):
        result = enemy.Be_Attacked(self.Damage)
        return self.Name, result[0], result[1], result[2]

    @abstractmethod
    def Be_Attacked(self, Damage, Text):
        pass