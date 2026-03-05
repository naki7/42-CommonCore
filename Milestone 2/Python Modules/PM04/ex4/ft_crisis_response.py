def main() -> None:
    file_arr: list[str] = ["lost_archive.txt", "classified_vault.txt",
                           "standard_archive.txt"]
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    for file_name in file_arr:
        try:
            with open(file_name, "r") as file:
                text: str = file.read()
            print(f"ROUTINE ACCESS: Attempting access to {file_name}...")
            print(f"SUCCESS: Archive recovered - ``{text}''")
            print("STATUS: Normal operations resumed\n")
        except FileNotFoundError:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")
        except Exception as alert:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
            print(f"RESPONSE: Unusual compilication encountered '{alert}'")
            print("STATUS: Crisis handled, complication managed\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
