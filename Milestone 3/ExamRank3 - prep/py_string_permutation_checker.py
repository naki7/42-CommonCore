"""
Write a function that determines if two strings are permutations of each other.
Two strings are permutations if they contain the same characters with the same
frequencies.
"""


def string_permutation_checker(s1: str, s2: str) -> bool:
    list_s1 = []
    for char in s1:
        list_s1.append(char)
    for char in s2:
        try:
            temp_i = list_s1.index(char)
            list_s1.pop(temp_i)
        except ValueError:
            return False
    if len(list_s1) == 0:
        return True
    return False


def main():
    print(string_permutation_checker("abc", "bca"))
    print(string_permutation_checker("abc", "def"))
    print(string_permutation_checker("listen", "silent"))
    print(string_permutation_checker("hello", "bello"))
    print(string_permutation_checker("", ""))
    print(string_permutation_checker("a", ""))
    print(string_permutation_checker("Abc", "abc"))
    print(string_permutation_checker("a gentleman", "elegant man"))


main()
