grade = 0
credit = 0
sum_of_weighted_grade = 0
sum_of_credits = 0
sum_of_grades = 0
grade_list = []
while True:
    grade = float(input())
    if grade < 0:
        break
    credit = int(input())
    if grade >= 0:
        grade_list.append(grade)
        sum_of_weighted_grade += grade * credit
        sum_of_credits += credit
        sum_of_grades += grade

if sum_of_credits > 0:
    weighted_average_grade = sum_of_weighted_grade / sum_of_credits
    weighted_average_grade = round(weighted_average_grade, 2)



highest_grade = 0

for i in grade_list:
    if i > highest_grade:
        highest_grade = i
    
    
if sum_of_credits != 0:
    print("Weighted average grade:", weighted_average_grade)
if highest_grade != 0:
    print("Highest grade:", highest_grade)