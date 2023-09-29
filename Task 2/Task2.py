class Quiz:
    def __init__(self):
        self.questions = []
        self.user_name = ""

    def get_user_name(self):
        self.user_name = input("Enter your name: ")

    def add_question(self, question, options, correct_option):
        self.questions.append({
            'question': question,
            'options': options,
            'correct_option': correct_option
        })

    def run_quiz(self):
        score = 0
        for idx, question_data in enumerate(self.questions, start=1):
            print(f"Question {idx}: {question_data['question']}")
            for i, option in enumerate(question_data['options'], start=1):
                print(f"{i}. {option}")
            
            user_answer = input("Your choice (enter the number): ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(question_data['options']):
                user_answer = int(user_answer)
                if question_data['options'][user_answer - 1] == question_data['correct_option']:
                    score += 1
                    print("Correct!")
                else:
                    print(f"Wrong. The correct answer is: {question_data['correct_option']}")
            else:
                print("Invalid input. Skipping this question.")

        print(f"Dear {self.user_name}, your score: {score}/{len(self.questions)}")

# Create a quiz instance
quiz = Quiz()

while True:
    print("Welcome to the Quiz Application!")
    print("1. Start the Quiz")
    print("2. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Get the user's name
        quiz.get_user_name()

        # Add multiple-choice questions
        quiz.add_question("Who is the father of Geometry?", ["Aristotle","Euclid","Pythagoras", "Kepler"], "Euclid")
        quiz.add_question("Which currency has emerged as the best-performing currency of the September quarter in 2023?", ["US Dollar", "Euro", "Japanese Yen", "Afghani"], "Afghani")
        quiz.add_question("Who is currently the richest man in India as of August 2023?", ["Gautam Adani", "Cyrus Poonawalla", "Shiv Nadar", "Mukesh Ambani"], "Mukesh Ambani")

        # Run the quiz
        print(f"Welcome, {quiz.user_name}, to the Quiz Application!")
        quiz.run_quiz()

    elif choice == "2":
        print("\n~~~~ Thank you for using the Quiz Application ~~~~\n")
        break

    else:
        print("Invalid choice. Please enter 1 to start the quiz or 2 to quit.")
