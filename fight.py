from choice import *

      
def your_fight(your_player_strenght, computer_player_defence):
        p_1 = False
        procent = randint(0, 100)
        chance = (0.25 + your_player_strenght - computer_player_defence) * 100
        if procent < chance:
            print("Игрок забил гол")
            p_1 = True
        else:
            print("Игрок не забил гол")
            p_1 = False
        return p_1

def computer_fight(your_player_defence, computer_player_strenght):
        p_2 = False
        procent = randint(0, 100)
        chance = (0.25 + computer_player_strenght - your_player_defence) * 100
        if procent < chance:
            print("Компьютер забил гол")
            p_2 = True
        else:
            print("Компьютер не забил гол")
            p_2 = False
        return p_2
    


    