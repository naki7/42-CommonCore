"""
Write a function that checks if brackets [], parentheses (), and braces {} are
properly
balanced and correctly nested in a string. All others characters are ignored.
Return True if balanced, False otherwise
"""


def bracket_validator(s: str) -> bool:
    bracket_holder = []
    for char in s:
        if char == '[' or char == '(' or char == '{':
            bracket_holder.append(char)
        elif char == ']':
            if bracket_holder[len(bracket_holder) - 1] != '[':
                return False
            else:
                bracket_holder.pop(len(bracket_holder) - 1)
        elif char == ')':
            if bracket_holder[len(bracket_holder) - 1] != '(':
                return False
            else:
                bracket_holder.pop(len(bracket_holder) - 1)
        elif char == '}':
            if bracket_holder[len(bracket_holder) - 1] != '{':
                return False
            else:
                bracket_holder.pop(len(bracket_holder) - 1)
    if len(bracket_holder) > 0:
        return False
    else:
        return True


def main() -> None:
    print(bracket_validator("()"))
    print(bracket_validator("()[]{}"))
    print(bracket_validator("(]"))
    print(bracket_validator("([)]"))
    print(bracket_validator("{[]}"))
    print(bracket_validator("hello(world)[test]{code}"))
    print(bracket_validator("((()))"))
    print(bracket_validator("((())"))
    print(bracket_validator(""))


if __name__ == "__main__":
    main()
