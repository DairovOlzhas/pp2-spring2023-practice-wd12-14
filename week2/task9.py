N = int(input())

sum_grades = {}
cnt_grades = {}

for i in range(N):
    student, grade = input().split(' ', 1)
    grade = int(grade)

    sum_grades[student] = sum_grades.get(student, 0) + grade
    cnt_grades[student] = cnt_grades.get(student, 0) + 1


for student, sum in sum_grades.items():
    print(student, sum_grades[student]/cnt_grades[student])


# for student, avg_grade in sum_grades.items():
#     print(student, avg_grade)