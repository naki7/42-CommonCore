import alchemy
from alchemy import __version__, __author__


def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    direct_list: list = [
        alchemy.elements.create_fire,
        alchemy.elements.create_water,
        alchemy.elements.create_earth,
        alchemy.elements.create_air
    ]
    for element in direct_list:
        function_name: str = element.__name__
        function_result: str = element()
        print(f"alchemy.elements.{function_name}(): {function_result}")

    print("\nTesting package-level access (controlled by __init__.py):")
    package_list: list = [
        alchemy.create_fire,
        alchemy.create_water
    ]
    for element in package_list:
        function_name: str = element.__name__
        function_result: str = element()
        print(f"alchemy.{function_name}(): {function_result}")

    function_name: str = "create_earth"
    try:
        function_result: str = alchemy.create_earth()
    except AttributeError:
        function_result: str = "AttributeError - not exposed"
    print(f"alchemy.{function_name}(): {function_result}")
    function_name: str = "create_air"
    try:
        function_result: str = alchemy.create_air()
    except AttributeError:
        function_result: str = "AttributeError - not exposed"
    print(f"alchemy.{function_name}(): {function_result}")

    print("\nPackage metadata:")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")


if __name__ == "__main__":
    main()
