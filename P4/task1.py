from generator import fake_user_generator

class User:
    def __init__(self, username, age, gender, created_at):
        self.username = username
        self.age = age
        self.gender = gender
        self.created_at = created_at
    
    def age_group(self):
        if 0 <= self.age <= 12:
            return 'Child'
        elif 13 <= self.age <= 17:
            return 'Adolescent'
        elif 18 <= self.age <= 65:
            return 'Adult'
        elif 65 <= self.age <= 100:
            return 'Old adult'
        else:
            return 'unknown'

generated_users = fake_user_generator()

for _ in range(10):
    user = User(**next(generated_users))
    print(f'User: {user.username}, {user.age}, {user.gender}, {user.created_at}, {user.age_group()}')

# print(generated_user)

# user = User(
#     username=generated_user['username'],
#     age = generated_user['age'],
#     gender = generated_user['gender'],
#     created_at = generated_user['created_at'],
# )

# user = User(**generated_user)

