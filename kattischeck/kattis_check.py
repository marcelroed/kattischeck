from kattischeck.fetch_data import get_unzipped_file
from kattischeck.run_script import script_paths
from kattischeck.run_script import run_script
from kattischeck.compare_output import compare
from pathlib import Path
from colorama import init
from colorama import Fore, Style


def kattis_check(problem_names):
    """
    Tests a local solutions for the given problem names with remote sample inputs and outputs.
    :param problem_names: A list of strings of problem names.
    :return:
    """
    init()
    print(Style.BRIGHT, end='')
    # For every problem
    implementations = script_paths(Path.cwd(), problem_names)
    for problem_name in problem_names:
        unzipped = get_unzipped_file('https://open.kattis.com/problems/' + problem_name + '/file/statement/samples.zip')
        samples = split_samples(unzipped)
        for implementation in sorted(implementations[problem_name]):
            print(Fore.YELLOW + implementation.stem + implementation.suffix)
            # Check every sample input and output with every implementation of the problem
            for sample_name, sample_input, sample_output in samples:
                print(Fore.WHITE + sample_name)
                sample_input, sample_output = [text_from_file(i) for i in [sample_input, sample_output]]
                local_output = run_script(implementation, sample_input)
                if local_output is None:
                    local_output = ''
                correct = compare(local_output, sample_output)
                if correct:
                    print(Fore.YELLOW, end='')
                    print(local_output)
                    print(Fore.GREEN + 'Test Passed')
                    print()
                else:
                    print(Fore.RED + 'Sample output: ')
                    print(Fore.RESET + sample_output)
                    print(Fore.RED + 'Local output: ')
                    print(Fore.RESET + local_output)
                    print(Fore.RED + 'Test Failed' + Fore.RESET)
                    print()
    print(Style.RESET_ALL)


def text_from_file(file):
    buffer = [line for line in file]
    return ''.join(buffer)


def split_samples(unzipped):
    problems = {}
    for filename, generator in unzipped:
        ext_idx = filename.rfind('.')
        ext = filename[ext_idx + 1:]
        name = filename[:ext_idx]
        existing = problems.get(name, [None, None])
        if ext == 'in':
            existing[0] = generator
        elif ext == 'ans':
            existing[1] = generator
        else:
            raise ValueError('Sample input not as expected')
        problems[name] = existing
    return [[sample_name, sample[0], sample[1]] for sample_name, sample in problems.items()]
