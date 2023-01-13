from random import randint
def play_game():
   secret_number = randint(1, 1000)
   guess = int(input("Guess a number between 1 and 1000: "))
   guess_count = 1
   while secret_number != guess:
      if guess > secret_number:
         guess = int(input("Guess a lower number: "))
      elif guess < secret_number:
         guess = int(input("Guess a higher number: "))
      guess_count += 1
   print(f"Yay! You won in {guess_count} turns!")
play_game()