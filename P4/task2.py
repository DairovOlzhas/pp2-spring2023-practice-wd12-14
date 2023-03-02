from sample_inputs import users
from datetime import datetime

# {
#     "name": "Nursat Urazov",
#     "birthdate": "1975-03-15",
#     "height": 168
# }

def age(birthdate):
    birthdate_parsed = datetime.strptime(birthdate, '%Y-%m-%d')
    # print(type(birthdate_parsed))
    today = datetime.now()
    # print(type(today))
    age = today - birthdate_parsed
    # print(type(age))

    return age.total_seconds() // (365.25*24*60*60)

# age('1975-03-15')

def ab_groups(users, max_age):
    filtered_users = [
      user for user in users
      if age(user['birthdate']) <= max_age
    ]

    sorted_user = sorted(filtered_users, key=lambda user: age(user['birthdate']))

    group_a, group_b = [], []

    for i, user in enumerate(sorted_user):
        (group_a if i%2 else group_b).append(user)
        # if i%2==0:
        #     group_a.append(user)
        # else:
        #     group_b.append(user)
    
    return group_a, group_b


def average_age(users):
    return sum([age(user['birthdate']) for user in users]) / len(users)        

a, b = ab_groups(users, 40)

print('Group A:')
print('\n'.join(map(lambda i: str(i), a)))
print('Group B:')
print('\n'.join(map(lambda i: str(i), b)))
    # for i in users:
    #     if age(i['birthdate']) <= max_age:
    #         yield i

print('Group A avg age:', average_age(a))
print('Group B avg age:', average_age(b))


# max_age = 40
# a_group, b_group = ab_groups(users, max_age)
# print(len(a_group), len(b_group))
# print(average_height(a_group), average_height(b_group))