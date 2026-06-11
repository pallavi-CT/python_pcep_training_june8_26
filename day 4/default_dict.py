# Ex: Employee Performance Analysis

from collections import defaultdict, namedtuple

Employee = namedtuple("Employee", ['id', 'name', 'department', 'project', 'score'])

records = [
    Employee(101, "Prithvi", "IT", "Cloud", 85),
    Employee(102, "Poornima", "IT", "AI", 90),
    Employee(103, "Pranav", "Mechanical", "CAD", 78),
    Employee(104, "Riya", "IT", "Cloud", 88),
    Employee(105, "Kiran", "Mechanical", "CAD", 91),
    Employee(106, "Mohit", "Civil", "Bridge", 82),
    Employee(107, "Kanak", "IT", "AI", 83)
]

# group by department
dept_emps = defaultdict(list)

for emp in records:
    dept_emps[emp.department].append(emp.name)

# print(dict(dept_emps))

# calculate the average score by department
# dept_scores = defaultdict(list)

# for emp in records:
#     dept_scores[emp.department].append(emp.score)

# for dept, scores in dept_scores.items():
#     avg = sum(scores)/ len(scores)
#     print(f'{dept}: {avg:.2f}')


# top scorer in each department
top_scorers = defaultdict(lambda: ("", 0))   # {key: ("", 0)}
# print(top_scorers)
for emp in records:
    current_score = top_scorers[emp.department][1] # key is created => "IT":("", 0)
    if emp.score > current_score:
        top_scorers[emp.department] = (emp.name, emp.score)  # IT:("Prithvi", 85)

print(dict(top_scorers))