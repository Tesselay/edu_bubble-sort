def find_smallest_index(numbers):
    smallest_val: int = min(numbers)
    return numbers.index(smallest_val)


def iteration(numbers, iterator):
    try:
        if numbers[iterator] > numbers[iterator + 1]:
            first_val = numbers[iterator]
            second_val = numbers[iterator + 1]
            numbers[iterator] = second_val
            numbers[iterator + 1] = first_val
        else:
            iterator += 1
    except IndexError:
        iterator = 0

    return numbers, iterator


def bubble_sort(numbers):
    iterator: int = 0

    smallest_index = find_smallest_index(numbers)
    takeout = numbers.pop(smallest_index)
    numbers.append(takeout)

    while find_smallest_index(numbers) != 0:
        numbers, iterator = iteration(numbers, iterator)

    return numbers
