N = int(input())
res = []
while N != 0:
    info = [x for x in map(str, input().split(','))]

    first_s = info[0][0].lower()  # первая буква имени
    count_s = list(map(chr, range(97, 123))).index(first_s) + 1  # по счёту буква в алфавите
    list_age = [i for i in info[3]] + [i for i in info[4]]
    age_sum = sum(list(map(int, list_age)))  # сумма символов месяца и дня

    count_set_name = 0
    for i in info:
        full_name = info[:3]
        count_set_name = len(set(''.join(full_name)))  # количество уникальных символов
    res.append(hex(count_set_name + (age_sum * 64) + (count_s * 256))[-3:].upper())
    N -= 1

print(*res, end=' ')
