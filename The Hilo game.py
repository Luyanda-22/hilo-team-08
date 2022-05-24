import random
import time 

print("Welcome to a game of Hilo")
time.sleep(0.5)

print()

name = input("What is your name? ")

print()

print(f"Hello {name}. You have 300 points.")


class cards:
    card = random.randint(1, 13)
    current_card = card
    next_card = card


    def current_card(self):
        return self.card

    def next_card(self):
        return self.card

card1 = cards()
print(card1.current_card())
card2 = cards()
print(card2.next_card())


points = 300

answer = print(input("Is the next card higher or lower? (higher / lower): "))

print(card2.next_card())


class score:

    if answer == 'higher' and card1.current_card() < card2.next_card():
        points += 100
        print(f'You have {points}.')
                
    elif answer == 'lower' and card1.current_card() > card2.next_card():
        points += 100
        print(f'You have {points}.')

    elif answer == 'higher' and card1.current_card() > card2.next_card():
        points -= 75
        print(f'You have {points}.')

    elif answer == 'lower' and card1.current_card() < card2.next_card():
        points -= 75
        print(f'You have {points}.')

    else:
        print('Invalid input. Please try again.')
        print(answer)

    if points == 0:
        print(f'You have {points}. Game Over. Thank you for playing')

    elif points != 0:
        keep_playing = (f'You have {points}. Would you like to continue playing? (Y/N). if you choose to play, type quit when you want the game to stop.')

    else:
        print('Draw!')

    while keep_playing == 'Y':
        print(answer)
        print()
    else: 
        'quit'
        print('Thank you for playing')

    if keep_playing == 'N':
        print('Thank you for playing.')

