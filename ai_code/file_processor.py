import glob
import os

def process_file1(filename):
    print(f'Processing file with processor 1: {filename}')
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
    return True

def process_file2(filename):
    print(f'Processing file with processor 2: {filename}')
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
    return True

def is_valid_file(filename):
    # Add your selection logic here
    return True

def process_files(glob_pattern, file_processors, file_selector):
    for filename in glob.glob(glob_pattern, recursive=True):
        if file_selector(filename):
            for file_processor in file_processors:
                if not file_processor(filename):
                    break
