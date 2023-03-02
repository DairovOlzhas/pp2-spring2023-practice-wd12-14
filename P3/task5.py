

a = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

is_float = lambda x : isinstance(x, float)
is_str = lambda x : isinstance(x, str)

print(is_float(1))


def count_if(a, condition):
    cnt = 0
    for i in a:
        if condition(i):
            cnt += 1
    return cnt

print(count_if(a, is_str))
print(count_if(a, is_float))
