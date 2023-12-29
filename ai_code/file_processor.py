import glob
import os

def check_file_content(filename, terms):
    with open(filename, 'r') as file:
        content = file.read()
        for term in terms:
            if term not in content:
                return False
        return True

def process_files(glob_pattern, file_processors, file_selector):
    for filename in glob.glob(glob_pattern, recursive=True):
        if file_selector(filename):
            for file_processor in file_processors:
                if not file_processor(filename):
                    break
