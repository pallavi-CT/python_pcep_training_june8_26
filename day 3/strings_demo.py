# indexing -> positive and negative
# +ve -> 0 to n-1
# -ve -> -1 to -n

# language = 'Python'

# # print(language[0])
# # print(language[-1])

# # slicing
# print(language[1:3])
# print(language[3:]) # prints from index 3 onwards
# print(language[:4])

# print(language[::2])  # prints every second character
# print(language[::-1])  # prints in reverse

log_entry = "2026-06-10T09:30:25 | INFO | user_service | Login OK"

# date_part = log_entry[:10]
# time_part = log_entry[11:19]
# error_level = log_entry[22:26].strip()

# print(f'Date: {date_part}')
# print(f'Time: {time_part}')
# print(f'Error Level: {error_level}')

# string alignment
# print(f"{'Product':20} {'Price':>8} {'Stock':>6}")
# print(f"{'Laptop':20} {25000:>8.2f} {10:>6}")
# print(f"{'Headphones':20} {15600:>8.2f} {15:>6}")

# multi - line formatted strings
user = {'name': 'Prithvi', 'role': 'admin', 'logins': 120}

report = (
    f'=== User Report ===\n'
    f"Name: {user['name']}\n"
    f"Role: {user['role']}\n"
    f"Logins: {user['logins']}"
)

print(report)


# num = 32.3

# print(type(num))

