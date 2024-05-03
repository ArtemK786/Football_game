def choose_players(your_team):
    count_of_players = []
    while len(count_of_players) != 5:
        count_of_players_2 = 1
        player = int(input(f"Выберите {count_of_players_2} из 5 игроков, который будет играть: "))
        if not(player in count_of_players):
            count_of_players.append(player)
        elif player in count_of_players:
            player = int(input(("Этот игрок уже выбран, выберите другого: ")))
            count_of_players.append(player)
    for player in your_team.all_team:
        if not(((your_team.all_team.index(player) + 1) in count_of_players)):
            player.is_alive = False
            your_team.amount_of_alive_players -= 1
    print()
    print("Ваша команда")
    your_team.print_team_statistic()
