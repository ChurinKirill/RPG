from msvcrt import getch

class Printer:
    def __init__(self, path : str):
        self.path = path

    def complete_text(self, attacking : str, defencing : str, damage : int, healing : int):
        """Completes text from results"""
        Text = (attacking + ' is attacking')
        if damage == 0:
            Text += (', but ' + defencing + ' dodged the attack and took no damage!\n')
        elif healing > 0:
            Text += (' for ' + str(damage) + ' damage' + ', but ' + defencing + ' is healing ' + str(healing) + ' hp!\n')
        else:
            Text += (' for ' + str(damage) + ' damage!\n')
        return Text

    def PrintToConsole(self, Text):
        print(Text)

    def PrintToFile(self, Text):
        with open(self.path, 'a') as f:
            f.write(Text)

    def Start_war(self):
        print('Start war?\ny / n (exit)')
        key = ord(getch())
        while True:
            ch = chr(key)
            ch = ch.lower()
            if ch != 'y'and ch != 'n':
                print('Unknown key! Please try again!')
                print('Start war?\ny / n (exit)')
                key = ord(getch())
            if chr(key) == 'y':
                return True
            else:
                return False

    def Begin_battle(self):
        print('Begin new battle?\ny / n (exit)')
        key = ord(getch())
        while True:
            ch = chr(key)
            ch.lower()
            if ch != 'y'and ch != 'n':
                print('Unknown key! Please try again!')
                print('Begin new battle?\ny / n (exit)')
                key = ord(getch())
            if chr(key) == 'y':
                return True
            else:
                return False

    def Start_battle(self, enemy1, enemy2):
        """Prints start of the game"""
        Text = ('\n' + enemy1.Specialty + ' ' + enemy1.Name + ' vs ' + enemy2.Specialty + ' ' + enemy2.Name + '\n\n')
        self.PrintToConsole(Text)
        self.PrintToFile(Text)

    def End_battle(self, enemy1, enemy2, Text):
        """Prints results of the battle"""
        Text += (enemy1.Name + ' - ' + str(enemy1.HP) + ' hp ; ' + enemy2.Name +' - '  + str(enemy2.HP) + ' hp\n\n')
        self.PrintToConsole(Text)
        self.PrintToFile(Text)

    def End_war(self, enemy1, enemy2):
        """Prints results of the war"""
        Text = 'Winner is '
        if enemy1.HP > 0:
            Text += (enemy1.Name + '\n')
        else:
            Text += (enemy2.Name + '\n')
        self.PrintToConsole(Text)
        self.PrintToFile(Text)