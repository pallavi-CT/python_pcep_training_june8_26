# boolean operators: and, or, not
# if - elif - else
age = 28
salary = 55000
credit = 620

# eligibility = (age > 21) and (salary > 40000) and (credit > 700)
# if eligibility:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible")

if age > 21:
    if salary > 40000:
        if credit > 700:
            print("Eligible for Loan - 100000")
    elif salary > 50000:
        if credit > 750:
            print("Eligible for Loan - 250000")
        else:
            print("Eligible for Loan - 100000")
else:
    print("Not Eligible")

    