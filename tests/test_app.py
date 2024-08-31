import os
import sys

VALID_COLORS = {'white', 'black', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta'}

def validate_color():
    color = os.getenv('PAGE_COLOUR', 'white')
    if color not in VALID_COLORS:
        print(f"Invalid color: {color}. Must be one of: {', '.join(VALID_COLORS)}")
        sys.exit(1)
    else:
        print(f"Valid color: {color}")

if __name__ == "__main__":
    validate_color()
