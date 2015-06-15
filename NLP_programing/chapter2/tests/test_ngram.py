import unittest
from evaluate_model import EvaluateModel
from reader import Reader
from train_ngram import TrainNgram
from writer import Writer
from read_ngram import ReadNgram


class TestSeaquenceFunction(unittest.TestCase):

    def test_word_count(self):
        file_name = 'data/02-train-input.txt'
        reader = Reader(file_name)
        reader.read_file()
        ngram = TrainNgram(reader.word_list, 3)
        ngram.train()

        print({k: v for k, v in ngram.word_dict.items()})
        print({k: v for k, v in ngram.lambda_word_dict.items()})

        file_name = 'data/ngram_model'
        writer_model = Writer(file_name, ngram.word_dict)
        writer_model.write_file()
        model = ReadNgram(file_name)
        model.read_model()

        file_name = 'data/02-train-input.txt'
        test = EvaluateModel(file_name, model.word_dict, ngram.lambda_word_dict)
        test.evaluate()
        print('entropy is ' + str(test.H / test.total_word_count))


if __name__ == "__main__":
    unittest.main()
