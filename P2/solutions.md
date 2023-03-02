### Task 1

```python
products = "apple candy grape banana"

array_products = products.split(" ")
results = ", ".join(array_products)

print(f"I have {results} in my shopping cart.")
```

### Task 2

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

s = set(a)

query = int(input())

for _ in range(query):
    q = tuple(input().split())
    if q[0] == "pop":
        s.pop()
    elif q[0] == "discard":
        s.discard(int(q[1]))
    elif q[0] == "remove":
        s.remove(int(q[1]))

print(sum(s))
```

### Task 3

```python
n = int(input())
i = 1

while i * i <= n:
    print(i * i)
    i += 1
```

### Task 4

```python
s = input()

counts = {}
for w in s.split():
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

print(counts)
```

### Task 5

```python
quiz = {
    "1. Which is the currency of Kazakhstan ? ": {"Tenge", "KZT"},
    "2. Name one of the past/present presidents of Kazakhstan: ": {"Nazarbayev", "Tokayev"},
    "3. What year Kazakhstan proclaim independence? ": "1991"
}

counter = 0
for question, answer in quiz.items():
    user_answer = input(question)
    if user_answer in answer:
        counter += 1

result_perc = (counter / len(quiz)) * 100
user_won = True if result_perc > 70 else False
if user_won:
    print(f"Congrats, you won with {result_perc:.2f}% correctness")
else:
    print(f"You lost! You got only {result_perc:.2f}% correctness")
```

### Task 6

```python
my_list = [(1,2), (2,3), (3,7), (4,16)]

mult_res = (x[0] * x[1] for x in my_list)
result = list(mult_res)

print(result)
```

### Task 7
```python
array = []
for i in range(1,100):
    if % 3 == 0:
        array.append(i)
print(array)
```

### Task 8
```python
arr2 = [100, "Astana", -10, 1, 10.4, True, 3, 4, 70, 24, -9, "Almaty", "Aktay"]
only_ints = []
list_of_string = []
float_nums = []
array_of_bools = []

for element in arr2:
    if type(element) == str:
        list_of_string.append(element)
    elif type(element) == int:
        only_ints.append(element)
    elif type(element) == float:
        float_nums.append(element)
    elif type(element) == bool:
        array_of_bools.append(element)
print(only_ints)
print(list_of_string)
print(float_nums)
print(array_of_bools)
```
### Task 9

```python
n = int(input())

names = set()
grades_sum = {}
grades_count = {}

for _ in range(n):
    name, grade = input().split(' ', 1)
    names.add(name)
    grades_sum[name] = grades_sum.get(name, 0) + int(grade)
    grades_count[name] = grades_count.get(name, 0) + 1

for name in names:
    print(name, grades_sum[name]/grades_count[name])
```

### Task 10

```python
word = input().lower()

number_of_letters = {}

for letter in word:
    if letter in number_of_letters:
        number_of_letters[letter] += 1
    else:
        number_of_letters[letter] = 1

for letter, count in number_of_letters.items():
    print(letter, count)
```

### Task 11

```
number: int = int(input('number: '))

for i in range(1, number + 1):
    message: str = ''
    if i % 15 == 0:
        message = 'FizzBuzz'
    elif i % 3 == 0:
        message = 'Fizz'
    elif i % 5 == 0:
        message = 'Buzz'
    else:
        message = i

    print(f'{message:>8}', end='')
    print(',' if i != number else '.', end=' ')

    if i % 10 == 0:
        print()
```

### Task 12

```
n: int = int(input())
arr: list = []

for i in range(n):
    pair: list = input().split(' ')
    key, value = pair[0], pair[1]

    if key == 'str':
        arr.append(value)
    elif key == 'bool':
        arr.sort(reverse=bool(value))
    elif key == 'int':
        index: int = int(value)
        if 0 > index >= len(arr):
            continue

        arr = arr[index:]
    elif key == 'set':
        arr.append(value)
        arr = list(set(arr))
    else:
        arr.insert(0, key)
        arr.append(value)

print(arr)
```

### Task 13

### Task 14
