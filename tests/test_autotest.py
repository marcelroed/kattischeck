from kattis_autotest.fetch_data import get_zip_file, unzip
from kattis_autotest.run_script import run_script, script_paths
import os


class TestFetchData:
    def test_fetch_zip(self):
        data_url = 'https://open.kattis.com/problems/doorman/file/statement/samples.zip'
        data = get_zip_file(data_url)
        files = unzip(data)


class TestRunScript():
    def test_run_local(self):
        script_path = os.path.curdir + '/aaah.py'
        result = run_script(script_path, 'aaah\naah')
        print(result)
        assert result == 'go\n'

    def test_find_paths(self):
        paths = script_paths('aaah')
        print(paths)
