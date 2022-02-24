from Enemy import Enemy
from random import randint

class Archer(Enemy):
    def Be_Attacked(self, Damage):
        damage = Damage - self.Armor
        if randint(1, 10) == 3:
            damage = 0
        self.HP -= damage
        return self.Name, damage, 0