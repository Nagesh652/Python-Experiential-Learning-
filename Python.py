import random


def play_round():
    print("\n========== NUMBER GUESSING GAME ==========")
    print("Choose Difficulty:")
    print("1. Easy   - 10 attempts")
    print("2. Medium - 7 attempts")
    print("3. Hard   - 5 attempts")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            max_attempts = 10
            break
        elif choice == "2":
            max_attempts = 7
            break
        elif choice == "3":
            max_attempts = 5
            break
        else:
            print("Invalid choice! Please enter 1, 2 or 3.")

    # Generate random number
    secret_number = random.randint(1, 100)

    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            # Correct guess
            if guess == secret_number:
                score = (max_attempts - attempts + 1) * 10

                print("\n🎉 Congratulations!")
                print("You guessed the correct number.")
                print("Number:", secret_number)
                print("Attempts:", attempts)
                print("Score:", score)

                return score

            # Guess is too low
            elif guess < secret_number:
                print("Hint: Your guess is TOO LOW.")

            # Guess is too high
            else:
                print("Hint: Your guess is TOO HIGH.")

            print("Attempts remaining:", max_attempts - attempts)

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Game over
    print("\n❌ GAME OVER!")
    print("The correct number was:", secret_number)
    print("Score: 0")

    return 0


# Main program
total_score = 0
total_rounds = 0

print("==========================================")
print("       🎯 NUMBER GUESSING GAME 🎯")
print("==========================================")

while True:

    total_rounds += 1

    score = play_round()
    total_score += score

    print("\n------------------------------------------")
    print("Round Score:", score)
    print("Total Score:", total_score)
    print("Rounds Played:", total_rounds)
    print("------------------------------------------")

    while True:
        again = input("\nDo you want to play another round? (yes/no): ").lower()

        if again == "yes":
            break
        elif again == "no":
            print("\n==========================================")
            print("             GAME FINISHED")
            print("==========================================")
            print("Total Rounds :", total_rounds)
            print("Final Score  :", total_score)
            print("Thank you for playing! 🎮")
            print("==========================================")
            exit()
        else:
            print("Please enter 'yes' or 'no'.")
