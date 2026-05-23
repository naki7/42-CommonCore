"""
Write a function that mirrors a 2D matrix horizontally by reversing each row.
"""


def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for column in matrix:
        column.reverse()
    return matrix


def main() -> None:
    print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))
    print(mirror_matrix([[1, 2], [3, 4], [5, 6]]))
    print(mirror_matrix([[7]]))
    print(mirror_matrix([[1, 2, 3, 4]]))
    print(mirror_matrix([[-1, -2], [-3, -4]]))


if __name__ == "__main__":
    main()
