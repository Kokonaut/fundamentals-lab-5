from os import listdir
from os.path import isfile, join


def get_files_in_path(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files.sort()
    return files
