from generate_player import *
from player import *
class TEAM:
    def __init__(self, name):
        self.name = name
        self.count_of_players = 5
        self.all_team = []
        self.number_of_fans = randint(100, 1000)
        self.amount_of_alive_players = 5
        self.budget = 5000
        self.number_of_players = 5
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
        number_of_player = [i + 1 for i in range(self.number_of_players)]
        print(f"Название команды: {self.name}")
        for player in self.all_team:
            print(f'Игрок номер {number_of_player[0]}')
            player.print_statistic()
            number_of_player.pop(0)
        print(f"Число болельщиков: {self.number_of_fans}")
        print(f"Бюджет команды: {self.budget}")
        print()
def revive_the_players(all_available_teams):
    for team in all_available_teams:
        for player in team.all_team:
            player.is_alive = True
        team.amount_of_alive_players = 5


def your_team_revive(your_team):
    count_player = 0
    for player in your_team.all_team:
        player.is_alive = True
        count_player += 1
    your_team.amount_of_alive_players = count_player