"""
Write a function that creates a simple cipher by shifting letters in a st
by a given amount. Non-alphabetic characters should remain unchanged.
"""


def whisper_cipher(text: str, shift: int) -> str:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_str = []
    for char in text:
        try:
            char_i = lowercase.index(char)
            if char_i + shift > len(lowercase) - 1:
                char_i = char_i - len(lowercase)
            new_str.append(lowercase[char_i + shift])
        except ValueError:
            try:
                char_i = uppercase.index(char)
                if char_i + shift > len(uppercase) - 1:
                    char_i = char_i - len(uppercase) - 1
                new_str.append(uppercase[char_i + shift])
            except ValueError:
                new_str.append(char)
    return "".join(new_str)


def main():
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("Hello World!", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("ABC123def", 5))
    print(whisper_cipher("", 10))
    print(sorted([1, 3, 7, 2, 4, 6, 0]))


main()
