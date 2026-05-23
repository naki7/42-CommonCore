"""
Write a function that converts a number from one
base to another.
Support bases from 2 to 36 inclusive, using
digits 0-9 and letters A-Z for values 10-35.
Return "ERROR" for invalid inputs (base, digits)
"""


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    if not (number):
        return "ERROR"

    decimal_val = 0
    for char in number:
        try:
            curr_val = base.index(char)
        except ValueError:
            return "ERROR"
        if curr_val >= from_base:
            return "ERROR"

        decimal_val = decimal_val * from_base + curr_val

    result = []
    while decimal_val > 0:
        result.append(base[decimal_val % to_base])
        decimal_val //= to_base

    return "".join(reversed(result))


def main() -> None:
    result: str = number_base_converter("1010", 2, 10)
    print(result)
    result: str = number_base_converter("FF", 16, 10)
    print(result)
    result: str = number_base_converter("255", 10, 16)
    print(result)
    result: str = number_base_converter("123", 10, 2)
    print(result)
    result: str = number_base_converter("Z", 36, 10)
    print(result)
    result: str = number_base_converter("35", 10, 36)
    print(result)
    result: str = number_base_converter("123", 1, 10)
    print(result)
    result: str = number_base_converter("G", 16, 10)
    print(result)


if __name__ == "__main__":
    main()
