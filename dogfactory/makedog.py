import argparse

parse = argparse.ArgumentParser()
args = parse.parse_args()

# Commandline flags for dogfactory package
parse.add_argument('-l', '--large',
                   help='Create a large dog.', action='store_true')
parse.add_argument('-s', '--small',
                   help='Create a small dog.', action='store_true')