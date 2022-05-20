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
    current_card = random.randint(1, 13)
    next_card = random.randint(1, 13)


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


class score:
    card2 = cards()
    print(card2.next_card())


    if answer == 'higher' and card1.current_card < card2.next_card:
        points = ({points} + 100)
        print(points)
 
    elif answer == 'lower' and card1.current_card > card2.next_card:
        points = ({points} + 100)
        print(points)
 
    elif answer == 'higher' and card1.current_card > card2.next_card:
        points = ({points} - 75)
        print(points)

    elif answer == 'lower' and card1.current_card < card2.next_card:
        points = ({points} - 75)
        print(points)

    else:
        print('Invalid input. Please try again.')
        answer




# if points == 0:
#     print('You lose. Thank you for playing')

# elif points != 0:
#     keep_playing = (f'You have {points}. Would you like to continue playing? (Y/N). if you choose to play, type quit when you want the game to stop.')


# while keep_playing == 'Y':
#     print(cards)
#     print()
#     print(answer)
#     print()
#     print(cards)
# else: 
#     'quit'
#     print('Thank you for playing')

# if keep_playing == 'N':
#     print('Thank you for playing.')
