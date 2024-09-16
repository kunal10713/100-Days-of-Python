import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def starting():
    want_to_play = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    
    while want_to_play == 'y':

        user_starting_cards = [random.choice(cards), random.choice(cards)]
        computer_starting_cards = [random.choice(cards), random.choice(cards)]

        another_card = 'y'
        
        while another_card == 'y':
            user_score = sum(user_starting_cards)
            computer_score = sum(computer_starting_cards)
            
            print(f"Your cards: {user_starting_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_starting_cards[0]}")

            # Check if user or computer has blackjack
            if user_score == 21:
                print(f"Your final hand: {user_starting_cards}, final score: {user_score}")
                print("Blackjack! You win!")
                break
            elif computer_score == 21:
                print(f"Computer's final hand: {computer_starting_cards}, final score: {computer_score}")
                print("Computer has blackjack! You lose.")
                break
            
            # Check if user is bust
            if user_score > 21:
                if 11 in user_starting_cards:
                    user_starting_cards[user_starting_cards.index(11)] = 1  # Change ace value from 11 to 1
                    user_score = sum(user_starting_cards)
                if user_score > 21:
                    print(f"Your final hand: {user_starting_cards}, final score: {user_score}")
                    print(f"Computer's final hand: {computer_starting_cards}, final score: {computer_score}")
                    print("You went over. You lose.")
                    break
            
            another_card = input("Type 'y' to get another card, 'n' to pass: ")
            
            if another_card == 'y':
                user_starting_cards.append(random.choice(cards))
            else:
                while sum(computer_starting_cards) < 17:
                    computer_starting_cards.append(random.choice(cards))
                
                computer_score = sum(computer_starting_cards)
                
                if computer_score > 21:
                    print(f"Your final hand: {user_starting_cards}, final score: {user_score}")
                    print(f"Computer's final hand: {computer_starting_cards}, final score: {computer_score}")
                    print("Opponent went over. You win!")
                    break
                elif user_score > computer_score:
                    print(f"Your final hand: {user_starting_cards}, final score: {user_score}")
                    print(f"Computer's final hand: {computer_starting_cards}, final score: {computer_score}")
                    print("You win!")
                    break
                elif user_score < computer_score:
                    print(f"Your final hand: {user_starting_cards}, final score: {user_score}")
                    print(f"Computer's final hand: {computer_starting_cards}, final score: {computer_score}")
                    print("You lose.")
                    break
                else:
                    print(f"Your final hand: {user_starting_cards}, final score: {user_score}")
                    print(f"Computer's final hand: {computer_starting_cards}, final score: {computer_score}")
                    print("It's a draw.")
                    break
        
        # Prompt to play another game
        want_to_play = input("Do you want to play again? Type 'y' or 'n': ")
    
    print("Thanks for playing!")

starting()
