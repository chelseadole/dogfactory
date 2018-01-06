"""Package logic and flags for dogfactory package."""
import argparse

parser = argparse.ArgumentParser()

# Commandline flags for dogfactory package
parser.add_argument('-l', '--large',
                    help='Create a large dog.', action='store_true')
parser.add_argument('-s', '--small',
                    help='Create a small dog.', action='store_true')

args = parser.parse_args()


def large():
    """Large dog flag."""
    return 'BORK!'


def small():
    """Small dog flag."""
    return 'yip!'


def main():
    """Commandline for makedog."""
    if args.large:
        return large()
    if args.small:
        return small()
    else:
        return '~ d o g    c r e a t e d ~'
