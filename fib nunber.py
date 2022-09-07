fib_list = [0, 1]


def get_next_fib_num(previous2, previous1):
    return previous2 + previous1


def get_fibs(limit):
    len_of_fib_list = len(fib_list)
    max_entry = max(fib_list)
    if max_entry < limit:
        next_fib_num = get_next_fib_num(fib_list[len_of_fib_list - 2], fib_list[len_of_fib_list - 1])
        fib_list.append(next_fib_num)
        get_fibs(limit)
    return fib_list


euler_limit = 12586269025

print(sum(filter(lambda x: x < euler_limit, get_fibs(euler_limit))))