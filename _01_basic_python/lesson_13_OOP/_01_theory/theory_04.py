class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def is_correct(self, user_answer):
        return self.answer == user_answer


if __name__ == '__main__':
    question1 = Question('Самый крупный хищник', 'белый медведь')
    user_answer1 = input('Ваш ответ: ').strip().lower()
    print(question1.is_correct(user_answer1))
