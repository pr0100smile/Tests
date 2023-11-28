import unittest

from ya_folder import create_folder, folder_info

FOLDERNAME = 'folder_test'

class TestFolderYa(unittest.TestCase):
    def test_create_folder(self):
        result = create_folder(FOLDERNAME)
        self.assertEqual(result == 201, f'Результат: {result}')

def test_folder_info(self):
    self.assertEqual(folder_info(FOLDERNAME) == 'dir')