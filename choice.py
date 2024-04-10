from all_teams import *
from random import randint


def find_right_player(team, choice_of_player):
    count = 1
    for player in team.all_team:
        if count == choice_of_player:
            if player.is_alive:
                player.print_statistic()
                player.is_alive = False
                team.amount_of_alive_players -= 1
            else:
                print("Этот игрок уже играл. Выберите другого игрока: ")
                your_choice_of_player(team)
            return player
        count += 1
    print()


def find_right_player_computer(team, what_of_max):
    if what_of_max % 2 == 0:
        max_strenght = 0
        for player in team.all_team:
            if player.is_alive:
                if player.strenght > max_strenght:
                    max_strenght = player.strenght
        for player in team.all_team:
            if player.strenght == max_strenght:
                player.print_statistic()
                player.is_alive = False
                team.amount_of_alive_players -= 1
                return player
    elif what_of_max % 2 != 0:
        max_defence = 0
        for player in team.all_team:
            if player.is_alive:
                if player.defence > max_defence:
                    max_defence = player.defence
        for player in team.all_team:
            if player.defence == max_defence:
                player.print_statistic()
                player.is_alive = False
                team.amount_of_alive_players -= 1
                return player
    print()


def your_choice_of_team(all_available_teams):
    choice_of_team = int(input("Введите номер команды: "))
    all_available_teams[choice_of_team - 1].print_team_statistic
    return all_available_teams[choice_of_team - 1]   


def your_choice_of_player(your_team):
    choice_of_player = int(input(f"Выберите одного из {your_team.amount_of_alive_players} игроков: "))
    print("Ваш игрок:")
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


def computer_choice_of_player(computer_team, what_of_max):
    # computer_choice_of_player_1 = randint(1, 5)
    # while True:
    #     if computer_team.all_team[computer_choice_of_player_1-1].is_alive:
    #         break
    #     else:
    #         computer_choice_of_player_1 = randint(1, 5)
    print("Игрок компьютера: ")
    player = find_right_player_computer(computer_team, what_of_max)
    return player
    