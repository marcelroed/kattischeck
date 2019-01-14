import argparse
import sys

vprint = None


def main(args=sys.argv[1:]):
    # Parse args
    parsed_args = parse_args(args)
    print(parsed_args)
    # Setup verbose printing, can call vprint()
    init_vprint(parsed_args.verbose)


def init_vprint(verbose):
    global vprint
    vprint = print if verbose else lambda *a, **k: None


def parse_args(args):
    parser = argparse.ArgumentParser(description="Check Kattis solution")
    parser.add_argument('problem_names', metavar='problem-name', help='the name of the problem(s)', type=str, nargs='+')
    parser.add_argument('--verbose', help='increase output verbosity', action='store_true')
    return parser.parse_args(args)


if __name__ == '__main__':
    main()
