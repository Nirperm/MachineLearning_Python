import unittest
from reader import Reader


class TestSeaquenceFunction(unittest.TestCase):

    def test_word_count(self):
        file_name = 'data/KEN_ALL.CSV'
        reader = Reader(file_name)
        reader.read_file()
        self.assertEqual(len(reader.data_list), 123721)


if __name__ == '__main__':
    unittest.main()
