import colleted_data  # Dataset of people and follower count
import art  # ASCII art for the game visuals
import random  # For selecting random people

# Compare follower counts between two people
def check_followers(person_a, person_b):
    return person_a["follower_count"] > person_b["follower_count"]

# Perform comparison, take input, and return score
def compare(final_score):
    person_a = colleted_data.data[random.randint(0, len(colleted_data.data) - 1)]
    person_b = colleted_data.data[random.randint(0, len(colleted_data.data) - 1)]
    
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    print(f"{art.vs}")
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")
    
    guess = input("Who has more followers? Type 'A' or 'B'").upper()
    
    if (guess == 'A' and check_followers(person_a, person_b)) or (guess == 'B' and not check_followers(person_a, person_b)):
        final_score += 1
        return True, final_score
    else:
        print(f"Sorry, that's wrong. Final score {final_score}")
        return False, final_score

# Main game loop
def higher_lower():
    print(f"{art.logo}")
    print("Guess Who has more followers")
    
    correct_answer = True
    final_score = 0
    
    while correct_answer:
        correct_answer, final_score = compare(final_score)
        if correct_answer:
            print(f"You're right! Current Score {final_score}")

# Start the game
higher_lower()
