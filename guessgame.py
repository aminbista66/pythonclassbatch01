import random
from datetime import datetime, timedelta

start_datetime = datetime.now()

def main():
    print("====== Number Guessing Game ======")

    computer_number = random.randint(1, 100)
    DIFFERNCE_THRESHOLD = 10

    while True:
        if start_datetime < datetime.now() - timedelta(seconds=10):
            print("Time is over")
            break

        # for better error message
        try:
            user_guess = int(input("Enter your Guess: ")) # this line needs only number
        except Exception:
            print("Enter a valid number")
            continue

        # checking user and computer number
        if user_guess == computer_number:
            print("You Win !!")
            break
        elif user_guess > computer_number:
            difference = user_guess - computer_number

            if difference > DIFFERNCE_THRESHOLD:
                print("Too High")
            else:
                print("High")
        else:
            difference = computer_number - user_guess
            
            if difference > DIFFERNCE_THRESHOLD:
                print("Too Low")
            else:
                print("Low")
main()