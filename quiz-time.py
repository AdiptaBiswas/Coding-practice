class Question:
    
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
questions = ["What is 1 + 1?\n(a)1\n(b)2\n(c)3\n", "What is the color of Orange?\n(a)Red\n(b)Orange\n(c)Green\n",
"What is the color of the sky?\n(a)White\n(b)Black\n(c)Blue\n"]

question_prompt = [Question(questions[0], "b"), Question(questions[1], "b"), Question(questions[2], "c")]

def quiz():
    score = 0
    for q in question_prompt:
        print(q.prompt)
        answer = input("Enter your response option: ")
        print("\n")
        if q.answer == answer:
            score += 1
    print("You completed the quiz. Please wait for your score.\n")
    for i in range(100000000):
        continue
    print("\nYou scored {}/{}, {}%\n".format(score, len(question_prompt), round((score/len(question_prompt))*100),2))
    print("Please play again. Thank You :)")
    
def welcome():
    print('''
    *************************
    ** WELCOME TO THE QUIZ **
    *************************\n
    ''')
    name = input("Please enter your name: ")
    print("\nHey "+name+". Are you all set for the quiz?\n")
    for i in range(10000000):
        continue
    print("Alright..\n")
    for i in range(10000000):
        continue
    print("Let's begin!\n")
    for i in range(100000000):
        continue
    quiz()
    
welcome()