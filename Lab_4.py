import os

while True:
    file_path = input("Enter the path to the file: ")

    if not os.path.exists(file_path):
        print("File not found!")
        continue

    with open(file_path, 'r') as file:
        content = file.readlines()

    
    total_lines = len(content)
    empty_lines = content.count('\n')
    lines_with_h = sum('h' in line for line in content)
    h_count = sum(line.count('h') for line in content)
    lines_with_will = sum('will' in line for line in content)

    print(f"\nFile: {file_path}")
    print(f"total lines: {total_lines}")
    print(f"empty lines: {empty_lines}")
    print(f"lines with \"h\": {lines_with_h}")
    print(f"\"h\" count: {h_count}")
    print(f"lines with \"will\": {lines_with_will}")

    answer = input("Do you want to analyze another file? (y/n): ")
    if answer.lower() != 'y':
        break