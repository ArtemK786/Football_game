from fight import *
from team import revive_the_players
from buy_or_exchange_players import choice_of_func
variant = 1
points = []
all_available_teams = set_teams()
while variant != 0:
        if variant == 3:
                all_available_teams = set_teams()
        revive_the_players(all_available_teams)
        print_all_available_teams(all_available_teams)
        your_team = your_choice_of_team(all_available_teams)
        buy_or_exchange = int(input("Если хотите купить игрока, нажмите 1\nЕсли обменять игрока, нажмите 2\nЕсли нет, нажмите 0: "))
        choice_of_func(your_team, all_available_teams, buy_or_exchange)
        your_player = your_choice_of_player(your_team)
        print()
        what_of_max = 1
        computer_team = computer_choice_of_team(all_available_teams, your_team)
        computer_player = computer_choice_of_player(computer_team, what_of_max)
        number_of_round = 1
        your_team_count = 0
        computer_team_count = 0
        while your_team.amount_of_alive_players > 0 and computer_team.amount_of_alive_players > 0:
                if number_of_round % 2 != 0:
                        count_your = your_fight(your_player.strenght, computer_player.defence)
                        number_of_round += 1
                        if count_your:
                                your_team_count += 1
                                your_player.price += randint(100, 200)
                        else:
                                your_player.price -= randint(100, 200)
                                computer_player.price += randint(100, 200)
                else:
                        count_computer = computer_fight(your_player.defence, computer_player.strenght)
                        number_of_round += 1
                        if count_computer:
                                computer_team_count += 1
                                computer_player.price += randint(100, 200)
                        else:
                                computer_player.price -= randint(100, 200)
                                your_player.price += randint(100, 200)
                print()
                what_of_max += 1
                print(f"Счет команды игрока {your_team_count}")
                print(f"Счёт команды компьютера {computer_team_count}")
                print()
                your_team.print_team_statistic()
                your_player = your_choice_of_player(your_team)
                print()
                computer_player = computer_choice_of_player(computer_team, what_of_max)
        print(f"Счет команды игрока {your_team_count}")
        print(f"Счёт команды компьютера {computer_team_count}")
        choice_of_winner(your_team_count, computer_team_count, computer_team, your_team)
        points.append(your_team_count)
        points.append(computer_team_count)
        print()
        print("Статистика за все игры")
        for i in range(0, len(points)-1, 2):
                print(f"Игрок: {points[i]} Компьютер: {points[i + 1]}")
        print()
        variant = int(input("Продолжить с теми же командами 1\nПродолжить с новыми командами 3\nЗавершить игру 0: "))
print("Спасибо, до свидания!")
    

