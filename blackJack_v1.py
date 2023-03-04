from os import system
from ascii_art import logo
from random import choice

import os
rows, columns = os.popen('stty size', 'r').read().split()
star = ''.join(['='] * (int(columns) - 5))
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ]

def compare(player_cards, player_score, computer_cards, computer_score):
    if player_score > 21:
        result = "Your score exceeded 21. So You lose."
    elif computer_score == player_score:
        result = "Your score didn't exceeded 21, and it matches with Dealer's score. So It's a Draw."
    elif player_score == 21 and len(player_cards) == 2:
        result = "You got a Black-Jack, Dealer didn't. So You win!"
    elif computer_score > 21:
        result = "Dealer's score exceeded 21, your's didn't. So You win!"
    elif computer_score == 21 and len(computer_cards) == 2:
        result = "Dealer got a Black-Jack, you didn't. So You lose."
    elif player_score > computer_score:
        result = "Your score is greater than Dealer's score. So You win!"
    elif computer_score > player_score:
        result = "Dealer's score is greater than your score. So you lose."
    else:
        print(f"computer_score: {computer_score},  player_score: {player_score}.")
        result = "There's still a glitch."
    return result

def print_player(player_cards, player_score, computer_cards):
    print(f"Your cards: {player_cards}, Current score: {player_score}.")
    print(f"Dealer's first card: {computer_cards[0]}.")

def print_final(player_cards, player_score, computer_cards, computer_score):
    print(f"Your final cards: {player_cards}, final score: {player_score}.")
    print(f"Dealer's cards: {computer_cards}, score: {computer_score}.")
    result= compare(player_cards, player_score, computer_cards, computer_score)
    print(result)

def blackJack_main():
    if ans1 == 'y':
        system('clear')
        print(logo)

        player_cards = []
        player_score = 0

        computer_cards = []
        computer_score = 0
        card_count = [2, 3, 4, ]

        #draw cards until score 17
        while computer_score <= 17:
            rnd_card = choice(cards)
            computer_cards.append(rnd_card)
            computer_score = sum(computer_cards)
            if 11 in computer_cards and computer_score > 21:
                computer_cards.remove(11)
                computer_cards.append(1)
            computer_score = sum(computer_cards)

        result = ""
        for i in range(2):
            player_cards.append(choice(cards))
        player_score = sum(player_cards)
        print_player(player_cards, player_score, computer_cards)
        wanna_add = True
        while wanna_add:
            if player_score <= 21:
                ans2 = input("Wanna add another card, or flush out? Type 'y' to add, 'n' to flush out: ").lower()
                print(star)
                # print("=====================================================================================")
                if ans2 == 'y':
                    random_card = choice(cards)
                    player_cards.append(random_card)
                    player_score = sum(player_cards)
                    if 11 in player_cards and player_score > 21:
                        player_cards.remove(11)
                        player_cards.append(1)
                    player_score = sum(player_cards)
                    if player_score <= 21:
                        print_player(player_cards, player_score, computer_cards)
                else:
                    wanna_add = False
                    print_final(player_cards, player_score, computer_cards, computer_score)
                    print(star)
            else:
                wanna_add = False
                print_final(player_cards, player_score, computer_cards, computer_score)   
                print(star)
    else:
        return print("Goodbye!")
    
    ans3 = input("Wanna play again? Type 'y' to play again, 'n' to stop playing: ").lower()
    if ans3 == 'y':
        system('clear')
        blackJack_main()
    else:
        system('clear')
        return print("Goodbye!")

ans1 = input("Wanna play blackJack? Type 'y' to play, 'n' to abort: ").lower()
blackJack_main()