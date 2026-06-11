user = {
    'id': 101,
    "username": "jane_doe",
    'email': 'jane.doe@sample.com',
    'active': True
}

# print(user)
# print(user['id'])
# print(user.get('email'))
# print(user['usrename'])
# print(user.get('usrename', 'check the key again'))

user["firstname"] = 'Jane'
user["lastname"] = 'Doe'

user.update({'email': 'jone_doe@sample.com'})

user.update({'city': 'Bengaluru', 'state': 'Karnataka'})

print(user)

removed_val = user.pop('state')
print("Removed Value: ", removed_val)

dict_keys = user.keys()  # returns keys
dict_values = user.values() # returns values
dict_items = user.items()  # returns key:value pairs

print(dict_keys)
print(dict_values)
print(dict_items)