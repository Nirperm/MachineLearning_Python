import unittest
from reader import Reader


class TestSeaquenceFunction(unittest.TestCase):

    def test_wc(self):
        file_name = 'data/KEN_ALL.CSV'
        wc = Reader(file_name)
        wc.read_file()
        self.assertEqual(len(wc.file_data), 123721)


if __name__ == '__main__':
    unittest.main()
