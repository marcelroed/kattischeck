from sys import executable
from subprocess import check_output
from os import listdir
from os.path import curdir


def run_script(script_path, input_str):
    file_ext = script_path


def run_python(script_path, input_str):
    output = check_output([executable, script_path],
                          input=input_str,
                          universal_newlines=True)
    return output


def script_paths(problem_names):
    filenames = []
    for filename in listdir():
        if filename[:filename.rfind('.')] in problem_names:
            filenames.append(filename)
    return [curdir + '/' + filename for filename in filenames]
