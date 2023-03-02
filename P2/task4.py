sentence = input()

count_of_each_word = {}

for word in sentence.split(' '):
    count_of_each_word[word] = count_of_each_word.get(word, 0) + 1
    # if word in count_of_each_word:
    #     count_of_each_word[word] += 1
    # else:
    #     count_of_each_word[word] = 1

for word, count in count_of_each_word.items():
    print(word, ':', count)

