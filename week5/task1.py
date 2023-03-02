import re

from text_paypal import text_paypal

user_str = input("Write keyword:")
should_look_for_start = bool(int(input("Should look for start?")))
should_look_for_end = bool(int(input("Should look for end?")))
should_look_for_digits = bool(int(input("Should look for digits?")))

text = re.split('\.', text_paypal)

if should_look_for_start:
    user_str = '^' + user_str
if should_look_for_end:
    user_str = user_str + '$'


print(user_str)

print('Matched sentences:')
for sentence in text:
    if re.search(user_str, sentence):

        is_digit_found = False

        if should_look_for_digits:
            is_digit_found = bool(re.search('\d', sentence))
        
        if not should_look_for_digits or is_digit_found:
            print(sentence)
