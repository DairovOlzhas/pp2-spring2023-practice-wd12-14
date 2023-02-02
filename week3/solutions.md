### Task 1

```python
def miniMaxSum(arr):
    minSum = sum(arr) - max(arr)
    maxSum = sum(arr) - min(arr)

    return minSum, maxSum

minSum, maxSum = miniMaxSum([1,3,5,7,9])

print(f"Minimum sum is {minSum}\nMaximum sum is {maxSum}")
```

OR

```python
miniMaxSum = lambda x: (sum(x) - max(x), sum(x) - min(x))

minSum, maxSum = miniMaxSum([1,3,5,7,9])

print(f"Minimum sum is {minSum}\nMaximum sum is {maxSum}")
```

### Task 2

```python
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def shift(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2)**0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"

point1 = Point(10,4)
point2 = Point(5,12)

print(point1.distance(point2))
point1.shift(10,1)
print(point1.distance(point2))
print(point2.__str__())
```

### Task 3

```python
def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)
```

### Task 4

```python
class Clothing:
    def __init__(self, name, size, color, price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price

    def display_info(self):
        print("Name:", self.name)
        print("Size:", self.size)
        print("Color:", self.color)
        print("Price:", self.price)

class Shirt(Clothing):
    def __init__(self, name, size, color, price, type):
        super().__init__(name, size, color, price)
        self.type = type

    def display_info(self):
        super().display_info()
        print("Type:", self.type)

class Pants(Clothing):
    def __init__(self, name, size, color, price, length):
        super().__init__(name, size, color, price)
        self.length = length

    def display_info(self):
        super().display_info()
        print("Length:", self.length)

# Example usage
shirt = Shirt("T-Shirt", "L", "Blue", 25.0, "Casual")
shirt.display_info()
# Output:
# Name: T-Shirt
# Size: L
# Color: Blue
# Price: 25.0
# Type: Casual

pants = Pants("Jeans", "M", "Blue", 50.0, "Regular")
pants.display_info()
# Output:
# Name: Jeans
# Size: M
# Color: Blue
# Price: 50.0
# Length: Regular
```

### Task 5

```python
def count_integer(list1):
    els = list(map(lambda i: isinstance(i, float), list1)) 
    result = len([e for e in els if e])         
    return result
    
list1 = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(count_integer(list1))
```


### Task 6

```python
class Person:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def sum_money(self):
        return self.fives*5 + self.tens*10 + self.twenties*20

def most_money(wallets):
    st_sum = {}
    for wallet in wallets:
        st_sum[wallet.name] = wallet.sum_money()
    return max(st_sum, key=lambda x:st_sum[x])

john = Person("John", 2, 2, 0)
alice = Person("Alice", 1, 3, 0)
mike = Person("Mike", 0, 0, 2)

print(most_money([john, alice, mike]))
print(most_money([john, alice]))
print(most_money([alice, mike]))
```


### Task 7

```python
def ispalindrome(string=None):
    index = len(string) - 1
    rightstring = ""
    while 0 <= index:
        rightstring += string[index]
        index = index - 1
    if rightstring == string:
        return True
    return False
```
```python
def isPalindromes(string):
    right_string = ""
    for index in range(1, len(string)+1):
        minus_index = 0 - index
        right_string += string[minus_index]
    if right_string == string:
        return True
    return False
```

### Task 8

```python
class Person:

    count_of_object = 0

    def __init__(self, name, family_name, age, occupation, nationality):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.occupation = occupation
        self.nationality = nationality
        Person.count_of_object += 1

    def get_name(self):
        return ("{name} {family_name}".format(name = self.name, family_name = self.family_name))

    def get_nationality(self):
        return self.nationality

    def get_age(self):
        return self.age

    def get_occupation(self):
        return self.occupation

    def year_born(self, cur_year):
        return cur_year - self.age

    def get_gender(self, gender):
        self.gender = gender
        return gender
```

### Task 9

```python
def get_arithmetic_operation(operator):
    if operator == '+':
        return lambda x, y: x + y
    elif operator == '-':
        return lambda x, y: x - y
    elif operator == '*':
        return lambda x, y: x * y
    elif operator == '/':
        return lambda x, y: x / y
    else:
        print(f'Invalid arithmetic operator `{operator}`.')

def get_conditional_operation(operator):
    if operator == '>':
        return lambda x, y: x > y
    elif operator == '<':
        return lambda x, y: x < y
    elif operator == '>=':
        return lambda x, y: x >= y
    elif operator == '<=':
        return lambda x, y: x <= y
    else:
        print(f'Invalid conditional operator `{operator}`.')


a = [1,2,3,4,5]
result = []

command, args = input().split(' ', 1)

if command in ['map', 'filter']:
    operator, operand = args.split(' ', 1)
    operand = int(operand)

    for elem_i in a:

        if command == 'map':
            result.append(get_arithmetic_operation(operator)(elem_i, operand))

        elif command == 'filter':
            if get_conditional_operation(operator)(elem_i, operand):
                result.append(elem_i)

elif command in ['progression', 'fold']:
    operator = args

    operation = get_arithmetic_operation(operator)

    result.append(a[0])

    for elem_i in a[1:]:

        if command == 'progression':
            result.append(operation(result[-1], elem_i))

        elif command == 'fold':
            result[0] = operation(result[0], elem_i)

print(result)
```

### Task 10
```python
class Polygon:

    def _is_polygon_can_exist(cls, edges: list[int]):
        sum_of_edges = sum(edges)

        for edge in edges:
            if edge >= sum_of_edges - edge or edge <= 0:
                return False

        return True

    def __init__(self, edges):
        self._edges = edges
        if not self._is_polygon_can_exist(edges):
            print(f"Polygon with edges {edges} can't exist.")

    def Set(self, new_edges):
        if len(new_edges) != len(self._edges):
            print(f"Error. New polygon have different number of edges.")
            return
        self._edges = new_edges
        if not self._is_polygon_can_exist(new_edges):
            print(f"Polygon with edges {new_edges} can't exist.")

    def Print(self):
        if self._is_polygon_can_exist(self._edges):
            print(
                f"It's {len(self._edges)}-gon with length of edges: "
                f"{', '.join(map(str,self._edges))}."
            )        
        else:
            print(f"Polygon with edges {self._edges} can't exist.")

class RightTriangle(Polygon):
    def _is_right_triangle(cls, edges):
        if len(edges) != 3:
            return False
        for i in range(3):
            edge1, edge2, edge3 = edges[i], edges[i-1], edges[i-2]
            if edge1 * edge1 == edge2 * edge2 + edge3 * edge3:
                return True
        return False

    def __init__(self, a, b, c):
        super().__init__([a,b,c])
        if not self._is_right_triangle(self._edges):
            print(f"It's not right triangle.")
    
    def Set(self, a, b, c):
        super().Set([a,b,c])
        if not self._is_right_triangle(self._edges):
            print(f"It's not right triangle.")
    
    def Print(self):
        if self._is_right_triangle(self.edges):
            print(f"It's not right triangle.")
        else:            
            print(
                f"It's right triangle with length of edges: "
                f"{', '.join(map(str,self._edges))}."
            )


a = Polygon([1,2,3])
a.Print()
```
### Task 11

```
def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, number + 1):
        if i * i > number:
            return True

        if number % i == 0:
            return False

def prime_with_prime_index(number: int) -> list:
    numbers = [i for i in range(2, number + 1)]

    primes = list(filter(is_prime, numbers))

    prime_indeces = list(filter(is_prime, range(1, len(primes) + 1)))

    return [primes[i - 1] for i in prime_indeces]

number = int(input())

print(prime_with_prime_index(number))
```

### Task 12

```
class Person:
    def __init__(self, name: str, age: int = 0) -> None:
        self.set_name(name=name)
        self.set_age(age=age)
        self._partner = None
        self._children = []
        self._status = 'Single'

    def procreate(cls, person1, person2):
        baby: Person = Person(f'Child of {person1.name} and {person2.name}')

        person1._children.append(baby)
        person2._children.append(baby)

        return baby

    def get_full_information(self):
        return f'Person {self.name} with age {self.age} and status {self.status} has partner {self.partner} and {self.children}'

    def get_children(self):
        if len(self._children):
            return f'{self.name} has {", ".join(map(str, self._children))} children'
        else:
            return '0 child'

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            print('Name must be `str` type')
            return

        if name == '':
            print('Name cannot be empty')
            return

        self._name = name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if not isinstance(age, int):
            print('Age must be `int` type')
            return

        if age < 0:
            print('Age cannot be less than zero')
            return

        self._age = age

    def get_partner(self):
        return self._partner

    def set_partner(self, person):
        self._partner = person

        if person != None:
            self.status = 'Married'
        else:
            self.status = 'Single'

    def set_status_with_partner(self, status, person):
        if self.partner and self.partner != person:
            self.status = 'Traitor'
        else:
            self.partner = person
            self.status = status

    def get_status(self):
        return self._status

    def set_status(self, status):
        if status in self.statuses:
            self._status = status

    def __str__(self) -> str:
        return f'Person {self._name}'

    def __repr__(self) -> str:
        return f'Person {self._name}'

    def __add__(self, person):
        if not self.partner and not person.partner:
            self.partner = person
            person.partner = self

            return

        self.set_status_with_partner('In love', person)
        person.set_status_with_partner('In love', self)

    def __mul__(self, person):
        return Person.procreate(self, person)

    def __sub__(self, person):
        if self.partner == person:
            self.partner = None

        if person.partner == self:
            person.partner = None

    def __del__(self):
        self.status = 'Dead'
        if self.partner:
            self.partner.partner = None

        del self

    age = property(get_age, set_age)
    name = property(get_name, set_name)
    children = property(get_children)
    partner = property(get_partner, set_partner)
    status = property(get_status, set_status)
    procreate = classmethod(procreate)
    statuses = ['Single', 'Married', 'In love', 'Traitor', 'Dead']
```

### Task 13

### Task 14
