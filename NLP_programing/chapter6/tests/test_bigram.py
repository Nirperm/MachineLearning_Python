import unittest
from train_bigram import TrainBigram
from writer import Writer
from evaluate_model import EvaluateModel
from reader import Reader
from model_reader import ModelReader


class TestSeaquenceFunction(unittest.TestCase):

    def test_word_count(self):
        file_name = 'data/02-train-input.txt'
        reader = Reader(file_name)
        reader.read_file()

        bigram = TrainBigram(reader.word_list)
        bigram.train()

        print({k: v for k, v in bigram.word_dict.items()})
        print({k: v for k, v in bigram.lambda_word_dict.items()})

        file_name = 'data/bigram_model'
        writer = Writer(file_name, bigram.word_dict)
        writer.write_file()

        model = ModelReader(file_name)
        model.read_model()

        file_name = 'data/02-train-input.txt'
        test = EvaluateModel(file_name, model.word_dict, bigram.lambda_word_dict)
        test.evaluate_model()

        print('entropy is ' + str(test.H / test.total_word_count))


if __name__ == "__main__":
    unittest.main()
