import unittest

from evaluater import Evaluater
from model import Model
from reader import Reader
from train_unigram import TrainUnigram
from writer import Writer


class TestClass(unittest.TestCase):

    def test_word_count(self):
        file_name = 'data/01-train-input.txt'
        reader = Reader(file_name)
        reader.read_file()
        unigram = TrainUnigram(reader.word_list, reader.total_word_count)
        unigram.train_unigram()

        file_name = 'data/unigram_model'
        write_model = Writer(file_name, unigram.word_dict)
        write_model.write_file()
        model = Model(file_name)
        model.read_model()

        file_name = 'data/01-test-input.txt'
        test = Evaluater(file_name, model.word_dict)
        test.evaluate_model()

        print('entropy is ' + str(test.H / test.total_word_count))
        print('coverage is ' + str(1.0 * (test.total_word_count - test.unknown_word_count) / test.total_word_count))


if __name__ == "__main__":
    unittest.main()
