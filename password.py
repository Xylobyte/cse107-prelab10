"""
This program uses regular expressions to check if a user inputted password
has at least one uppercase, one lowercase, and one number in it.

File: password.py

Authors: Donovan Griego and Haley Dietz

Date: 10-25-2021

Assignment: Prelab10
"""
import re


def passwordcheck(password):
    """
    Purpose: A function that checks the strength of a password using regular expression
    Argument:
        password: Password that user wants to check
    """
    # Checks length of password
    if len(password) < 8:
        return False
    else:
        # Checks for each condition separately
        cond1 = re.search(".*[A-Z].*", password)
        cond2 = re.search(".*[a-z].*", password)
        cond3 = re.search(".*[0-9].*", password)
        if cond1 and cond2 and cond3:
            return True
        else:
            return False


def main():
    password = input("Please enter a password: ")
    print("Success! The password given is strong!" if passwordcheck(
        password) else "Error: The password given is not strong enough")
    pass


if __name__ == "__main__":
    main()
