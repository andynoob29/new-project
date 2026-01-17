def is_number_palindrome(number):
    """
    Check if a number is a palindrome.
    
    Args:
        number: The number to check (int)
    
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    num_str = str(abs(number))
    return num_str == num_str[::-1]


def is_word_palindrome(word):
    """
    Check if a word is a palindrome.
    Ignores case and spaces.
    
    Args:
        word: The word or phrase to check (string)
    
    Returns:
        bool: True if the word is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for comparison
    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]


def main():
    print("=== Palindrome Checker ===\n")
    print("This program can check if numbers or words are palindromes!")
    print("Examples: 121, 'radar', 'A man a plan a canal Panama'\n")
    
    while True:
        user_input = input("Enter a number or word (or 'q' to quit): ").strip()
        
        # Check if user wants to quit
        if user_input.lower() == 'q':
            print("Thank you for using the palindrome checker!")
            break
        
        if not user_input:
            print("Please enter something!\n")
            continue
        
        # Try to determine if input is a number or word
        try:
            # Try converting to integer
            number = int(user_input)
            if is_number_palindrome(number):
                print(f"✓ {number} is a palindrome number!\n")
            else:
                print(f"✗ {number} is NOT a palindrome number.\n")
        
        except ValueError:
            # It's not a number, treat as a word/phrase
            if is_word_palindrome(user_input):
                print(f"✓ '{user_input}' is a palindrome word!\n")
            else:
                print(f"✗ '{user_input}' is NOT a palindrome word.\n")


if __name__ == "__main__":
    main()