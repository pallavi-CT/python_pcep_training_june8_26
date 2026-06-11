# empty_set = set()
# print(empty_set)

# usernames = ['alice', 'bob', 'mark', 'ethan', 'mark', 'bob', 'alice', 'bob']
# unique_users = set(usernames)

# print(unique_users)

emp_referals = {'u01', 'u02', 'u04', 'u07'}
naukri_applications = {'u02', 'u03', None, 'u08'}
website_visitors = {'u01', 'u09'}
linkedin_users = {'u02', 'u05', 'u09'}

# union
true_applications = website_visitors & naukri_applications
# print("Serious applications: ", true_applications)

# intersection
set_applications = website_visitors | naukri_applications
# print(set_applications)

# difference -
difference_sets = naukri_applications - linkedin_users
print(difference_sets)

all_users = (
    emp_referals | naukri_applications | website_visitors | linkedin_users
)

single_application = {
    user for user in all_users
    if (
        (user in emp_referals) + (user in naukri_applications) +
        (user in website_visitors) + (user in linkedin_users)
    ) == 1
}

# single_application = (emp_referals ^ naukri_applications ^ website_visitors ^ linkedin_users)
print("Single Channel: ", single_application)

# diff = emp_referals ^ naukri_applications ^ website_visitors
# print(diff)