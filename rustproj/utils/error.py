import sys


def throw_error(msg):
    print(f"\033[91mError: {msg}\033[m")
    sys.exit()