# colors = ['cyan', 'red', 'green', 'blue', 'black']
# iterator = iter(colors)

# # color = next(iterator)

# for color in iterator:
#     print(color)

# list comprehesion
# numbers = [2, 3, 4, 5, 6]
# squares = [num**2 for num in numbers]

# # for num in numbers:
# #     squares.append(num**2)

# print(squares)

prices = [450, 500, 60, 100, 250, 35]

# for price in prices:
#     if price > 250:
#         print(price)

high_prices = [price for price in prices if price > 250]
# print(high_prices)

raw_emails = [" john.doe@ex.com", "Jane.Doe@EX.COM", "", " john.s.ex.com", None]
# validated_emails = [
#     e.strip().lower()
#     for e in raw_emails
#     if e and "@" in str(e)
# ]

# validated_emails = []

# for e in raw_emails:
#     if (e != None or e != '') and "@" in str(e):
#         validated_emails.append(e.strip().lower())

# print(validated_emails)

records = [
    ("Prithvi", 85, "IT", 101),
    ("Pranav", 65, "Mech", 200),
    ("Poornima", 78, "IT", 210),
    ("Mohit", 81, "Civil", 45),
    ("Kanak", 89, "Mech", 670)
]

top_scorer = [
    r for r in records
    if r[2] == 'IT'
    and r[3] == max(x[3] for x in records if x[2] == 'IT')
]

print(top_scorer)
# it_team = [
#     r for r in records if r[2] == 'IT'
# ]

# high_scorer_it = max([r for r in it_team])

# it_team = []
# for r in records:
#     if r[2] == "IT":
#         it_team.append(r)

# print(it_team)
# print(high_scorer_it)