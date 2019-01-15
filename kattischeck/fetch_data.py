from urllib.request import urlopen, Request
from io import BytesIO
from zipfile import ZipFile


def get_zip_file(url):
    # Make a real request, so that Python is allowed to scrape.
    req = Request(url, headers={'User-Agent': "Chrome Browser"})
    # Get the response
    resp = urlopen(req)
    zip_file = ZipFile(BytesIO(resp.read()))
    return zip_file


def unzip(zip_file):
    """
    Returns a list of [name, file_stream] for every file in the zip.
    :param zip_file: A ZipFile to read from
    :return: List of [name, file_stream]
    """
    name_list = zip_file.namelist()
    return list(zip(name_list, [[line for line in decode(zip_file.open(file_name).readlines())] for file_name in
                                zip_file.namelist()]))


def decode(byte_str_generator):
    return (line.decode('UTF-8') for line in byte_str_generator)


def get_unzipped_file(url):
    return unzip(get_zip_file(url))
