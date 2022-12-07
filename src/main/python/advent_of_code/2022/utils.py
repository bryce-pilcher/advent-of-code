import os.path
from contextlib import contextmanager


@contextmanager
def get_file(filename: str):
    file = None
    try:
        file = open(os.path.join(os.path.dirname(__file__), 'resources', filename), 'r', newline='')
        yield file
    finally:
        file.close()
