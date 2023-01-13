from random import randint
def play_game():
   secret_num = randint(1, 1000)
   guess = int(input("Угадайте число в диапазоне от 1 до 1000: "))
   guess_count = 1
   while secret_num != guess:
      if guess > secret_num:
         guess = int(input("Попробуй меньшее число: "))
      elif guess < secret_num:
         guess = int(input("Попробуй большее число: "))
      guess_count += 1
   print(f"Поздравляем! Вы угадали загаданное число за {guess_count} попыток")
play_game()