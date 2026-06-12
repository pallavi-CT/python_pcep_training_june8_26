# def greet():
#     print("Welcome to Python Functions")

# def greet(str):
#     print(f'Hello {str}')

# def greet(name: str, greeting: str='Hello') -> str:
#     return f'{greeting} {name.title()}'

# print(greet('Pallavi'))

# def min_max(numbers: list) -> (tuple):
#     """
#         returns (min, max) of a number list as tuple
#     """
#     return min(numbers), max(numbers)

# least, highest = min_max([5,2, 10, 1, 6, 8])
# print(f'Minumum: {least}, Maximun: {highest}')

# person = ('Al', 34, 'al@ex.com')
# # name = person[0]
# name, age, email = person

# def emp_details(name: str, dept: str, salary: float) -> dict:
#     return {'name': name, 'dept': dept, 'salary': salary}

# print(emp_details(dept='IT', name='Prithvi', salary=45000))

# def calc_average(*args) -> float:
#     return (sum(args)/len(args))

# # *args, **kwargs
# def calculate_sum(*values):
#     # num1, n2, n3, n4 = values
#     print(f'Total: {sum(values)}')
#     print(f'Mean: {calc_average(*values):.2f}')
#     print(f'Min: {min(values)}')
#     print(f'Count: {len(values)}')

# calculate_sum(20, 10, 30, 40)
# calculate_sum(1 ,2, 3,4,5,6,7,8,9,10)

# def emp_details(**attributes):
#     print(attributes)

# emp_details(name='Prithvi', dept='IT', salary=34500)

# def build_user_profile(id, **attributes):
#     """build user profile using **kwargs"""
#     profile = {"id": id}
#     profile.update(attributes)
#     return profile

# p = build_user_profile('U001', name='Prithvi', dept='IT', remote=True, level=3)
# print(f'Profile: {p}')



# --------------------------------------------
# Lambda Functions

# def square_root(x):
#     return x ** 2

# square_root = lambda x: x**2
# print(square_root(4))

# add = lambda a, b: a + b
# print(add(2, 4))


# prices = [250, 300.99, 180, 560.75, 490, 230.67]
# discounts = list(map(lambda p: round(p * 0.8, 2), prices))

# # val = lambda p: round(p * 0.8, 2)

# print(f'Prices: {prices}')
# print(f'Discounts: {discounts}')

# def apply_transformation(data: list, transform_fn):
#     return [transform_fn(item) for item in data]

# # print(apply_transformation([2, 4, 6], lambda x: x**2))
# print(apply_transformation(['hello', 'world'], str.title))

# ----------------------------------------------

#closures

# def outer():
#     message = "In outer function"

#     def inner():
#         print(message)
    
#     return inner

# val = outer()
# val()

# def make_multipler(factor):
#     def multiply(value):
#         return value * factor
    
#     return multiply

# double = make_multipler(2)
# triple = make_multipler(3)

# print(double(5))
# print(triple(4))

def fn_call(fn):
    def wrapper(*args, **kwargs):
        print(f'Calling: {fn.__name__}')
        result = fn(*args, **kwargs)
        print(f'Done: returned {result}')
        return result
    return wrapper

# @fn_call
# def add(*values):
#     return sum(values)

# add(23, 34, 2, 3)

# timing decorator
# import time

# def timer(fn):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = fn(*args, *kwargs)
#         end = time.time()

#         print(f'Execution time: {end - start}')
#         return result
#     return wrapper

# @timer
# def process():
#     time.sleep(5)

# process()
def greet():
    print("Hello World")

def authenticator(fn):
    def wrapper(user_type):
        if user_type == 'member' or user_type == 'admin':
            print(f'{user_type.title()}, Operation complete')
        else:
            print(f'{user_type.title()} -> Access Denied')
            return
        
        return fn(user_type)
    return wrapper

# @authenticator
# def update_user(user):
#     print('User updated')
#     greet()

# update_user('admin')
# update_user('member')
# update_user('guest')
# update_user('neighbor')