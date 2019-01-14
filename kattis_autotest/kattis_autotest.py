from kattis_autotest.fetch_data import get_samples
from kattis_autotest.compare_output import compare
from kattis_autotest.local_script import run_script, find_implementations


def test_problems(problem_names):
    """
    Tests a local solutions for the given problem names with remote sample inputs and outputs.
    :param problem_names: A list of strings of problem names.
    :return:
    """
    # For every problem
    for problem_name in problem_names:
        samples = get_samples(problem_name)
        implementations = find_implementations(problem_name)
        for sample_input, sample_output in samples:
            # Check every sample input and output with every implementation of the problem
            for implementation in implementations:
                local_output = run_script(implementation, sample_input)
                compare(local_output, sample_output)
