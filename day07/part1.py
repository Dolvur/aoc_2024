from typing import Callable, List


def add(a: int, b: int):
    return a + b


def mult(a: int, b: int):
    return a * b


def can_match(
    sum: int,
    result: int,
    terms: List[int],
    possible_operations: List[Callable[[int, int], int]] = [add, mult],
):
    if len(terms) == 0:
        return result == sum

    for operation in possible_operations:
        next_value = terms[0]
        local_sum = operation(sum, next_value)
        if can_match(local_sum, result, terms[1:], possible_operations):
            return True

    return False


if __name__ == "__main__":
    file = open("input.txt", "r")
    input = file.read()
    file.close()

    lines = input.splitlines()
    total_sum = 0
    for line in lines:
        result, rest = line.split(":")
        result = int(result)
        terms = [int(elem) for elem in rest.split(" ")[1:]]
        if can_match(terms[0], result, terms[1:]):
            total_sum += result

    print(total_sum)
