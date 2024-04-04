from generate_player import *
from player import *
class TEAM:
    def __init__(self, name):
        self.name = name
        self.count_of_players = 5
        self.all_team = []
        self.number_of_fans = randint(100, 1000)
    def generate_team(self):
        for i in range(self.count_of_players):
            player = generate_player_1()
            self.all_team.append(player)
    def atributes_with_fans(self):
        for player in self.all_team:
            player.strenght += round(player.strenght - (self.number_of_fans / 10 * 0.005), 3)
            if player.strenght > 1:
                    player.strenght = 1
            round(player.strenght, 3)
            player.defence += round(player.defence - (self.number_of_fans / 10 * 0.008), 3)
            if player.defence > 1:
                    player.defence = 1
            round(player.defence, 3)
    def print_team_statistic(self):
        number_of_player = [1, 2, 3, 4, 5]
        print(f"Название команды: {self.name}")
        for player in self.all_team:
            print(f'Игрок номер {number_of_player[0]}')
            player.print_statistic()
            number_of_player.pop(0)
        print(f"Число болельщиков: {self.number_of_fans}")
        print()

