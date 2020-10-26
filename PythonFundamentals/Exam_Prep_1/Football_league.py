import re
key = input()

scores = {}
goals = {}

regen = re.compile(re.escape(key) + '\w*' + re.escape(key))

counter = 0

while True:
    matches = input()
    if matches == 'final':
        break
    list_matches = matches.split()
    final_score = list_matches[-1].split(':')

    collection = re.findall(regen, matches)
    TeamA = (collection[0][len(key):-len(key)][::-1]).upper()
    TeamB = (collection[1][len(key):-len(key)][::-1]).upper()
    if TeamA not in  scores:
         scores[TeamA] = 0
         goals[TeamA] = 0
    if TeamB not in scores:
         scores[TeamB] = 0
         goals[TeamB] = 0

    if int(final_score[0]) > int(final_score[1]):
        scores[TeamA] += 3
        goals[TeamA] += int(final_score[0])
        scores[TeamB] += 0
        goals[TeamB] += int(final_score[1])
    elif int(final_score[0]) < int(final_score[1]):
        scores[TeamA] += 0
        goals[TeamA] += int(final_score[0])
        scores[TeamB] += 3
        goals[TeamB] += int(final_score[1])
    elif int(final_score[0]) == int(final_score[1]):
        scores[TeamA] += 1
        goals[TeamA] += int(final_score[0])
        scores[TeamB] += 1
        goals[TeamB] += int(final_score[1])

sorted_scores = sorted(scores.items(), key=lambda kvp: (-kvp[1], kvp[0]))
sorted_goals = sorted(goals.items(), key=lambda kvp: (-kvp[1], kvp[0]))

print('League standings:')
counter = 1
for k,v in sorted_scores:
    print(f'{counter}. {k} {v}')
    counter += 1
print('Top 3 scored goals:')

for k,v in sorted_goals[0:3]:
    print(f'- {k} -> {v}')








