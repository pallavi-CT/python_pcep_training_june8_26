"""
string methods:
strip, lstrip, rstrip
upper, lower, title
split
join
replace
find, index
count
isdigit, isalpha, isalnum
startswith, endswith
length
"""

# string methods sample
# email_raw = "Alice.Smith@examPLE.COM"
# cleaned_email = email_raw.strip().lower()

# username = 'alice_190'
# username = username.strip()

# if not (3 <= len(username) <= 20):
#     print('username must be 3 to 20 characters')

# if not username.isalnum() and "_" not in username:
#     print('Only letters, numbers and underscore allowed')

# if username[0].isdigit():
#     print('Username cannot start with a number')

# found = username.find("li")

# new_name = username.replace('a', 's', 1)

# # found = username.index('li')

# print(f'Username: {username}')
# print(f'Email: {cleaned_email}')
# print(f'Found? {found}')
# print(f'New username: {new_name}')

url = "https://shop.example.com/products/laptop-dell?ref=google"

protocol = url.split("://")[0]
domain_init = url.split("://")[1]
# print(domain_init)
domain = domain_init.split("/")[0]
# print('Domain: ', domain)
# path = "/".join(url.split("/")[3:]).split('?')[0]  # 
path = '/'+'/'.join(url.split('/')[3:]).split('?')[0]
print(path)

# split_url = url.split('/')
# print(split_url)

# domain = split_url[0].split(':')[0]
# print('Domain ', domain)