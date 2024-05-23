from all_teams import *


def buy_players(your_team, all_available_teams):
    in_what_team_players = int(input("Напишите номер команды, в которой находиться нужный игрок: "))
    print()
    other_team = all_available_teams[in_what_team_players - 1]
    other_team.print_team_statistic()
    what_player = int(input("Номер игрока, который хотите купить: "))
    for player in other_team.all_team:
        if other_team.all_team.index(player) == what_player - 1:
            if your_team.budget > player.price:
                your_team.all_team.append(player)
                your_team.amount_of_alive_players += 1
                your_team.number_of_players += 1
                your_team.budget -= player.price
                other_team.budget += player.price
                other_team.all_team.remove(player)
                other_team.all_team.append(generate_player_1())
    your_team.print_team_statistic()


def exchange_players(your_team, all_available_teams):
    what_player_in_your_team = int(input("Номер игрока, которого хотите обменять: "))
    in_what_team_players = int(input("Напишите номер команды, в которой находиться нужный игрок: "))
    print()
    other_team = all_available_teams[in_what_team_players - 1]
    other_team.print_team_statistic()
    what_player_in_other_team = int(input("Номер игрока, на которого хотите обменять: "))
    your_player = your_team.all_team[what_player_in_your_team - 1]
    other_player = other_team.all_team[what_player_in_other_team - 1]
    if your_team.budget > other_player.price:
        if your_player.price > other_player.price:
            dop_price = your_player.price - other_player.price
            your_team.budget += dop_price
            other_team.budget -= dop_price
        elif your_player.price < other_player.price:
            dop_price = other_player.price - your_player.price
            your_team.budget -= dop_price
            other_team.budget += dop_price
        your_team.all_team.append(other_player)
        other_team.all_team.append(your_player)
        your_team.all_team.remove(your_player)
        other_team.all_team.remove(other_player)
        your_team.print_team_statistic()

    
def choice_of_func(your_team, all_available_teams, buy_or_exchange):
    if buy_or_exchange == 0:
        pass
    elif buy_or_exchange == 1:
        return buy_players(your_team, all_available_teams)
    elif buy_or_exchange == 2:
        exchange_players(your_team, all_available_teams)