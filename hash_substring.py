# python3

import sys

import sys

def read_input():
    choice = input("Input choice I or F (for input from keyboard or from file): ")
    if choice == "I":
        text = input("Enter the text string: ")
        pattern = input("Enter the pattern string: ")
        return text, pattern
    elif choice == "F":
        with open("tests/06", "r") as file1, open("tests/06.a", "r") as file2:
            text = file1.read().strip()
            pattern = file2.read().strip()
            return text, pattern
    else:
        print("Invalid choice")
        return None






def print_occurrences(output):
    """
    Prints the list of occurrences in the required format.
    """
    print(' '.join(map(str, output)))

def rabin_karp(pattern, text):
    """
    Rabin-Karp algorithm for searching pattern in text.
    Returns a list of starting indices of matches found in text.
    """
    # Set prime number and modulus for hashing function
    prime = 101
    modulus = 2**32
    
    n = len(text)
    m = len(pattern)
    
    # Calculate hash values for pattern and first substring of text
    pattern_hash = 0
    substring_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * prime + ord(pattern[i])) % modulus
        substring_hash = (substring_hash * prime + ord(text[i])) % modulus
    
    # Check if pattern matches first substring of text
    indices = []
    if pattern_hash == substring_hash and pattern == text[:m]:
        indices.append(0)
    
    # Calculate hash values for remaining substrings of text and compare with pattern hash
    for i in range(m, n):
        substring_hash = (substring_hash * prime - ord(text[i-m]) * pow(prime, m, modulus) % modulus + ord(text[i])) % modulus
        if pattern_hash == substring_hash and pattern == text[i-m+1:i+1]:
            indices.append(i-m+1)
    
    return indices



# this part launches the functions
if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = rabin_karp(pattern, text)
    print_occurrences(occurrences)
