questions = [
    {
        'question': 'Какой сегодня день?',
        'answers': [
            '0. Среда',
            '1. Четверг',
            '2. Пятница',
        ],
        'correct_answer': 1
    },
    {
        'question': 'Какой сегодня месяц?',
        'answers': [
            '0. Май',
            '1. Апрель',
            '2. Январь',
        ],
        'correct_answer': 2
    }
]

correct_answer_cnt = 0

for question in questions:
    print(question['question'])
    for answer in question['answers']:
        print(answer)
    
    user_answer = int(input())

    if user_answer == question['correct_answer']:
        correct_answer_cnt += 1

if correct_answer_cnt/len(questions) < 0.7:
    print('You lost!')
else:
    print('Congrats!')
