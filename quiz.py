import random
import time

# Quiz questions with options and correct answers
quiz_questions = [
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["a) Jupiter", "b) Saturn", "c) Earth", "d) Mars"],
        "correct_answer": "a",
    },
    {
        "question": "Which famous scientist formulated the theory of general relativity?",
        "options": ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Nikola Tesla"],
        "correct_answer": "b",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["a) Go", "b) Au", "c) Gl", "d) Ag"],
        "correct_answer": "b",
    },
    {
        "question": "Which river is the longest in the world?",
        "options": ["a) Nile", "b) Amazon", "c) Mississippi", "d) Yangtze"],
        "correct_answer": "a",
    },
    {
        "question": "Which famous painting is known for its enigmatic smile?",
        "options": ["a) The Starry Night", "b) Guernica", "c) The Scream", "d) Mona Lisa"],
        "correct_answer": "d",
    },
]

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("Answer multiple-choice or fill-in-the-blank questions on a specific topic.")
    print("Let's see how well you can do!\n")

def display_question(question_data):
    print(question_data["question"])
    options = question_data["options"]
    random.shuffle(options)  # Randomize options for each question
    for option in options:
        print(option)
    print()

def get_user_answer():
    valid_options = ["a", "b", "c", "d"]
    while True:
        user_answer = input("Enter the letter corresponding to your answer: ").strip().lower()
        if user_answer in valid_options:
            return user_answer
        else:
            print("Invalid input. Please enter a valid option (a/b/c/d).")

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct answer!")
        return True
    else:
        print("Incorrect answer. The correct answer is:", correct_answer.upper())
        return False

def calculate_final_score(score, total_questions):
    return (score / total_questions) * 100

def display_final_results(score, total_questions):
    percentage_score = calculate_final_score(score, total_questions)
    print("\n----- Final Results -----")
    print("Total Questions: ", total_questions)
    print("Your Score: ", score, "/", total_questions)
    print("Percentage Score: {:.2f}%".format(percentage_score))

def play_again():
    play_again_input = input("\nDo you want to play again? (yes/no): ")
    return play_again_input.lower() == "yes"

def main():
    display_welcome_message()
    total_questions = len(quiz_questions)
    score = 0
    scorecard = []

    while True:
        random.shuffle(quiz_questions)

        for i, question_data in enumerate(quiz_questions):
            display_question(question_data)
            user_answer = get_user_answer()

            if evaluate_answer(user_answer, question_data["correct_answer"]):
                score += 1

            print("\n------------------------\n")
            time.sleep(1)  # Add a 1-second delay between questions for better flow

        scorecard.append((score, total_questions))
        display_final_results(score, total_questions)

        if not play_again():
            break

        print("\n------------------------\n")
        score = 0

    # Show scorecard after ending the game
    print("\n===== SCORECARD =====")
    for idx, (score, total) in enumerate(scorecard, start=1):
        percentage_score = calculate_final_score(score, total)
        print("Game {}: {} / {} - {:.2f}%".format(idx, score, total, percentage_score))

if __name__ == "__main__":
    main()
