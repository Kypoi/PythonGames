import csv
import os
from random import choice


class Question:
    def __init__(self, number, question, optionA, optionB, optionC, optionD, correctAnswer):
        self.number = number
        self.question = question
        self.optionA = optionA
        self.optionB = optionB
        self.optionC = optionC
        self.optionD = optionD
        self.correctAnswer = correctAnswer


def clear_console():
    os.system('cls')


def load_questions_from_csv(file_path):
    questions = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            questions.append(Question(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    return questions


def getFiftyFifty(question):
    wrong = 0

    match question.correctAnswer:
        case "a":
            wrong = choice([2, 3, 4])
            print(question.optionA)
        case "b":
            wrong = choice([1, 3, 4])
            print(question.optionB)
        case "c":
            wrong = choice([1, 2, 4])
            print(question.optionC)
        case "d":
            wrong = choice([1, 2, 3])
            print(question.optionD)
    match wrong:
        case 1:
            print(question.optionA)
        case 2:
            print(question.optionB)
        case 3:
            print(question.optionC)
        case 4:
            print(question.optionD)


def main():
    print("Bem-vindo ao Quem Quer Ser Milionário!")
    nome = input("Qual é o seu nome? ")
    print(f"Seja bem-vindo, {nome}! Vamos jogar!")
    file_path = "./questions"
    questions = load_questions_from_csv(file_path)
    play(questions)


def check_anwser(question, response, score):
    if response == question.correctAnswer:
        print("Correct!")
        return score + 1000
    else:
        print("Incorreto!")
        return score - 500


def play(questions):
    score = 0
    used_fifty_fifty = False
    used_skip = False
    for question in questions:
        print(question.number, question.question)
        print(question.optionA, question.optionB)
        print(question.optionC, question.optionD)
        print()
        response = input("R: ")

        if response == "skip" and used_skip == False:
            used_skip = True
            print("Skipped!")
            continue
        if response == "fifty" and used_fifty_fifty == False:
            used_fifty_fifty = True
            clear_console()
            getFiftyFifty(question)
            print("Fifty fifty!")
            response = input("R: ")
        score = check_anwser(question, response, score)
    print(f"Parabens o teu score foi {score}")


if __name__ == "__main__":
    main()
