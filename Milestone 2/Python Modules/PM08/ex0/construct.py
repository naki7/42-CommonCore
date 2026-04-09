import sys
import os
import site


def main() -> None:
    print("\nMATRIX STATUS: ", end="")
    if sys.prefix == sys.base_prefix:
        print("You're still plugged in")
    else:
        print("Welcome to the construct")
    path: list = site.getsitepackages()
    print(f"\nCurrent Python: {sys.executable}")
    if os.environ.get('VIRTUAL_ENV') is None:
        print(f"Virtual Environment: {os.environ.get('VIRTUAL_ENV')} detected")
        print("\nWARNING: You're in the global environment!",
              "The machines can see everything you install.\n",
              "To enter the construct, run:",
              "python3 -m venv matrix_env",
              "source matrix_env/bin/activate # On Unix",
              "matrix_env\\Scripts\\activate  # On Windows\n",
              "Then run this program again.", sep="\n")
    else:
        path_partition: tuple = path[0].partition("matrix_env")
        env_path: str = f"{path_partition[0]}{path_partition[1]}"
        print(f"Virtual Environment: {path_partition[1]}")
        print(f"Environment Path: {env_path}")

        print("\nSUCCESS: You're in an isolated environment!\n",
              "Safe to install packages without affecting\nthe global system.",
              sep="")

        print(f"\nPackage installation path: {path[0]}")


if __name__ == "__main__":
    main()
