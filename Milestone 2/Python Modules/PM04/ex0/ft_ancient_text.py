def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name: str = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file_name}")
    try:
        archive = open(file_name, "r")
    except FileNotFoundError:
        print("\nERROR: Storage vault not found. Run data generator first.\n")
        print("Data recovery failed.")
        return
    print("Connection established...\n")
    print("RECOVERED DATA:")
    fragments: str = archive.read()
    print(fragments)
    archive.close()
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
