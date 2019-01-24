from kattischeck.fetch_data import get_zip_file, unzip
from kattischeck.run_script import run_script, script_paths
from kattischeck.kattis_check import kattis_check
from kattischeck.compare_output import compare
from pathlib import Path

def is_tool(name):
            """Check whether `name` is on PATH and marked as executable."""
            # from whichcraft import which
            from shutil import which

            return which(name) is not None


class TestRunScript:
    def test_run_python(self):
        if not is_tool('python'):
            return
        script_path = Path() / 'aaah.py'
        result = run_script(script_path, 'aaah\naah')
        print(result)
        assert compare(result, 'go\n')

    def test_run_cpp(self):
        if not is_tool('g++'):
            return
        script_path = Path() / 'testproblem.cpp'
        result = run_script(script_path, '1 4')
        compare(result, '5')

    def test_find_paths(self):
        root = Path()
        paths = script_paths(root, ['aaah', '10typesofpeople', 'testproblem'])
        print(paths)

    def test_run_both(self):
        root = Path()
        problem_name = 'testproblem'
        paths = script_paths(root, [problem_name])
        filenames = paths.get(problem_name, [])
        print(filenames)
        results = ['3']
        for path in filenames:
            results += run_script(path, '1 2')
        for i in range(len(results) - 1):
            assert compare(results[i], results[i + 1])


class TestFetchData:
    def test_fetch_zip(self):
        data_url = 'https://open.kattis.com/problems/doorman/file/statement/samples.zip'
        data = get_zip_file(data_url)
        files = unzip(data)
        print(files)


class TestKattisAutotest:
    def test_all(self):
        problem_names = ['doorman']
        results = kattis_check(problem_names)
