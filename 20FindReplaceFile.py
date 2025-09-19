def find_replace(filename, old_text, new_text):
    with open(filename, 'r') as file:
        content = file.read()
    
    updated_content = content.replace(old_text, new_text)
    
    with open(filename, 'w') as file:
        file.write(updated_content)
    
    print(f"Replaced '{old_text}' with '{new_text}' in {filename}")

# Usage
find_replace('claude.txt', 'Current', 'Now')