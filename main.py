"""
Программа Влада
"""
def syracuse_sequence(n: int) -> list[int]:
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1
        sequence.append(n)

    # return sequence
    return conflict


def syracuse_max(n: int) -> int:
    sequence = syracuse_sequence(n)

    max_element = 1
    for element in sequence:
        if element > max_element:
            max_element = element

    return max_element

# улучшенный принт
def my_print(arg) -> None:
    print(arg)


if __name__ == '__main__':
    while True:
        line = input('Enter a syracuse sequence starting number: ')

        try:
            n = int(line)
        except ValueError:
            print('Incorrect input!')
            continue

        sequence = syracuse_sequence(n)
        max_element = syracuse_max(n)
        print('Sequence:', *sequence)
        print(f'Max element: {max_element}')
        break
