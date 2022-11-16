# PY FLEK :gear: :snake:

![GitHub CI](https://github.com/angeldollface/pyflek/actions/workflows/python.yml/badge.svg)

***Test the strength of your passwords with the Doll algorithm. :gear: :snake:***

## ABOUT :books:

This is my Python implementation of a package I wrote in [Dart](https://github.com/angeldollface/securitycheck), [ECMA Script](https://github.com/angeldollface/vulcheck), and [Rust](https://github.com/angeldollface/flek). These packages all do one thing: They provide functions for you to check whether your passwords are secure or not. They implement an algorithm  of my own design. It gives your password a score and if the score is higher than eight, then the password is deemed to be secure. Why *Py Flek*? The name is a combination of the words *Py*thon *Fl*aw Ch*e(c)k*. Enjoy. :heart:

## USAGE :hammer:

### REQUIREMENTS

You should have the following tools installed and available from the command line:

- [Git](https://git-scm.org)
- [Python 3.5+](https://www.python.org/downloads/)
- Pip for Python 3.5+ (Usually comes with Python.)

### INSTALLING *PY FLEK* ON YOUR SYSTEM

To use *Py Flek* on your own system with your own projects, run the following command:

```bash
python -m pip install git+https://github.com/angeldollface/pyflek
```

### IMPORTING *PY FLEK*

To import *Py Flek*'s functions into your Python code, add this line to the top of your code:

```python
from pyflek import *
```

### API

- `get_rand_item(subject)`: Get a random item from a string array.
- `conv_to_num(char)`: Convert string to int.
- `get_item_index(subject, item)`: Get index of a list item and return it.
- `clean_split(subject, split_char)`: Splits a string array by a character and returns the resulting array.
- `get_char_pos(char)`: Get the character position from a list.
- `get_char_space(char_one, char_two)`: Get the distance between two characters.
- `get_num_space(num_one, num_two)`: Get the distance between two numbers.
- `string_type(char)`: Get the type of a string.
- `is_num(char)`: Check if a string is a number or not.
- `password_strength(password)`: Computes the strength of a password.
- `is_secure(password)`: Simplified strenght measure. Returns a boolean depending on whether the security score is above or below eight.
- `generate_password(length)`: Generate a random password.
- `test_all()`: Test all the above methods.

### TEST THE EXAMPLE

To test the included example in the folder `example`, execute the following steps:

- 1.) Clone this repository to your machine:

```bash
git clone https://github.com/angeldollface/pyflek
```

- 2.) Change directory into the repository's root:

```bash
cd pyflek
```

- 3.) Change directory into the `example` folder:

```bash
cd example
```

- 4.) Install the example's dependencies:

```bash
python -m pip install -r requirements.txt
```

- 5.) Run the example:

```bash
python main.py
```

## CHANGELOG :black_nib:

### Version 1.0.0

- Initial release.
- Upload to GitHub.

## NOTE :scroll:

- *Py Flek :gear: :snake:* by Alexander Abraham :black_heart: a.k.a. *"Angel Dollface" :dolls: :ribbon:*
- Licensed under the MIT license.
