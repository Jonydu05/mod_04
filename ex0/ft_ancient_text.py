import sys

if __name__ == "__main__":
    if not sys.argv[1:]:
        print("Usage: ft_ancient_text.py <file>")
        exit(0)
    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    print(f"Acessing file '{file_name}'")
    try:
        with open(file_name, "r") as file:
            print(f"---\n\n{file.read()}\n\n---")
            file.close()
            print(f"File {file_name} closed.")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
