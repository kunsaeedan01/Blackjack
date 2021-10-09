import random
from art import logo
from replit import clear



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(massive):
  if sum(massive) == 21  and len(massive) == 2:
    return 0
  if sum(massive) > 21 and 11 in massive:
    massive.remove(11)
    massive.append(1)
  return sum(massive)


def compare(user_score, computer_score):
  if user_score == computer_score:
    return("It is draw")
  elif computer_score == 0:
    return "user is loser"
  elif user_score == 0:
    return "computer is loser"
  elif user_score > 21:
    return "user is loser"
  elif computer_score > 21:
    return "computer is loser"
  elif computer_score > user_score:
    return "user is loser"
  elif user_score > computer_score:
    return "computer is loser"

restart = "y"

while restart == "y": 
  user_cards = []
  computer_cards =[]
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, your score : {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      ask = input("y for get another card, n for stop")
      if ask == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True


  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score += calculate_score(computer_cards)

  print(f"{user_cards} + user score  {user_score}")
  print(f"{computer_cards}  computer score  {computer_score}")
  print(compare(user_score, computer_score))

  restart = input("y for restart and n for exit")

  if restart == "y":
    clear()
    print(logo)
    
