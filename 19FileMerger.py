def make_space():
    print("\n" *2)

def create_test_file():
    file1_content = """
Prashant Joshi
"""
    file2_content = """ 
Pranish Joshi"""

    file3_content = """
Shanti Bhatta"""

    with open("file1.txt", "w") as f:
        f.write(file1_content)

    with open("file2.txt", "w") as f:
        f.write(file2_content)

    with open("file3.txt", "w") as f:
        f.write(file3_content)
    
    print("Created test files: file1.txt, file2.txt, file3.txt")

def read_single_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Warning: {filename} not found!")
        return []
    
def read_multiple_files(filenames):
    all_contents = []

    for filename in filenames:
        print(f"Reading {filename}...")
        file_content = read_single_file(filename)
        all_contents.extend(file_content)
    return all_contents

    
def add_file_headers(filenames):
    all_contents = []

    for filename in filenames:
        print(f"Reading {filename}...")
        file_content = read_single_file(filename)

        if file_content:
            header = f"\n=== Content from {filename} ===\n"
            all_contents.append(header)
            all_contents.extend(file_content)

    return all_contents

def write_merged_file(filename, content):
    with open(filename, "w") as f:
        f.writelines(content)
    print(f"Merged content written to {filename}")

def show_preview(content, max_lines=10):
    print(f"\nPreview of merged content ({len(content)} total lines) :")
    for i, line in enumerate(content[:max_lines]):
        print(f"{i+1}: {line.strip()}")

    if len(content) > max_lines:
        print(f".. and {len(content) - max_lines} more lines.")

def main():
    make_space()
    print("=== File Merger ===")

    create_test_file()
    make_space()

    files_to_merge = ["file1.txt", "file2.txt", "file3.txt"]    
    merged_content = read_multiple_files(files_to_merge)
    write_merged_file("merged_simple.txt", merged_content)
    show_preview(merged_content)

    make_space()

if __name__ == "__main__":
    main()