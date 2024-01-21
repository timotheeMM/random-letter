import random
import string

def get_random_letter(uppercase: bool = False) -> str:
    """
    Generate and return a random letter.

    Args:
        uppercase (bool, optional): If False, return a lowercase letter.
                                    If True, return an uppercase letter.
                                    Defaults to False.

    Returns:
        str: A random letter.
    """
    
    letters = string.ascii_uppercase if uppercase else string.ascii_lowercase
    random_letter = random.choice(letters)
    return random_letter
