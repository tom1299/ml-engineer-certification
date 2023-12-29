import os
import shutil
import unittest

from file_processor import process_files, check_file_content
import tempfile

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
    return True

class TestFileProcessor(unittest.TestCase):
   
    def setUp(self):
        self.test_files_folder = tempfile.mkdtemp()
        self.create_test_files()
    
    def test_file_processor(self):
        file_extensions = ['yml', 'yaml', 'env']
        for file_extension in file_extensions:
            pattern = os.path.join(self.test_files_folder, '**/*.' + file_extension)
            process_files(pattern, [process_file1, process_file2], is_valid_file)
        
    def tearDown(self):
        shutil.rmtree(self.test_files_folder)
        
    def create_test_files(self):
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir1'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir2'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir3'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_1'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_2'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir2', 'sub_dir2_1'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir2', 'sub_dir2_2'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir3', 'sub_dir3_1'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir3', 'sub_dir3_2'))

        with open(os.path.join(self.test_files_folder, 'file1.yml'), 'w') as file:
            file.write(os.path.join(self.test_files_folder, 'file1.yml'))
        
        with open(os.path.join(self.test_files_folder, 'sub_dir3', 'file2.yaml'), 'w') as file:
            file.write(os.path.join(self.test_files_folder, 'sub_dir3', 'file2.yaml'))
            
        with open(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_1', 'file3.env'), 'w') as file:
            file.write(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_1', 'file3.env'))
            
        with open(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_2', 'file4.txt'), 'w') as file:
            file.write(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_2', 'file4.txt'))
    
class TestCheckFileContent(unittest.TestCase):
   
    def setUp(self):
        self.test_files_folder = tempfile.mkdtemp()
        self.create_test_files()
    
    def test_check_file_content(self):
        self.assertTrue(check_file_content(os.path.join(self.test_files_folder, 'file1.yml'), ['file1.yml']))
        self.assertTrue(check_file_content(os.path.join(self.test_files_folder, 'sub_dir3', 'file2.yaml'), ['file2.yaml']))
        self.assertTrue(check_file_content(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_1', 'file3.env'), ['file3.env']))
        self.assertFalse(check_file_content(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_2', 'file4.txt'), ['file4.txt']))
        
    def tearDown(self):
        shutil.rmtree(self.test_files_folder)
        
    def create_test_files(self):
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir1'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir2'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir3'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_1'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_2'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir2', 'sub_dir2_1'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir2', 'sub_dir2_2'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir3', 'sub_dir3_1'))
        os.mkdir(os.path.join(self.test_files_folder, 'sub_dir3', 'sub_dir3_2'))

        with open(os.path.join(self.test_files_folder, 'file1.yml'), 'w') as file:
            file.write(os.path.join(self.test_files_folder, 'file1.yml'))
        
        with open(os.path.join(self.test_files_folder, 'sub_dir3', 'file2.yaml'), 'w') as file:
            file.write(os.path.join(self.test_files_folder, 'sub_dir3', 'file2.yaml'))
            
        with open(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_1', 'file3.env'), 'w') as file:
            file.write(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_1', 'file3.env'))
            
        with open(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_2', 'file4.txt'), 'w') as file:
            file.write(os.path.join(self.test_files_folder, 'sub_dir1', 'sub_dir1_2', 'file5.txt'))
            
if __name__ == '__main__':
    unittest.main()        
