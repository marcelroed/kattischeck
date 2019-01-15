import argparse
import sys
from kattischeck.kattis_check import kattis_check
from os import system
import platform

vprint = None


def main(args=sys.argv[1:]):
    # Parse args
    parsed_args = parse_args(args)
    # Setup verbose printing, can call vprint()
    init_vprint(parsed_args.verbose)
    if parsed_args.clear:
        os = platform.system()
        if os == 'Windows':
            system('cls')
        else:
            system('clear')
    kattis_check(parsed_args.problem_names)


def init_vprint(verbose):
    global vprint
    vprint = print if verbose else lambda *a, **k: None


def parse_args(args):
    parser = argparse.ArgumentParser(description="Check Kattis solution")
    parser.add_argument('problem_names', metavar='problem-name', help='the name of the problem(s)', type=str, nargs='+')
    parser.add_argument('--verbose', help='increase output verbosity', action='store_true')
    parser.add_argument('--clear', help='clear console window before running', action='store_true')
    return parser.parse_args(args)


if __name__ == '__main__':
    main()
