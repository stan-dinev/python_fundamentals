class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems

exercises = []
counter = 1

while True:
    n = input()
    if n == 'go go go':
        break

    n2 = n.split(' -> ')

    topic1 = n2[0]
    course_name1 = n2[1]
    judge_contest_link1 = n2[2]
    problems1 = n2[3].split(', ')

    My_exercise = Exercise(topic = topic1, course_name = course_name1, judge_contest_link = judge_contest_link1, problems = problems1)
    exercises.append(My_exercise)
for a in exercises:
    print(f'Exercises: {a.topic}')
    print(f'Problems for exercises and homework for the "{a.course_name}" course @ SoftUni.')
    print(f'Check your solutions here: {a.judge_contest_link}')
    counter = 1
    for b in a.problems:
        print(f'{counter}. {b}')
        counter += 1






