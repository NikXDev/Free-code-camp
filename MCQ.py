from Question import Question

question_prompts = [
    "What Color Are Apples?\n(a)Red\t(b)Purple\t(c)Orange\n",
    "\nWhat Color Are Strawberries?\n(a)Black\t(b)Teal\t(c)Pink\n",
    "\nWhat Color Are Bananas?\n(a)Magenta\t(b)Turquoise\t(c)Yellow\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")
]


def run_test(questions):
    score = 0
    length = len(question_prompts)
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f" You Scored {score}/{length} Questions Correctly....!!!")


run_test(questions)
