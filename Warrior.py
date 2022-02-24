from Enemy import Enemy
from random import randint

class Warrior(Enemy):
    def Be_Attacked(self, Damage):
        damage = int(Damage - self.Armor * (randint(20, 50) / 100))
        self.HP -= damage
        return self.Name, damage, 0