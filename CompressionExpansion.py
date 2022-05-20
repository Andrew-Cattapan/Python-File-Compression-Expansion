"""This program assesses how strong a password is.

This program accepts a password from the user and checks if it has at least 16 characters, a capital letter, lowercase letter, and a number.
Then, the password is tested against all the words in a dictionary and 10,000,000 commonly used passwords.
Finally, it is compared to any passwords already entered by the user.

"""


import os
import sys


def get_input():
    """Get password from user.
    
    Args:
        None
        
    Returns:
        Password to be tested or nothing to exit the program.
    """
    print("Please enter a password or press <Enter> to quit:")
    password = str(input())
    print("You entered: " + str(password))
    return password


def check_password_length(password):
    """Checks that teh password is longer than 16 characters.
    
    Args:
        password: the password entered by the user.

    Returns:
        "Pass" if longer than or equal to 16 characters.
        "Fail" if shorter then 16 characters.

    Raises:
        AssertionError: If password is not a string.
    """
    assert isinstance(password, str)
    if len(password) >= 16:
        answer = "Pass"
    elif len(password) < 16:
        answer = "Fail"
    return answer


def check_string_has_one_of(tested, password):
    """Checks if a string has at least one of the charcters in tested.

    Args:
        password: the password entered by the user.

    Returns:
        "Pass" if the password has at least one number.
        "Fail" if the password has no numbers.
    
    Raises:
        AssertionError: If tested is not a string.
        AssertionError If tested is not at least one character.
        AssertionError: If password is not a string.
    """
    assert isinstance(tested, str), "String tested must be a string."
    assert len(tested) >= 1, "String tested must be at least one character."
    assert isinstance(password, str), "Password must be a string."
    tested = str(tested)
    string_count = 0
    while string_count < len(password):
        if check_character_is_part_of(tested, password[string_count]) == True:
            answer = "Pass"
            return answer
        elif check_character_is_part_of(tested, password[string_count]) == False:
            answer = "Fail"
        else:
            answer = "Unknown Error"
        string_count = string_count + 1
    return answer


def check_character_is_part_of(tested, password_character):
    """Checks if a character is a letter.

    Args:
        password_character: the character to be tested.
        tested: the string looped through to see if password_character is one of them.

    Returns:
        'True' if the character is a part of the string and False if it is not.
    
    Raises:
        AssertionError: If password_character is not a string.
        AssertionError: If password_character is more than one character.
        AssertionError: If tested is not a string.
        AssertionError: If tested is not at least one character.
    """
    assert isinstance(password_character, str), "Input must be a string."
    assert len(password_character) <= 1, "String character must only be one character."
    assert isinstance(tested, str), "Tested must be a string."
    assert len(tested) >= 1, "Tested must be at least one character."
    tested = str(tested)
    character_tested = 0
    while character_tested < len(tested):
        if password_character == tested[character_tested]:
            answer = True
            break
        else:
            answer = False
        character_tested = character_tested + 1
    return answer


def password_strength(password):
    """Checks if password has at least 16 characters, a capital letter, lowercase letter, and a number.
    
    Args:
        password: Password entered by the user.

    Returns:
        A number 1-5 depending on how many tests it passes.

    Raises:
        AssertionError: If password is not a string.
    """
    assert isinstance(password, str), "Password must be a string."
    strength = 0
    NUMBERS = "0123456789"
    CAPITAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    SEPARATORS = "`~!@#$%^&*()_+-=[]{};:'<>,./?"

    if check_password_length(password) == "Pass":
        strength = strength + 1
    if check_password_length(password) == "Fail":
        print("'" + password + "' should have at least 16 characters.")

    if check_string_has_one_of(NUMBERS, password) == "Pass":
        strength = strength + 1
    if check_string_has_one_of(NUMBERS, password) == "Fail":
        print("'" + password + "' should have at least one number.")
    
    if check_string_has_one_of(CAPITAL_LETTERS, password) == "Pass":
        strength = strength + 1
    if check_string_has_one_of(CAPITAL_LETTERS, password) == "Fail":
        print("'" + password + "' should have at least one capital letter.")
    
    if check_string_has_one_of(LOWERCASE_LETTERS, password) == "Pass":
        strength = strength + 1
    if check_string_has_one_of(LOWERCASE_LETTERS, password) == "Fail":
        print("'" + password + "' should have at least one lowercase letter.")

    if check_string_has_one_of(SEPARATORS, password) == "Pass":
        strength = strength + 1
    if check_string_has_one_of(SEPARATORS, password) == "Fail":
        print("'" + password + "' should have at least one special character: `~!@#$%^&*()_+-=[]{};:'<>,./?")
    
    return strength


def check_if_in_file(filename, password):
    """Reads a list of words or passwords and compares each word/password to the password entered by the user.

    Args:
        filename: File to open and read.
        password: Password to test against individual words in the dictionary.

    Returns:
        None

    Raises:
        AssertionError: If filename is not a string.
        AssertionError: If the file cannot be reached exists.
        AssertionError: If the password is not a string.
    """
    assert isinstance(filename, str), "Password must be a string."
    assert os.path.isfile(filename), "File cannot be found."
    assert isinstance(password, str), "Password must be a string."
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if str(line) == (password):
                return "Match"


def create_file(filename, password):
    """Creates a user password file.

    Args:
        filename: Filename to create.
        password: Password entered by the user.

    Returns:
        None

    Raises:
        AssertionError: If filename is not a string.
        AssertionError: If the password is not a string.
    """
    assert isinstance(filename, str), "Password must be a string."
    assert isinstance(password, str), "Password must be a string."
    with open(filename, "w") as file:
        file.write(str(password) + "\n")
    

def append_file(filename, password):
    """Appends the next password to the file.

    Args:
        filename: Filename to open and append.
        password: Password entered by the user.

    Returns:
        None
    
    Raises:
        AssertionError: If filename is not a string.
        AssertionError: If the file cannot be reached exists.
        AssertionError: If the password is not a string.
    """
    assert isinstance(filename, str), "Password must be a string."
    assert os.path.isfile(filename), "File cannot be found."
    assert isinstance(password, str), "Password must be a string."
    with open(filename, "a") as file:
        file.write(password + "\n")
        return "Success"


def main():
    """Runs main program logic."""
    while True:
        password = get_input()
        if password == "":
            break
        if check_string_has_one_of(" ", password) == "Pass":
            print("Password should not have spaces.")
            continue
        strength = password_strength(password)
        print("Your password has " + str(strength) + " out of 5 strength.")
        try:
            filename = "words.txt"
            if check_if_in_file(filename, password) == "Match":
                print("'" + str(password) + "' is susceptible to a dictionary attack. Try using a different word.")
            filename = "10 million password list.txt"
            if check_if_in_file(filename, password) == "Match":
                print("'" + str(password) + "' is in the top 10,000,000 password list. Try using a different password.")
            filename = "user passwords.txt"
            if os.path.isfile(filename):
                if check_if_in_file(filename, password) == "Match":
                    print("You entered: '" + str(password) + "' before. Try using a different password.")
                else:
                    append_file(filename, password)
            else:
                create_file(filename, password)
        except:
            print("Unexpected error.")
            print("Error:", sys.exc_info()[1])
            print("File: ", sys.exc_info()[2].tb_frame.f_code.co_filename) 
            print("Line: ", sys.exc_info()[2].tb_lineno)
    print("Program terminated.") 
    sys.exit()


if __name__ == "__main__":
    main()
