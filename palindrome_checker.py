def is_palindrome(number):
    """
    Check if a number is a palindrome.
    A palindrome number reads the same forwards and backwards.
    
    Args:
        number: The number to check (can be int or string)
    
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Convert the number to string to compare digits
    num_str = str(abs(number))  # Use abs() to handle negative numbers
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]


def main():
    print("=== Palindrome Number Checker ===\n")
    
    while True:
        try:
            # Get input from user
            user_input = input("Enter a number (or 'q' to quit): ")
            
            # Check if user wants to quit
            if user_input.lower() == 'q':
                print("Thank you for using the palindrome checker!")
                break
            
            # Convert input to integer
            number = int(user_input)
            
            # Check if it's a palindrome
            if is_palindrome(number):
                print(f"✓ {number} is a palindrome!\n")
            else:
                print(f"✗ {number} is NOT a palindrome.\n")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")


if __name__ == "__main__":
    main()