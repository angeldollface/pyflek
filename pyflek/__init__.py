# PY FLEK by Alexander Abraham a.k.a. "Angel Dollface".
# Licensed under the MIT license.

import random
from random import Random

# Security weight.
security_weight = 3

# The weight a special character has.
special_char_weight = 3

# The weight an arabic character has.
arabic_character_weight = 2

def get_rand_item(subject):
    """
    Get a random item from a string vector.
    """
    return random.choice(subject)

def conv_to_num(char):
    """
    Convert string to a number.
    """
    result = 0
    if is_num(char) == True:
        result = int(char)
    else:
        """
        DO NOTHING.
        """
    return result

def get_item_index(subject, item):
    """
    Get index of a list item and return it.
    """
    result = 0
    for i,j in enumerate(subject):
        if j == item:
            result = i
        else:
            """
            Do nothing.
            """
    return result

def clean_split(subject, split_char):
    """
    Splits a string array by a character and returns the resulting array.
    """
    return subject.split(split_char)

def get_char_pos(char):
    """
    Get the character position from a list.
    """
    result: usize = 0
    alphabet =  'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = list(alphabet)
    for letter in alphabet_list:
        if letter == char:
            result = get_item_index(alphabet_list, letter)
        else:
            """
            Do nothing.
            """
    return result

def get_char_space(char_one, char_two):
    """
    Get the distance between two characters.
    """
    char_one_index = get_char_pos(char_one)
    char_two_index = get_char_pos(char_two)
    result = 0
    if char_one_index > char_two_index:
        """
        Do nothing.
        """
    else:
        result = char_two_index - char_one_index
    return result

def get_num_space(num_one, num_two):
    """
    Get the space between two numbers.
    """
    result = 0
    if conv_to_num(num_one) > conv_to_num(num_two):
        """
        Do nothing.
        """
    else:
        result = conv_to_num(num_two) - conv_to_num(num_one)
    return result

def string_type(char):
    """
    Get the type of string.
    """
    result = "int"
    if is_num(char) == False:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_list = list(alphabet)
        if char in alphabet_list:
            result = "normChar"
        else:
            result = "specialChar"
    else:
        """
        Do nothing.
        """
    return result

def is_num(char):
    """
    Check if a string is a number or not.
    """
    result = False
    if char.isnumeric():
        result = True
    else:
        """
        Do nothing.
        """
    return result

def password_strength(password):
    """
    Computes the strength of a password.
    """
    result = 0
    char_list = list(password)
    for item in char_list:
        current_item = item
        current_item_type = string_type(item)
        current_index = get_item_index(char_list, item)
        previous_item_index = 0
        if current_index == 0:
            """
            Do nothing.
            """
        else:
            previous_item_index = current_index - 1
        previous_item = char_list[previous_item_index]
        previous_item_type = string_type(previous_item)
        if current_item_type == "normChar" and previous_item_type == "normChar":
            item_space = get_char_space(current_item, previous_item)
            if item_space > security_weight:
                result = result + arabic_character_weight
            else:
                """
                Do nothing.
                """
        elif current_item_type == "specialChar" and previous_item_type == "specialChar":
                result = result + special_char_weight
        elif current_item_type == "int" and previous_item_type == "int":
            itemSpace = get_num_space(current_item, previous_item)
            if itemSpace > security_weight:
                result = result + arabic_character_weight
            else:
                """
                Do nothing.
                """
        else:
            """
            Do nothing.
            """
    return result

def is_secure(password):
    """
    Simplified strenght measure.
    """
    result = False
    if password_strength(password) > 8:
        result = True
    else:
        """
        Do nothing.
        """
    return result

def generate_password(length):
    """
    Generate a random password.
    """
    result_list = []
    alphabet_string = "abcdefghijklmnopqrstuvwxyz1234567890@_.:"
    alphabet_list = list(alphabet_string)
    range_end = length + 1
    for i in range(1,range_end):
        rand_char = get_rand_item(alphabet_list)
        result_list.append(rand_char)
    result = ''.join(result_list)
    return result