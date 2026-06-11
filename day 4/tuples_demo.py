from collections import namedtuple

# import collections


# rgb = (255, 255, 0)

# person = ("alice", 34, 'alice@example.com')
# name, age, email = person  #unpacking

# print("Original: ", person)

# # person[1] = 35

# age += 1
# person = (name.title(), age, email)

# print('After: ', person)
# print(name)

# numbers = (3,)
# print(type(numbers))

# name = person[0]

Person = namedtuple("Person", ["name", "age", "email"])
person = Person("Alice", 34, "alice@example.com")

print(person.name)