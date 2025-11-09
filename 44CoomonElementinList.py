def find_common(list1, list2, list3):
    """Find elements that appear in all 3 lists"""
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    common = set1 & set2 & set3  # & means intersection
    return list(common)

def main():
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    c = [4, 5, 6, 7, 8]
    
    print(f"List 1: {a}")
    print(f"List 2: {b}")
    print(f"List 3: {c}")
    print(f"Common: {find_common(a, b, c)}")
    
    # Test with strings
    friends1 = ["Ram", "Shyam", "Hari"]
    friends2 = ["Hari", "Sita", "Gita"]
    friends3 = ["Hari", "Ram", "Krishna"]
    
    print(f"\nMutual friends: {find_common(friends1, friends2, friends3)}")

if __name__ == "__main__":
    main()