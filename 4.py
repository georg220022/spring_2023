import sys
import json


def count_questions(data: dict):
    sum_quest = 0
    for obj in data:
        if questions := obj.get("questions"):
            if isinstance(questions, list):
                sum_quest += len(questions)
            else:
                sum_quest += 1
    print(f"Всего вопросов: {sum_quest}")


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    answer_list = []
    for obj in data:
        if questions := obj.get("questions"):
            for question in questions:
                if correct_ans := question.get("correct_answer"):
                    if isinstance(correct_ans, list):
                        answer_list += correct_ans
                    else:
                        answer_list.append(correct_ans)
    print(f"Все правильные ответы: {answer_list}")


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    max_time = 0
    for obj in data:
        if questions := obj.get("questions"):
            for question in questions:
                if time_answer := question.get("time_to_answer"):
                    if max_time < time_answer:
                        max_time = time_answer
    print(f"Максимальное время ответа: {max_time}")


def main(args):
    # загрузить данные из test.json файла
    with open(args, "r") as f:
        row_data = json.load(f)
        if rounds := row_data.get("game", {}).get("rounds"):
            count_questions(rounds)
            print_right_answers(rounds)
            print_max_answer_time(rounds)


if __name__ == "__main__":
    # передать имя файла из аргументов командной строки
    if len(args := sys.argv) >= 2:
        main(args[1])
    else:
        print('Запуск файла только с аргументом, пример: "4.py test.json "')
