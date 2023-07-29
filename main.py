import os
from art import logo
import random

cards = [11,2,3,4,5,6,7,11,8,9,10,10,10,10]

computer = []
player = []

def deal_card():
    
    random.shuffle(cards)
    rand_card = cards[random.randint(0,13)]
    return rand_card


def game_init():
    
    print(logo)
    player.append(deal_card())
    player.append(deal_card())
    # player.append(11)
    # player.append(10)
    
    computer.append(deal_card())
    computer.append(deal_card())
    
    
def isBlackJack(player):
    
    if len(player) == 2:
        if sum(player) == 21:
            return True
        else:
            return False
    else:
        return False
            
def calculate_score(player):

    if isBlackJack(player):
        return 0
    

    if sum(player) > 21:
        if 11 in player:
            player.remove(11)
            player.append(1)

    score = sum(player)
    return score
    
def compare(user_score,comp_score):

    if user_score == comp_score:
        print("It's a Draw!")
    elif comp_score == 0:
        print("Opponent get a BlackJack! YOU LOSE.")
    elif user_score == 0:
        print("You Got a BlackJack! YOU WIN.")
    elif user_score > 21:
        print("You went Over, YOU LOSE!")
    elif comp_score > 21:
        print("Opponent went Over, YOU WIN!")
    else:
        if comp_score > user_score:
            print("Oppenent have the Highest Score! YOU LOSE! ")
        else:
            print("You Have the highest Score! YOU WIN.")     


should_play = True
while(should_play):
    if input("Do you want to play a game of BlackJack? Type 'y' or 'n' : ") != 'y':
        should_play = False
        break
    os.system('cls')   
    game_init()
    end_of_game = False
    while(not end_of_game):

        player_score = calculate_score(player)
        computer_score = calculate_score(computer)
        print(f"Your Cards: {player}, current score: {21 if player_score == 0 else player_score}")
        print(f"Computer's first card: {computer[0]}")

        if computer_score == 0 or player_score == 0:
            end_of_game = True
        elif player_score >= 21:
            end_of_game = True
        else:
            if input("Type 'y' to draw another card, or type 'n' to pass: ") == 'y':
                player.append(deal_card())
            else:
                end_of_game = True
            
       


    while(computer_score < 17 and computer_score != 0):
        computer.append(deal_card())
        computer_score = calculate_score(computer)
        
    print(f"Your final Hands: {player}, final score: {21 if player_score == 0 else player_score}")
    if not player_score > 21:
        print(f"Computer's final Hands: {computer}, final score: {21 if computer_score == 0 else computer_score}")

    compare(player_score,computer_score)
    player.clear()
    computer.clear()


    