import os
students = []
for file in os.listdir("scores"):
    with open("scores/" + file, "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            students.append((name, int(score)))

print("Total students:", len(students))

total = 0
for name, score in students:
    total += score
print("Total score:", total)

scores = [score for name, score in students]
print("Max:", max(scores))
print("Min:", min(scores))

new_scores = list(map(lambda x: x + 5, scores))
print("Increased:", new_scores)

top = list(filter(lambda x: x[1] > 85, students))
print("Top students:", top)

from functools import reduce
product = reduce(lambda x, y: x*y, scores)
print("Product:", product)

for i, (name, score) in enumerate(students):
    print(i+1, name, score)

names = [name for name, score in students]
print(list(zip(names, scores)))

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Sorted:")
for s in sorted_students:
    print(s)