# Python quiz game

questions = ("Which fast food restaurant has the largest number of retail locations in the world?: ",
            "Which planet in the solar system is the hottest?: ",
            "What is the most visited tourist attraction in the world?: ",
            "What is the only food that cannot go bad?: ",
            "What's the name of Hagrid's pet spider?")

options = (("A. Jack In The Box", "B. Chipotle", "C. Subway", "D. McDonald's"),
           ("A. Mercury", "B. Earth", "C. Mars", "D. Venus"),
           ("A. Statue of Liberty", "B. Great Wall of China", "C. Colosseum", "D. Eiffel Tower"),
           ("A. Peanut butter", "B. Canned tuna", "C. Honey", "D. Dark chocolate"), 
           ("A. Nigini", "B. Crookshanks", "C. Aragog", "D. mosag"))

answers = ("C", "D", "D", "C", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("------------------")
print("      RESULT      ")
print("------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")