from sys import executable
from subprocess import check_output, CalledProcessError
from os import listdir


def run_script(script_path, input_str):
    file_ext = script_path.suffix
    if file_ext == '.py':
        return run_python(script_path, input_str)
    elif file_ext == '.cpp':
        return run_cpp(script_path, input_str)
    else:
        return


def run_python(script_path, input_str):
    output = check_output([executable, str(script_path.resolve())],
                          input=input_str,
                          universal_newlines=True)
    return output


def run_cpp(cpp_path, input_str):
    # Compile using gcc
    absolute_path = cpp_path.resolve()
    try:
        check_output(['g++', str(absolute_path), '-o', 'problem'])
    except CalledProcessError as e:
        raise ValueError(e.output)
    # Run binary with parameters
    output = check_output(['problem.exe'],
                          input=input_str,
                          universal_newlines=True)
    (cpp_path.parent / 'problem.exe').unlink()
    return output


def script_paths(root, problem_names):
    """
    Returns a list of pairs (problem_name, path)
    :param root: A path object directing to root
    :param problem_names: An array of problem names to fetch the path of
    :return:
    """
    problem_files = {}
    dir_files = listdir(root)
    for problem_name in problem_names:
        for filename in dir_files:
            if problem_name in filename:
                problem_files[problem_name] = problem_files.get(problem_name, []) + [root / filename]
    return problem_files
