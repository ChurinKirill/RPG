import sys
from os import system
from random import randint, choice
from Archer import Archer
from Mage import Mage
from Warrior import Warrior
from datetime import date
from Printer import Printer

def BeginWar():
    while True:
        enemy1 = Get_random_enemy()
        enemy2 = Get_random_enemy()
        Battle(enemy1, enemy2)
        begin_result = printer.Begin_battle()
        if begin_result:
            cls()
            continue
        else:
            sys.exit()

def Battle(enemy1, enemy2):
    global printer

    printer.Start_battle(enemy1, enemy2)
    Text = ''
    printer.End_battle(enemy1, enemy2, Text)
    if enemy1.Specialty == 'Archer' and not enemy2.Specialty == 'Archer':
        result = enemy1.Attack(enemy2)
        Text += printer.complete_text(result[0], result[1], result[2], result[3])
        printer.End_battle(enemy1, enemy2, Text)
    elif enemy2.Specialty == 'Archer' and not enemy1.Specialty == 'Archer':
        result = enemy2.Attack(enemy1)
        Text += printer.complete_text(result[0], result[1], result[2], result[3])
        printer.End_battle(enemy1, enemy2, Text)

    while enemy1.HP > 0 and enemy2.HP > 0:
        Text = ''
        delay = input()
        Enemy = randint(0, 1)
        if Enemy == 0:
            result = enemy1.Attack(enemy2)
            Text = printer.complete_text(result[0], result[1], result[2], result[3])
        else:
            result = enemy2.Attack(enemy1)
            Text = printer.complete_text(result[0], result[1], result[2], result[3])

        printer.End_battle(enemy1, enemy2, Text)

    printer.End_war(enemy1, enemy2)
    Text = '\n\t**********\n'
    printer.PrintToFile(Text)

def Get_random_enemy():
    Names = ['Harold', 'Edward', 'Bill', 'Mike', 'John', 'Craig']
    Specialty = randint(0, 2)
    name = choice(Names)
    if Specialty == 0:
        enemy = Warrior(120 + randint(-5, 5), 30, 20, name, 'Warrior')
    elif Specialty == 1:
        enemy = Mage(70 + randint(-3, 3), 45, 10, name, 'Mage')
    else:
        enemy = Archer(80 + randint(-3, 3), 40, 0, name, 'Archer')
    Names.pop(Names.index(name))
    return enemy

printer = Printer("C:\\Users\Admin\MIniWar\Fights.txt")

start_result = printer.Start_war()
if start_result:
    cls()
    BeginWar()
else:
    sys.exit()