"""
Write a function that checks if a string is a palindrome, ignoring spaces
and case, only consider alphabetic characters for the comparison. The funct
"""


def echo_validator(text: str) -> bool:
    text = text.lower()
    # text = text.replace(" ", "")
    text = [char for char in text if char.isalpha() is True]
    if not text:
        return False
    i = 0
    while i < len(text) - i:
        if text[i] != text[len(text) - 1 - i]:
            return False
        i += 1
    return True


def main() -> None:
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("hello"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator(""))
    print(echo_validator("r4cec4r"))


main()
