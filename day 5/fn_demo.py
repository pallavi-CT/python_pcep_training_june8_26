from functions_demo import authenticator
# import functions_demo

@authenticator
def update_user(user):
    print('User updated')

update_user('admin')
update_user('member')
update_user('guest')
update_user('neighbor')


def authenticator(fn):
    def wrapper(user_type):
        if user_type == 'member' or user_type == 'admin':
            print(f'{user_type.title()}, Operation completed')
        else:
            print(f'{user_type.title()} -> Access Denied')
            return
        
        return fn(user_type)
    return wrapper