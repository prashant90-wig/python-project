import random

urls = {}

def make_short_code():
    letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    code = ""
    for i in range(4):
        random_letter = random.choice(letters)
        code = code + random_letter 
    return code

def shorten_url(long_url):
    short_code = make_short_code()
    urls[short_code] = long_url
    return short_code

def get_original_url(short_code):
    if short_code in urls:
        return urls[short_code]
    else:
        return print("URL not found!")
    

def show_all_urls():
    if len(urls) == 0:
        print("No URLS stored yet!")
        return
    print("\nAll stored URLS:")
    for short_code in urls:
        original_url = urls[short_code]
        print(f"{short_code} -->  {original_url}")

def main():
    print("====== URL SHORTENER ======")
    while True:
        print("\n---Menu---\n")
        print("1. Shorten a URL")
        print("2. Get original URL")
        print("Show all URLs")
        print("4. Exit")

        choice = input("Enter your choice (1-4) :")

        if choice == "1":
            url = input("Enter URL to shorten: ")
            short_code = shorten_url(url)
            print(f"Your short code is : {short_code}")
            print(f"Short URL: https://tiny.ly/{short_code}")

        elif choice == "2":
            code = input("Enter your code: ")
            original = get_original_url(code)
            print(f"Original URL: {original}")
        
        elif choice == "3":
            show_all_urls()
        
        elif choice == "4":
            print("Goodbye!")
            break

        else:
            return "Invalid choice"


if __name__ == "__main__":
    main()