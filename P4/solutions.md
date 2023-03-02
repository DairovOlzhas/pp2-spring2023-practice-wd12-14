### Task 1

<!-- generators.py -->

**generators.py**

```python
import random
from datetime import datetime

random_words = ['liam', 'snake', 'pool', 'ggg', 'hurray', 'yo', 'rock', 'football', 'basket', 'ice_cream', 'bing', 'chilling']
surnames = ['smith', 'black', 'white', 'johnson', 'williams', 'jones', 'millers', 'wilson', 'anderson', 'holmes', 'moore']

def fake_user_generator():
    i = -1
    while True:
        # The generator has a limit of up to 100 data
        i+=1
        if i == 100:
            break

        # Main code
        username = random.choice(random_words) + str(random.randint(0, 1000)) + random.choice(surnames)
        data = {
            "username": username,
            "age": random.randint(0, 100),
            "gender": random.choice(['female', 'male']),
            "created_at": str(datetime.now().strftime("%x"))
        }

        yield data
```

<!-- main.py(task1.py) -->

**main.py(task1.py)**

```python
from generators import fake_user_generator

class User:
    def __init__(self, username, age, gender, created_at):
        self.username = username
        self.age = age
        self.gender = gender
        self.created_at = created_at

    def age_group(self):
        if self.age <= 12:
            return 'Child'
        elif self.age <= 17:
            return 'Adolescent'
        elif self.age <= 65:
            return 'Adult'
        else:
            return 'Old adult'


user_generator = fake_user_generator()

for _ in range(10):
    new_user = next(user_generator)

    print('User:', new_user)
    user = User(new_user['username'], new_user['age'], new_user['gender'], new_user['created_at'])
    print(f'{user.username} age group is', user.age_group(), "\n")
```

### Task 2

### Task 3

```python
from datetime import datetime

from sample_inputs import users


def age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def parse_datetime(datetime_str):
    return datetime.strptime(datetime_str, '%Y-%m-%d')


def ab_groups(data, max_age):
    filtered_data = (person for person in data if age(parse_datetime(person['birthdate'])) <= max_age)
    sorted_data = sorted(filtered_data, key=lambda x: x['height'])
    group_a, group_b = [], []
    for i in range(len(sorted_data)):
        (group_a if i % 2 == 0 else group_b).append(sorted_data[i])
    return group_a, group_b


def average_height(data):
    total_height = sum(person['height'] for person in data)
    avg_height = total_height / len(data)
    return avg_height


max_age = 40
groups = ab_groups(users, max_age)

group_a, group_b = groups

a_av_h = average_height(group_a)
b_av_h = average_height(group_b)

print(len(group_a), len(group_b))
print(a_av_h, b_av_h)
```

### Task 4

### Task 5

```python
class CycleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.iterable_obj = 0

    def __next__(self):
        if self.iterable_obj >= self.max_times:
            raise StopIteration
        value = self.data[self.iterable_obj % len(self.data)]
        self.iterable_obj += 1
        return value

class Cycle():

    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CycleIterator(self.data, self.max_times)

c = Cycle('abc', 5)
# c = Cycle('string', 9)
print(list(c))        # prints a, b, c, a, b
```

### Task 6

### Task 7
```python
class FibonacciIterator:
    def __init__(self):
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

def get_fibonacci_numbers(n):
    iterator = FibonacciIterator()
    result = []
    for i in range(n):
        result.append(next(iterator))
    return result
```

### Task 8

### Task 9

```python
import json
import math

def point_distance(p1, p2):
    return math.sqrt((p2['x'] - p1['x']) ** 2 + (p2['y'] - p1['y']) ** 2)

def closest_pair(points):
    n = len(points)
    min_dist = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            dist = point_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def sum_distances_to_origin(points):
    return sum([math.sqrt(p['x'] ** 2 + p['y'] ** 2) for p in points])

def average_angle(points):
    angles = []
    n = len(points)
    for i in range(n-1):
        angle = math.atan2(points[i+1]['y'] - points[i]['y'], points[i+1]['x'] - points[i]['x'])
        angles.append(angle)
    avg_angle = sum(angles) / len(angles)
    return math.degrees(avg_angle)

def calculate_point_statistics(json_string):
    points = json.loads(json_string)
    closest_pair_distance = closest_pair(points)
    sum_of_distances_to_origin = sum_distances_to_origin(points)
    average_angle_between_points = average_angle(points)
    result = {
        'closest_pair_distance': closest_pair_distance,
        'sum_of_distances_to_origin': sum_of_distances_to_origin,
        'average_angle_between_points': average_angle_between_points
    }
    return json.dumps(result)

json_string = '[{"x":0, "y":0}, {"x":1, "y":1}, {"x":2, "y":2}, {"x":3, "y":3}]'
result = calculate_point_statistics(json_string)
print(result) 
# Output: {"closest_pair_distance": 1.4142135623730951, "sum_of_distances_to_origin": 5.656854249492381, "average_angle_between_points": 45.0}

```

### Task 10

### Task 11

```python
import datetime


class Example:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self.Inner_iter(self.n)

    class Inner_iter:
        def __init__(self, n):
            self.i = 0
            self.n = n

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < self.n:
                i = self.i
                self.i += 1

                return int(i * (i + 1) / 2)
            else:
                raise StopIteration()


    class Reverse_iter:
        def __init__(self, iter):
            self.data = list(iter)
            self.index = len(self.data)

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.index < 1:
                raise StopIteration
            
            self.index -= 1
            return self.data[self.index]


    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def take(n, iterator):
        ret = []
        for i in range(n):
            ret.append(next(iterator))

        return ret

    def get_generator():
        return ((x, y, z) for z in Example.integers() 
                          for y in range(1, z) 
                          for x in range(1, y) 
                          if x ** 2 + y ** 2 == z ** 2)

    def to_day(n, month):
        if month == 2:
            return (n + 27) % 28 + 1
        elif month in [4, 6, 9, 11]:
            return (n + 28) % 30 + 1
        else:
            return n % 31 + 1

    def to_mon(n):
        return (n + 11) % 12 + 1

    def to_year(n):
        return 2000 + n

    def conver_to_dates(arr):
        result = []

        for i in arr:
            year = Example.to_year(i[2])
            mon = Example.to_mon(i[1])
            day = Example.to_day(i[0], mon)

            result.append(datetime.datetime(year=year, month=mon, day=day))

        return result

    def date_in_format(date: datetime.datetime, format=1):
        if format == 1:
            return date.strftime('%d/%m/%Y')
        elif format == 2:
            return date.strftime('%Y-%m-%d')
        elif format == 3:
            return date.strftime('%d %B, %Y')
        else:
            print('unsupported format')
            return None

```

### Task 12

### Task 13
```python
import math

def find_roots(input_dict):
    a = input_dict["a"]
    b = input_dict["b"]
    c = input_dict["c"]
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x, x)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)
```
### Task 14

```
python
import json
from collections import Counter

def count_words(input_file_path, output_file_path):
    with open(input_file_path) as f:
        sentences = json.load(f)

    word_counts = Counter()
    for sentence in sentences:
        words = sentence.lower().split()
        word_counts.update(words)

    with open(output_file_path, 'w') as f:
        json.dump(dict(word_counts), f)
