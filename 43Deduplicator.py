def deduplicate(lst):
    """Remove duplicates, keeps order"""

    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def main():
    test = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8]
    print(f"Original: {test}")
    print(f"Deduplicated: {deduplicate(test)}")

if __name__ == "__main__":
    main()