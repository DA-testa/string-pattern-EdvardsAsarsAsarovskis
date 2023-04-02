# python3



import sys

import os

def read_input():
    input_format = input().upper().rstrip()
    if 'F' in input_format:
        input_file = '06'
        input_file = "tests/" + input_file
        if 'a' not in input_file:
            try:
                with open(input_file, "r") as f:
                    pattern = f.readline().rstrip()
                    text = f.readline().rstrip()
            except FileNotFoundError:
                return "File not found error"

    elif input_format == 'I':
        pattern = input().rstrip()
        text = input().rstrip()

    return pattern, text


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
