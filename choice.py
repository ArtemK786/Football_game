from all_teams import *
from random import randint

def find_right_player(team, choice_of_player):
    count = 1
    for player in team.all_team:
        if count == choice_of_player:
                player.print_statistic()
                team.all_team.remove(player)
                return player
        count += 1
    print()

def your_choice_of_team(all_available_teams):
    choice_of_team = int(input("Введите номер команды: "))
    all_available_teams[choice_of_team - 1].print_team_statistic
    return all_available_teams[choice_of_team - 1]   


def your_choice_of_player(your_team):
    choice_of_player = int(input(f"Выберите одного из {len(your_team.all_team)} игроков: "))
    print("Ваш игрок:" )
    player = find_right_player(your_team, choice_of_player)
    return player
    

def computer_choice_of_team(all_available_teams, your_team):
    computer_choice_of_team_1 = randint(0, 4)
    while True:
        if computer_choice_of_team_1 == all_available_teams.index(your_team):
            computer_choice_of_team_1 = randint(0, 4)
        else:
            break
    computer_team = all_available_teams[computer_choice_of_team_1]
    print(f"Компьютер выбрал команду {computer_team.name}")
    return computer_team
    
def computer_choice_of_player(computer_team):
    computer_choice_of_player_1 = randint(1, 5)
    print("Игрок компьютера: ")
    player = find_right_player(computer_team, computer_choice_of_player_1)
    return player
    