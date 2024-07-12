class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.score = 0
    self.question_list = q_list

  def still_has_questions(self):
    # Returns True if there are still questions left in the list, otherwise returns False.
    return self.question_number < len(self.question_list)

  def next_question(self):
    # Retrieve the current question from the list
    current_question = self.question_list[self.question_number]
    self.question_number += 1  # Move on to the next question for the next iteration.

    # Ask the user the current question and get their answer
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

    # Check the user's answer against the correct answer and update the score
    self.check_answer(user_answer, current_question.answer)

  def check_answer(self, user_answer, correct_answer):
    # If you want to check and print whether the user got it right immediately, you can do something like:
    # This converts the user's input (user_answer) to lowercase. This is done to make the comparison case-insensitive.
    if user_answer.lower() == correct_answer.lower():
      self.score += 1
      print("You got it right!")
    else:
      print("That's wrong.")

    print(f"The correct answer is {correct_answer}.")
    print(f"Your current score is {self.score}/{self.question_number}.")
    print("\n")  # Adding a new line for better readability


