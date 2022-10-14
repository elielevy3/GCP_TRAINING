import pandas as pd
from random import sample
from contextlib import redirect_stdout


def print_question(question, data): 
    print("____________________________\n")
    print(data["Question"][question]) 
    print("____________________________\n")
    for x in ["A", "B", "C", "D", "E"]:
        if str(data[x][question]) != "nan":
            print(f"{x} : {data[x][question]}")


def export_wrongly_answered_questions(questions, data):
    with open('wrongly_answered_questions.txt', 'w') as out_file:
        with redirect_stdout(out_file):
            for question in questions: 
                print_question(question, data)
                print(f"\nThe right answer is : {data['result'][question]}")


def main():
    # ask the user how many questions he wants
    n = int(input("How many questions do you want ? : "))

    # retrieve data 
    data = pd.read_csv("Evaluation_test.csv",sep=";")

    # Final Score obtained
    score = 0

    # question number 
    number = 0 
    
    # list of questions sampled to avoid duplicate
    questions = sample(range(1, len(data)+1), n)

    # list of wrongly answered questions that shall be displayed in a output file at the end of the exam
    wrongly_answered_questions = []
    for i, number in enumerate(questions):

        # Display questions and possible answers
        print(f"\nQuestion {i} out of {n}")
        print_question(number, data)

        # blocking instruction that waits upon the user to enter an answer
        answer = input("\nEnter your anser : ")

        # Checking results 
        if answer == data["result"][number]:
            print("\nCORRECT\n")
            score += 1
        else:
            print("\nWRONG\n")
            print(f"The correct answer is : {data['result'][number]}")
            wrongly_answered_questions.append(number)
        print(f"Explanation : \n {data['explanation'][number]}")

        # get wrongly answered questions with correct answers to an output file
        export_wrongly_answered_questions(wrongly_answered_questions, data)

    print("\nEnd of the exam !\n")
    print(f"Score: {score} / {n}")
    print(f"Accuracy percentage : {round(score / n, 3)} %")


if __name__ == '__main__':
    main()
