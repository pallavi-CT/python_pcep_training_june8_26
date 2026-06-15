from age_validator import age_validator
from custom_exceptions import InsufficientFundsError

# import custom_exceptions as ce

# num1 = int(input('Enter numerator: '))
# num2 = int(input('Enter Deniminator: '))
# try: 
#     if num2 <= 0:
#         raise ZeroDivisionError('Denominator cannot be Zero')
#     else:
#         result = num1 / num2
#         print(f'{num1} / {num2}: {result}')
# except ZeroDivisionError as ex:
#     print("Message: ", ex)
# except Exception as ex:
#     print("Message: ", ex)
# finally:
#     print("In finally block")

# try:
#     result = age_validator(-1)
#     print('Result: ', result)
# except ValueError as ex:
#     print('Message: ', ex)
# # finally:
# #     print('in finally')
# else:
#     print('In else')

balance = 20000

withdrawal_amt = 23000

try:
    if withdrawal_amt > balance:
        raise InsufficientFundsError('Funds insufficient for withdrawal')
except InsufficientFundsError as ex:
    print('Error: ', ex)





