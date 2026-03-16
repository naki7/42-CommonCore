def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name: str = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    try:
        archive = open(file_name, "x")
    except FileExistsError:
        archive.close()
        print("\nERROR: Discovery has already been found. Create a new one.\n")
        print("Data NOT preserved.")
        return
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    data_entries: dict[int: str] = {
        1: "New quantum algorithm discovered",
        2: "Efficiency increased by 347%",
        3: "Archived by Data Archivist trainee"
        }
    for entry in data_entries:
        archive.write(f"[ENTRY 00{entry}] {data_entries[entry]}")
        if entry != 3:
            archive.write("\n")
        print(f"[ENTRY 00{entry}] {data_entries[entry]}")
    archive.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
