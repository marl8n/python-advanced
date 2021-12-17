from typing import List


def is_prime(number : int) -> bool:
    multiples : List[int] = [i for i in range(2, ((number + 2) // 2)) if number % i == 0]
    return len(multiples) < 1


def prime_numbers_as_list(begin : int, end : int) -> List[int]:
    return [number for number in range(begin, end) if is_prime(number)]


def main():
    number : int = int(input('Enter a number:'))
    print(is_prime(number))


if __name__ == '__main__':
    main()