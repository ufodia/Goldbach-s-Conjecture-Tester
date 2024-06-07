# Goldbach's Conjecture Tester

This Python script tests the validity of Goldbach's Conjecture, which states that every even integer greater than 2 can be expressed as the sum of two prime numbers.

## How It Works

1. **Prime Number Check (`is_prime`)**:
   - The `is_prime` function efficiently determines if a given number is prime.
   - It uses optimizations for divisibility by 2 and 3, and then checks divisibility by 6k ± 1.

2. **Goldbach's Sum Check (`prime_sum`)**:
   - The `prime_sum` function takes an even number as input.
   - It iterates through potential prime numbers up to half the input number.
   - If it finds two prime numbers that sum up to the input, it returns them.
   - If no such pair is found, it returns `None`.

3. **Testing Options:**
   - The script provides two testing options:
     - **Option 1:** Tests all even numbers starting from 4 × 10¹⁸, continuing indefinitely. This starting point is chosen because Goldbach's Conjecture has been verified for all even numbers up to 4 × 10¹⁸ through extensive computational efforts.
     - **Option 2:** Tests even numbers within a user-specified range.

4. **Disproving Goldbach's Conjecture:**
   - If the script finds a counterexample (an even number that cannot be expressed as the sum of two primes), it writes that number to a file named "found.txt" and exits.

## Usage

1. **Clone or download this repository.**
2. **Run the script from your terminal:**
   ```bash
   python goldbach_tester.py 

3. **Choose a testing option (1 or 2).**
4. **If you choose Option 2, enter the desired start and end even numbers.**
5. **Observe the output:**
    - If a counterexample is found, it will be printed to the console and written to "found.txt".
    - Otherwise, the script will either continue indefinitely (Option 1) or finish testing the specified range (Option 2).

## Disclaimer
This script is a computational tool for testing Goldbach's Conjecture.  While it has not been proven false, it's important to note that this script cannot definitively prove the conjecture to be true.

## Contributing
Feel free to fork this repository and contribute improvements or optimizations.

## License
This project is licensed under the MIT License.

## Donate: 
**BTC**: `1DDus3a5DnugwXkWdVMSYcH1tZ2jMYXfi1`
