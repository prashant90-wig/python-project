def make_space():
    print("\n" * 3)

def read_file(filename):
    with open(filename, "r") as file:
        content = file.readlines()
    return content

def reverse_content(content):
    return content[::-1]

def write_file(filename, content):
    with open(filename, "w") as file:
        file.writelines(content)

def create_test_file():
    test_content = """Pranish Joshi
    Prashant Joshi
    Padam Joshi
    Shanti Bhatta
    Goma Joshi
"""
    with open("test.txt", "w") as file:
        file.write(test_content)
    print("Test file 'test.txt' created.")

def main():
    make_space()
    print("===== File Reverser =====")
    create_test_file()

    lines = read_file("test.txt")
    print(f"Original Lines : {len(lines)} lines.")

    make_space()
    reversed_lines = reverse_content(lines)
    write_file('reversed_test.txt', reversed_lines)
    print("Done! Check 'reversed_test.txt'")

    print("\n Original:")
    for line in lines:
        print(f":{line.strip()}")

    print("\n Reversed:")
    for line in reversed_lines:
        print(f":{line.strip()}")

if __name__ == "__main__":  
    main()