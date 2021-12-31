from random import randint

HARD_CHOICE = 5
EASY_CHOICE = 10

def check(guess, answer, turns):
    
  if guess == answer:
    print(f"You got it!! The answer is: {answer}")

  elif guess > answer:
    print("The answer is too high")
    return turns - 1

  elif guess < answer:
    print("The answer is too low")
    return turns - 1
    
print("WELCOME TO THE GAME!!")
print("Guess the correct number in the range of 1 to 100")
answer = randint(1,100)


def game():
  
  level = input("what choose a difficulty. 'easy' or 'hard': ")

  if level == "easy":
    choose = EASY_CHOICE
    
  else:
    choose = HARD_CHOICE

  guess = 0
  
  while answer != guess:
    guess = int(input("guess a number: "))
    choose = check(guess, answer, choose)

    if choose == 0:
      print(f"the answer is: {answer}")
      return

game()

