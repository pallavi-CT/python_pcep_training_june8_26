# ternary/ inline conditional
# revenue = 125000
# status = "High" if revenue > 100000 else "Low"
# print(f'Revenue: {revenue}, Status: {status}')

products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']

# for index, product in enumerate(products, start=1):
#     print('Index: ', index, ' Product: ', product)

prices = [25000, 250, 600, 2800]
# for product, price in zip(products, prices):
#     print(f" {product} -> {price}")

# for i in range(200, 210):
#     print('Values: ', i)

# start_value = 1
# while start_value < 10:
#     print(start_value)
#     if start_value == 5:
#         break
#         # continue
#         # pass  # -- placeholder
#     else:
#         start_value += 1

# target_price = 250

# for price in prices:
#     if price == target_price:
#         print("Unknown price")
#         break
#         # continue
# else:
#     print("All prices Ok. Can proceed")

# syntax for match case
# match value:
#   case pattern1: 
#       code block
#   case _:

day = 'Tuesday'

# if day == 'Saturday' or day == 'Sunday':
#     print(f'{day} is a weekend')
# elif day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
#     print(f'{day} is a weekday')
# else:
#     print(f'{day} is not a valid day')    

match day:
    case 'Saturday' | 'Sunday':
        print(f'{day} is a weekend')
    case 'Monday' | 'Tuesday'| 'Wednesday' | 'Thursday' | 'Friday':
        print(f'{day} is a weekday')
    case _:
        print(f'{day} is not a valid day')

marks = 75

match marks:
    case x if marks > 80:
        print("Grade A")
    case _:
        print("Grade F")
