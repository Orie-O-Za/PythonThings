questions = []

def start_quiz(questions):
    score = 0
    for question in questions:
        print(questions["prompt"])
        for options in questions ["options"]
            print(options)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!")
            score += 1