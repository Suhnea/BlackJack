import os
import random

os.environ['TERM'] = 'xterm'

decks = input('Введите количество колод: ')
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * (int(decks) * 4)

wins = 0
losses = 0

def deal(deck_func):
    hand = []
    random.shuffle(deck_func)
    
    for i in range(2):
        card = deck_func.pop()

        if card == 11:
            card = "J"
        elif card == 12:
            card = "Q"
        elif card == 13:
            card = "K"
        elif card == 14:
            card = "A"
        
        hand.append(card)
    return hand

def play_again():
    again = input('Хотите сыграть снова? (Да/Нет) : ').lower()
    if again == "да":
        game()
    else:
        print("\033[0;35;40mКазино всегда выигрывает!\033[0m")
        exit()

def total(hand):
    points = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == "K":
            points += 10
        elif card == "A":
            if points >= 11:
                points += 1
            else:
                points += 11
        else:
            points += card
    return points

def hit(hand):
    card = deck.pop()

    if card == 11:
        card = "J"
    elif card == 12:
        card = "Q"
    elif card == 13:
        card = "K"
    elif card == 14:
        card = "A"
    
    hand.append(card)
    return hand

def print_results(dealer_hand, player_hand):
    print("\n*** РЕЗУЛЬТАТЫ РАУНДА ***\n")
    print("У раздающего на руке: " + str(dealer_hand) + ", в сумме: " + str(total(dealer_hand)))
    print("У вас на руке: " + str(player_hand) + ", в сумме: " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global losses

    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Поздравляю! У вас блек-джек, вы выиграли!\n")
        wins += 1
        play_again()

    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Простите, вы проиграли. У раздающего блек-джек.\n")
        losses += 1
        play_again()

    elif total(dealer_hand) == total(player_hand):
        print_results(dealer_hand, player_hand)
        print("У вас и у раздающего блек-джек. В этом раунде победителя нет.\n")
        play_again()

def score(dealer_hand, player_hand):
    global wins
    global losses

    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Поздравляю! У вас 21, вы выиграли!\n")
        wins += 1
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Простите, вы проиграли. У раздающего 21.\n")
        losses += 1
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("У вас перебор. Вы проиграли.\n")
        losses += 1
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("У раздающего перебор. Вы выиграли!\n")
        wins += 1
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("У раздающего больше очков, чем у вас. Вы проиграли.\n")
        losses += 1
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Поздравляю, у вас больше очков, чем у раздающего. Вы выиграли!\n")
        wins += 1
    elif total(player_hand) == total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Раздающий набрал столько же, сколько и вы. В этом раунде победителя нет.\n")
    
    play_again()

def game():
    global wins
    global losses

    print("\n    Новая игра!\n")
    print("-" * 30 + "\n")
    print("    \033[1;32;40mПОБЕДЫ:  \033[1;37;40m%s   \033[1;31;40mПОРАЖЕНИЯ:  \033[1;37;40m%s\n\033[0m" % (wins, losses))
    print("-" * 30 + "\n")

    dealer_hand = deal(deck)
    player_hand = deal(deck)

    print("Раздающий показывает " + str(dealer_hand[0]))
    print("У вас на руке: " + str(player_hand) + ", в сумме количество очков равно " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)

    while True:
        choice = input("\033[1;33;40mВы хотите [д]обрать карту, [о]становиться или [в]ыйти из игры? \033[0m").lower()
        if choice == 'д':
            hit(player_hand)
            print("У вас на руке: " + str(player_hand) + ", в сумме количество очков равно " + str(total(player_hand)))
            if total(player_hand) > 21:
                print('У вас перебор')
                losses += 1
                play_again()

        elif choice == 'о':
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print('Раздающий взял новую карту. У него на руках: ', dealer_hand)
                if total(dealer_hand) > 21:
                    print('У раздающего перебор, вы выиграли!')
                    wins += 1
                    play_again()

            score(dealer_hand, player_hand)

        elif choice == 'в':
            print("\033[0;35;40mКазино всегда выигрывает!\033[0m")
            exit()
        else:
            print("Неверный ввод. Пожалуйста, введите 'д', 'о' или 'в'.")

game()