import json
from datetime import datetime

def write_entry(entry):
    timestamp = datetime.now().isoformat()
    with open('entries.json', 'a') as file:
        json.dump({'timestamp': timestamp, 'entry': entry}, file)
        file.write('\n')

def read_entries():
    entries = []
    try:
        with open('entries.json', 'r') as file:
            for line in file:
                entry = json.loads(line)
                entries.append(entry)
    except FileNotFoundError:
        pass
    return entries

def main():
    while True:
        print("\n1. Write an entry")
        print("2. View all entries")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            entry = input("Write your diary entry: ")
            write_entry(entry)
            print("Entry added successfully!")

        elif choice == '2':
            entries = read_entries()
            if entries:
                print("\n--- Your Entries ---")
                for entry in entries:
                    print(f"{entry['timestamp']}: {entry['entry']}")
            else:
                print("No entries found.")

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
