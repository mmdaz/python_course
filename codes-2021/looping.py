questions = ['name', 'quest', 'favorite color']
answers = ['Lancelot', 'To seek the holy grail', 'Blue']

for q, a in zip(questions, answers):
    print('What is your {0}? {1}.'.format(q, a))
