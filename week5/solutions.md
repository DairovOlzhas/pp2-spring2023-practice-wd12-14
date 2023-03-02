### Task 1

```python
import re
from text_paypal import text_paypal

def search_input():
    user_string = input("Please write the keyword which we should search: ")
    has_starts_symbol = input("It looks for sentences where it starts with user input: ")
    has_ends_symbol = input("It looks for sentences where it ends with user input: ")
    has_digits = input("It contains a number in it? ")


    texts = [x.strip() for x in re.split('\.', text_paypal)]

    # 3 options
    if has_starts_symbol.lower() == 'true':
        user_string = '^' + user_string

    if has_ends_symbol.lower() == 'true':
        user_string = user_string+ '$'

    match_digits = True
    if has_digits.lower() == 'false':
        match_digits = False


    for text in texts:
        matched_input = re.search(user_string, text)
        # checks each text if it matched with digit's containings
        if matched_input and (match_digits == bool(re.search('\d', text))):
            print(matched_input.string) # text
```

### Task 2

### Task 3

```python
import re


def is_valid_email(email):
    username_and_domain = email.split('@')
    if len(username_and_domain) != 2:
        return False
    username, domain = username_and_domain

    username_pattern = r'^\w+([\.-]?\w+)*$'
    domain_pattern = r'^\w+([\.-]?\w+)*\.\w{2,3}$'

    if re.match(username_pattern, username) and re.match(domain_pattern, domain):
        return True
    else:
        return False


# Test the function with some example email addresses
print(is_valid_email("example@example.com"))  # Output: True
print(is_valid_email("example@example.co.uk"))  # Output: True
print(is_valid_email("example.example.com"))  # Output: False
print(is_valid_email("example@example"))  # Output: False
print(is_valid_email("example@example@.com"))  # Output: False
```

### Task 4

### Task 5

```python
import re
from data import restaurants, ids

def get_restaurants(restaurants):
    prev = 0
    counter = 0
    rests = {}
    obj = {}
    for k, v in restaurants.items():
        # get index of restaurant
        i = int(re.findall("\d+", k)[0])
        # if we got next restaurant data
        if i != prev:
            # save current restaurant's data
            rests[counter] = dict(zip(obj.keys(), obj.values()))
            # or
            # rest_dict = {}
            # for k, v in obj.items():
            #     rest_dict[k] = v
            # rests[counter] = rest_dict
            obj.clear()
            prev = i
            counter += 1
        obj_key = re.sub("\d+\_", "", k)
        if obj_key in ids:
            obj[obj_key] = v
    rests[counter] = dict(zip(obj.keys(), obj.values()))

    return rests


rests = get_restaurants(restaurants)

for i in range(len(rests)):
    print(f'Restaurant #{i+1}')
    for k, v in rests[i].items():
        print(f'{k}: {v}')
```

### Task 6

### Task 7

```python
import re
from text import text

unwanted_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "()", "(", ")", "-", "_", "+", "=", "'", "|",
                       "/", ":", ">", "<", ".", ",", "s", "?", "`", "~", "]" ,"["]
for index in range(len(text)):
    for character in unwanted_characters:
        if character in text[index]:
            text[index] = text[index].replace(f"{character}", " ").lower()

def delete_whitespaces(x):
    #Начало вашего кода
    result = re.sub(r'\s+',' ', x).rstrip()
    return result

correct_text = list(map(delete_whitespaces, text))
print(correct_text)
```

### Task 8

### Task 9

### Task 10

### Task 11

```python
import re
from movies import movies

regex = r"(?:^|,\s?)(?=[^\"]?)\"?((?:[^\"]*|[^,\"]*))\"?(?=,\s?|$)"

all_movies = re.findall(regex, movies)

print('The default regular expresion is any symbol')
print('Enter `exit` to finish or `list` to see all movies')
while True:
    command = input('Enter a regular expression (or press ENTER to use the default`): ')

    if command == 'exit':
        break

    if command == 'list':
        print('\n'.join(all_movies))
        continue

    regex = command if command else '.*'

    r = re.compile(regex)
    found_movies = list(filter(r.match, all_movies))

    if found_movies:
        print(f'found {len(found_movies)} movie(s): {found_movies[0]}, ...')
    else:
        print('Not found any movie')

print('Exit...')
```

### Task 12

### Task 13

### Task 14
