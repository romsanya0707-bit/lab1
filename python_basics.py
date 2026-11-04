"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    text = data.value
    return (text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u') +
         text.count('A') + text.count('E') + text.count('I') + text.count('O') + text.count('U'))


def has_unique_characters(data: TextInput) -> bool:
    seen_symbols = []
    for symbol in data:
        if symbol in seen_symbols:
            return False
        seen_symbols.append(symbol)
    return True


def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    s = 0
    while number > 0:
        s = s + (number % 2)
        number = number // 2
    return s


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    s = 0
    while number > 9:
        a = 1
        c = number
        while c > 0:
            b = c % 10
            a = a * b
            c = c // 10
        number = a
        s = s + 1
    return s


def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    n = 0
    for x in predicted:
        n = n + 1
    s = 0
    i = 0
    while i < n:
        k = (predicted[i] - expected[i]) * (predicted[i] - expected[i])
        s = s + k
        i = i + 1
    return s / n


def prime_factorization(data: PositiveIntegerInput) -> str:
    n = data
    divisor = 2
    result = ""
    while n > 1:
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor
        if count > 0:
            if count == 1:
                result += f"({divisor})"
        else:
            result += f"({divisor}**{count})"
        divisor += 1

    return result


def pyramid(data: PositiveIntegerInput) -> int | str:
        cubes = data
        k = 1
        while cubes >= k ** 2:
            cubes -= k ** 2
            k += 1
        if cubes == 0:
            return k - 1
        else:
            return "It is impossible"


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    n = 0
    c = number
    while c > 0:
        n = n + 1
        c = c // 10
    k = (n - 1) // 2
    s2 = 0
    i = 0
    while i < k:
        s2 = s2 + (number % 10)
        number = number // 10
        i = i + 1
    a = n - 2 * k
    i = 0
    while i < a:
        number = number // 10
        i = i + 1
    s1 = 0
    i = 0
    while i < k:
        s1 = s1 + (number % 10)
        number = number // 10
        i = i + 1
    if s1 == s2:
        return True
    else:
        return False

