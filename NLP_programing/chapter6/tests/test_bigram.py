import unittest
from train_bigram import TrainBigram
from writer import Writer
from evaluate_model import EvaluateModel
from reader import Reader
from model_reader import ModelReader


class TestSeaquenceFunction(unittest.TestCase):

    def test_wc(self):
        fileName = 'data/02-train-input.txt'
        reader = Reader(fileName)
        reader.file_Read()
        bigram = TrainBigram(reader.word_list)
        bigram.train()
        print({k: v for k, v in bigram.word_dict.items()})
        print({k: v for k, v in bigram.lambda_word_dict.items()})
        fileName = 'data/bigram_model'
        writemodel = Writer(fileName, bigram.word_dict)
        writemodel.write_file()
        model = ModelReader(fileName)
        model.read_model()
        fileName = 'data/02-train-input.txt'
        test = EvaluateModel(fileName, model.word_dict, bigram.lambda_word_dict)
        test.evaluate_model()
        print('entropy is ' + str(test.H / test.total_word_size))


if __name__ == "__main__":
    unittest.main()
