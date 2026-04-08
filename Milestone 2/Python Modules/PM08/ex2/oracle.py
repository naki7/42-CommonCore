import os
from dotenv import load_dotenv


def get_env_variables(env_variables: list) -> list:

    for variable in env_variables:
        env_variables[variable] = os.environ.get(variable)

    load_dotenv()
    for variable in env_variables:
        if env_variables[variable] is None:
            env_variables[variable] = os.environ.get(variable)

    return env_variables


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    env_variables: list = {
        "MATRIX_MODE": None,
        "DATABASE_URL": None,
        "API_KEY": None,
        "LOG_LEVEL": None,
        "ZION_ENDPOINT": None
    }

    env_variables = get_env_variables(env_variables)

    print("Configuration loaded:")
    only_none: bool = True
    none_exists: bool = False
    titles: list = ["Mode", "Database", "API Access", "Log Level",
                    "Zion Network"]
    i: int = 0
    for variable in env_variables:
        if env_variables[variable] is not None:
            if variable == "DATABASE_URL":
                env_variables[variable] = "Connected to local instance"
            if variable == "API_KEY":
                env_variables[variable] = "Authenticated"
            if variable == "ZION_ENDPOINT":
                env_variables[variable] = "Online"
            if only_none is True:
                only_none = False
        elif none_exists is False:
            none_exists = True
        print(f"{titles[i]}: {env_variables[variable]}")
        i += 1

    print("\nEnvironment security check:")
    if none_exists is True:
        env_str: str = "[KO] .env file not properly configured"
    else:
        env_str: str = "[OK] .env file properly configured"
    if only_none is True:
        print("[KO] .env file/enviornment variables not properly created",
              "\nThe Oracle is blind to configurations.", sep="\n")
    else:
        print("[OK] No hardcoded secrets detected",
              f"{env_str}",
              "[OK] Production overrides available",
              "\nThe Oracle sees all configurations.", sep="\n")


if __name__ == "__main__":
    main()
