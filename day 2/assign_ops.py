# assignment ops -> =, += -= *= /= %= //= **=

# total_revenue = 0
# daily_sales = [1200, 980, 1450, 870, 2100]

# for sale in daily_sales:
#     total_revenue += sale
#     print(f' Running total: {total_revenue}')

# print(f"Total Revenue: {total_revenue}")

# bitwise ops -> & | ^ ~ << >>
READ = 0b001 #1
WRITE = 0b010 #2
ADMIN = 0b100 #4

user_permissions = READ | WRITE

print(f'User has READ permissions: {bool(user_permissions & READ)}')
print(f'User has WRITE permissions: {bool(user_permissions & WRITE)}')
print(f'User has ADMIN permissions: {bool(user_permissions & ADMIN)}')

# revoke permissions
user_permissions &= ~WRITE

print(f'Permissions: {user_permissions:04b} = {user_permissions}')

# 6 = 0b110