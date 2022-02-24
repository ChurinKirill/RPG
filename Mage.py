from Enemy import Enemy
from random import randint

class Mage(Enemy):
    def Be_Attacked(self, Damage):
        damage = Damage + randint(int((-Damage * 0.25)), 0)
        self.HP -= damage
        heal = 0
        if randint(1, 4) == 1 and self.HP < 70:
            heal = randint(10, 25)
            self.HP += heal
        return self.Name, damage, heal