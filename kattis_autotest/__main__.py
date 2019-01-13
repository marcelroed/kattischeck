import argparse
import sys

vprint = None


def main(args=sys.argv[1:]):
    # Parse args
    parser = parse_args(args)
    # Setup verbose printing, can call vprint()
    global vprint
    verbose = True
    vprint = print if verbose else lambda *a, **k: None


def parse_args(args):
    parser = argparse.ArgumentParser(description="Check Kattis solution")
    parser.add_argument(...)
    return parser.parse_args(args)
