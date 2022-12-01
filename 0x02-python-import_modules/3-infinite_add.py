#!/usr/bin/python3
import sys

if __name__ == "__main__":
    result = 0

    for arg in sys.argv:
        if arg != sys.argv[0]:
            result += int(arg)

    print(result)
