# csv files read and write

from csv import reader, DictReader, DictWriter, writer

# read from a csv file in a list
# with open('employees.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
    
#     header = next(reader)    # skips the header row
    
#     for row in reader:
#         print(row)

# read from csv file in a dict
# with open('employees.csv', 'r', encoding='utf-8') as f:
#     reader = DictReader(f)

#     employees = list(reader)

#     # print(employees)
#     for emp in employees:
#         print(f"{emp['FIRST_NAME']} works in {emp['DEPARTMENT_ID']}, earns {emp['SALARY']}")
    
#     for emp in employees:
#         print(f"{emp}")

#     for i, emp in enumerate(employees):
#         print(f"{i} -> {emp}\n")

# writing into csv file using DictWriter

students = [
    {'id': 101, 'name': 'Jane Doe', 'email': 'jane.d@ex.c', 'dept': 'IT'},
    {'id': 102, 'name': 'John Doe', 'email': 'john.d@ex.c', 'dept': 'CSE'},
    {'id': 103, 'name': 'Simon Smith', 'email': 'simon.s@ex.c', 'dept': 'IT'},
    {'id': 104, 'name': 'Carol Reed', 'email': 'carol.r@ex.c', 'dept': 'Mechanical'}
]

try:
    with open('students.csv', 'a', encoding='utf-8', newline="") as f:
        fieldnames = ['id', 'name', 'email', 'dept']
        write_file = DictWriter(f, fieldnames=fieldnames)

        write_file.writeheader()   # writes the header row
        for row in students:
            write_file.writerow(row)
except Exception as e:
    print('Error: ', e)
    
print('Written successfully')