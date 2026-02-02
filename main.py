import random

def user_guess(num):

    chance = 5
    guessed_num = []

    while chance != 0:
     try: 
      print(f"Chances:{chance}")
      guess = int(input("Guess the number (1-20): "))
      
      if guess in guessed_num:
        print("You already used the number.")

      else:
         if guess == num:
           print("You guessed it correctly!")
           return True
         elif guess < num :
           print("Guessed number is less than the actual number")
         elif guess > num:
           print("Guessed number is greater than the actual number")

         chance -= 1
         guessed_num.append(guess)

      if chance == 0:
           print("You are out of guessing limits. Try again!")
      
     except ValueError:
          print("Number must be an integer.")
          pass

def main():

    print("*** NUMBER GUESSING GAME ***")
    num = random.randint(1,20) # returns random number within the range (1,100)
    
    user_guess(num)


main()
 
