import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

# Start an infinite loop
while True:
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

        # Check if the user entered a valid choice
        if user_choice >= 3 or user_choice < 0:
            print("You typed an invalid number, you lose!")
        else:
            # Generate the computer's choice
            computer_choice = random.randint(0, 2)
            print("Computer chose:")
            print(choices[computer_choice])

            # Determine the outcome
            if user_choice == 0 and computer_choice == 2:
                print("You win!")
            elif computer_choice == 0 and user_choice == 2:
                print("You lose")
            elif computer_choice > user_choice:
                print("You lose")
            elif user_choice > computer_choice:
                print("You win!")
            elif computer_choice == user_choice:
                print("It's a draw")

    # Handle the keyboard interruption to stop the loop
    except KeyboardInterrupt:
        print("\nGame terminated by the user. Goodbye!")
        break

    # Handle cases where the input is not a valid integer
    except ValueError:
        print("Invalid input. Please enter a number.")