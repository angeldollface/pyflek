# PY FLEK by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

from pyflek import *

def test_all():
    """
    Tests all of the functions that
    Py Flek provides.
    """
    subject = list('abcd')
    item = 'b'
    print(get_rand_item(list('abcd')))
    print(get_item_index(subject, item))
    print(conv_to_num("2"))
    print(get_char_pos("d"))
    print(get_char_space("d", "v"))
    print(get_num_space("1","2"))
    print(string_type("a"))
    print(string_type("1"))
    print(string_type("@"))
    print(is_num("a"))
    print(is_num("2"))
    print(password_strength("1969HoglinSteak"))
    print(password_strength("1969HoglinSteak_@@"))
    print(is_secure("1969HoglinSteak"))
    print(is_secure("1969HoglinSteak_@@"))
    print(generate_password(16))

def main():
    test_all()

if __name__ == '__main__':
    main()
