def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_itereative(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range (2, n + 1):
        result *= i
    return result

def compare_performance(n):
    import time

    #recursive
    start = time.time()
    rec_result = factorial_recursive(n)
    rec_time = time.time() - start

    #iterative
    start = time.time()
    iter_result = factorial_itereative(n)
    iter_time = time.time() - start

    print(f"\n{n}! = {rec_result}")
    print(f"Recursive: {rec_time:.4f}s")
    print(f"Iterative: {iter_time:.4f}s")
    print(f"Iterative is {rec_time/iter_time:.1f}x faster")


def main():
    print("------------------- FACTORIAL CALCULATOR -------------------")

    test_nums = [5, 10, 15, 30]

    for num in test_nums:
        try:
            print(f"\nTesting {num}:")
            print(f"Recursive: {factorial_recursive(num)}")
            print(f"Iterative: {factorial_itereative(num)}")
        except ValueError as e:
            print(f"Error: {e}")
        

    print("\n=== Performance Test ===")
    compare_performance(90)

    print("=== Try your own ===")
    while True:
        try:
            n = input("\nEnter a number (or 'q' to quit): ")
            if n.lower() == 'q':
                break
            n = int(n)
            print(f"Recursive: {factorial_recursive(n)}")
            print(f"Iterative: {factorial_itereative(n)}")
        except ValueError as e:
            print(f"Error: {e}")
        except RecursionError:
            print("Number too large for recursive approach!")

if __name__ == "__main__":
    main()
