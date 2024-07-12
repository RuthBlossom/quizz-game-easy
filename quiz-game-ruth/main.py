# Importing necessary classes and modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create an empty list to store Question objects
question_bank = []

# Iterate over each question in the question_data list
for question in question_data:
    # Extract the question text and answer from the dictionary
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Create a new Question object using the extracted data
    new_question = Question(q_text=question_text, q_answer=question_answer)

    # Add the new Question object to the question_bank list
    question_bank.append(new_question)

# Create a QuizBrain object with the question_bank list
quiz = QuizBrain(question_bank)

# Loop through questions until there are no more questions
while quiz.still_has_questions():
    # Call the next_question method to ask the user the current question
    quiz.next_question()

# Print a completion message and the user's final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")

