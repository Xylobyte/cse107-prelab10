"""
This program...

File: sieve.py

Authors: Donovan Griego and Haley Dietz

Date: 10-25-2021

Assignment: Prelab10
"""


def sieve(user_input):
    """
    Pupose: Function that calculates the primes from 1 to a user_input using the sieve of Eratosthenes algorithm
    Argument:
        user_input: A number
    """

    primes = []
    nums = []
    # Create list of numbers from 2 to user_input
    for i in range(2, int(user_input)):
        nums.append(i)
    # Loop until our created list is empty
    while len(nums) > 0:
        # Add number being checked as a prime
        primes.append(nums[0])
        n = nums[0]
        del nums[0]
        j = 0
        # Check for and remove any multiples of the prime being checked
        while j < len(nums):
            if nums[j] % n == 0:
                del nums[j]
            j += 1
    # Add 1 as a prime and return primes found
    return [1] + primes


def main():
    primes = sieve(int(input("Enter a number: ")))
    print("Primes: {}".format(primes))


if __name__ == "__main__":
    main()
