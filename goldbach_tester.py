def is_prime(num):
    """
    Checks if a number is prime or not.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_sum(num):
    """
    Checks if an even number can be expressed as the sum of two prime numbers.
    """
    if num <= 2 or num % 2 != 0:  # Odd numbers cannot be the sum of two primes
        return None
    for i in range(2, num // 2 + 1):  # Check up to half of the number
        if is_prime(i) and is_prime(num - i):
            return (i, num - i)
    return None

print("Goldbach's Conjecture Test Options:")
print("1. Test from 4 × 10¹⁸ to Infinity")
print("2. Test within a Specific Range")

choice = int(input("Choose your option (1 or 2): "))

with open("found.txt", "w") as f:  # Open the file in write mode
    if choice == 1:
        start = 4 * 10**18
        while True:
            for i in range(start, start + 1000000, 2):  # Check 1 million numbers at a time
                result = prime_sum(i)
                if not result:
                    f.write(str(i) + "\n")  # Write the disproving number to the file
                    print(f"Goldbach's Conjecture is false for {i}. Result written to found.txt")
                    exit()  # Exit the program if a counterexample is found
            start += 1000000  # Move to the next million numbers
    elif choice == 2:
        start = int(input("Enter the starting even number (at least 4): "))
        while start % 2 != 0 or start < 4:
            print("Please enter an even number greater than or equal to 4.")
            start = int(input("Enter the starting even number (at least 4): "))

        end = int(input("Enter the ending even number: "))
        while end % 2 != 0 or end < start:
            print("Please enter an even number greater than the starting number.")
            end = int(input("Enter the ending even number: "))

        for i in range(start, end + 1, 2):
            result = prime_sum(i)
            if result:
                print(f"{i} can be expressed as the sum of {result[0]} and {result[1]}")
            else:
                f.write(str(i) + "\n")  # Write the disproving number to the file
                print(f"Goldbach's Conjecture is false for {i}. Result written to found.txt")
                exit()  # Exit the program if a counterexample is found
    else:
        print("Invalid choice!")
