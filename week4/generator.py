# generators.py
import random
import datetime

random_words = ['liam', 'snake', 'pool', 'ggg', 'hurray', 'yo', 'rock', 'football', 'basket', 'ice_cream', 'bing', 'chilling']
surnames = ['smith', 'black', 'white', 'johnson', 'williams', 'jones', 'millers', 'wilson', 'anderson', 'holmes', 'moore']

def fake_user_generator():
    i = 0
    while True:
        i+=1
        if i > 100:
            break
            
        username = (
            random.choice(random_words) 
            + str(random.choice(range(1000)))
            + random.choice(surnames)
        )

        age = random.choice(range(0,100))

        gender = random.choice(['male', 'female'])

        created_at = datetime.datetime.now().strftime('%x')

        yield {
            "username": username,
            "age": age,
            "gender": gender,
            "created_at": created_at
        }    
