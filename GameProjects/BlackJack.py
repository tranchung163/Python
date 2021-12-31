import random

def deal_card():

  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card_choice = random.choice(cards)
  return card_choice

def calculate_score(cards):
  sum = 0

  for number in cards:
    sum = sum + number
  
  if sum == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum > 21:
    cards.remove(11)
    cards.append(1)

  return sum

user_cards = []
dealer_cards = []
is_game_over = False

for card in range(2):

  user_cards.append(deal_card())
  dealer_cards.append(deal_card())

while not is_game_over:

  print(f"your cards is: {user_cards}")
  print(f"dealer first card is: {dealer_cards[0]}")

  if calculate_score(user_cards) == 0 or calculate_score(dealer_cards) == 0 or calculate_score(user_cards) > 21:
    is_game_over = True

  else:
    dealer_should_hit = input("would you like to hit more card 'yes' or 'no':  ").lower()
    
    if dealer_should_hit == "yes":
      user_cards.append(deal_card())

      if calculate_score(user_cards) > 21 and 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)

    else:
      is_game_over = True

stop_game = False

if calculate_score(user_cards) > 21:
    print("YOU LOSE!!")
    print(f"Your cards are: {user_cards}")
    print(f"Your score is: {calculate_score(user_cards)}")
    print(f"Dealer cards are: {dealer_cards}")
    print(f"Dealer score is: {calculate_score(dealer_cards)}")
    stop_game = True


while calculate_score(dealer_cards) != 0 and calculate_score(dealer_cards) < 17:
  dealer_cards.append(deal_card())

def compare(usercards, dealercards):

  userscore = calculate_score(usercards)
  dealerscore = calculate_score(dealercards)

  if not stop_game:

    if userscore == 0 and dealerscore != 0 :
      print("BLACKJACK !!!!YOU WIN!!")
      print(f"Your cards are: {usercards}")

      print(f"Dealer cards are: {dealercards}")
      print(f"Dealer score is: {dealerscore}")

    elif userscore != 0 and dealerscore == 0:
      print("YOU LOSE!!")
      print(f"Your score is: {userscore}")
      print(f"Dealer cards is: {dealercards}")
      print(f"Dealer score is: {dealerscore}")

    elif userscore > 21 and dealerscore <= 21:
      print("YOU LOSE!!")
      print(f"Your score is: {userscore}")
      print(f"Dealer cards is: {dealercards}")
      print(f"Dealer score is: {dealerscore}")

    elif userscore <= 21 and dealerscore > 21:
      print("YOU WIN!!")
      print(f"Your score is: {userscore}")
      print(f"Dealer cards is: {dealercards}")
      print(f"Dealer score is: {dealerscore}")

    elif userscore > 21 and dealerscore > 21:
      print("DRAW!!")
      print(f"Your score is: {userscore}")
      print(f"Dealer cards is: {dealercards}")
      print(f"Dealer score is: {dealerscore}") 

    elif userscore > dealerscore:
      print("YOU WIN!!")
      print(f"Your score is: {userscore}")
      print(f"Dealer cards is: {dealercards}")
      print(f"Dealer score is: {dealerscore}")
      

    elif userscore < dealerscore:
      print("YOU LOSE!!")
      print(f"Your score is: {userscore}")
      print(f"Dealer cards is: {dealercards}")
      print(f"Dealer score is: {dealerscore}")

    elif userscore == dealerscore:
      print("DRAW!!")
      print(f"Your score is: {userscore}")
      print(f"Dealer cards is: {dealercards}")
      print(f"Dealer score is: {dealerscore}")

    elif userscore > 21 and dealerscore > 21:
      print("DRAW!!")
      print(f"Your score is: {userscore}")
      print(f"Dealer cards is: {dealercards}")
      print(f"Dealer score is: {dealerscore}") 

compare(user_cards, dealer_cards)
    





 





'''
if calculate_score(user_cards) == 0:
  print("you win!! ")



print(f"your cards is: {user_cards}")
print(f"dealer first card is: {dealer_cards[0]}")

stop = False
while not stop:
  hit = input("Do you want to hit: 'yes' or 'no' ").lower()
  if hit == "yes": 
    user_cards.append(deal_card())
    print(user_cards)
    if calculate_score(user_cards) > 21 :
      print("You lose!!!")
      stop = True    
  else:
    stop = True

stop1 = False
while not stop1:
  if calculate_score(dealer_cards) < 17:
    dealer_cards.append(deal_card())
  else:
    stop1 = True

  if calculate_score(user_cards) < calculate_score(dealer_cards) and calculate_score(dealer_cards) < 21:
    print("You lose!!")
    print(f"Your cards are : {user_cards}")
    print(f"Dealer cards are: {dealer_cards}")
    
  elif calculate_score(user_cards) > calculate_score(dealer_cards) and calculate_score(user_cards) < 21:
    print("You win!!")
    print(f"Your cards are : {user_cards}")
    print(f"Dealer cards are: {dealer_cards}")
    
  elif calculate_score(user_cards) == calculate_score(dealer_cards):
    print("Draw!!")
    print(f"Your cards are : {user_cards}")
    print(f"Dealer cards are: {dealer_cards}")'''
    
    
