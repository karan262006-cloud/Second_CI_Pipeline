
def missing_number(numbers):
    n = len(numbers)
    result = n

    for i, number in enumerate(numbers):
        result ^= i ^ number

    return result
