questions = [
    {
    "prompt": "What is the capital of France?",
    "option": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
    "answer": "A",      
    },
    {
    "prompt": "What is the largest planet in our solar system?",
    "option": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"],
    "answer": "B",
    },
    {
    "prompt": "What is the chemical symbol for gold?",
    "option": ["A. Au", "B. Ag", "C. Pb", "D. Fe"],
    "answer": "A",
},
{
    "prompt": "Who wrote 'Romeo and Juliet'?",
    "option": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
    "answer": "B",
},
{
    "prompt": "What is the smallest prime number?",
    "option": ["A. 0", "B. 1", "C. 2", "D. 3"],
    "answer": "C",
},
{
    "prompt": "In South Africa, putting meat of a fire grill is called...?",
    "option": ["A. Braai", "B. Barbecue", "C. Grill", "D. Roast"],
    "answer": "A",
},
]

def mathaQuiz(questions):
    for question in questions:
        print(question["prompt"])
        for option in question["option"]:
            print(option)
        answer = input("Which option is your answer: \n")
        if answer.upper() == question["answer"]:
            print("Correct!\n")
        else:
            score = 0
            print(f"Eisan Eish!! Wrong! The correct answer is {question['answer']}")
    print(f"you got {score} out of {len(question)} correct!")

mathaQuiz(questions)

