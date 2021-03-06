import unittest
from feature_reader import FeatureReader
from one_prediction import OnePrediction
from online_learning import OnlineLearning
from reader import Reader
from train_unigram import TrainUnigram
from writer import Writer


class TestSeaquenceFunction(unittest.TestCase):

    def test_word_count(self):
        file_name = 'data/01-train-input.txt'
        reader = Reader(file_name)
        reader.read_file()
        unigram = TrainUnigram(reader.word_list, reader.total_word_count)
        unigram.train()

        file_name = 'data/unigram_model'
        writemodel = Writer(file_name, unigram.word_dict)
        writemodel.write_file()

        file_name = 'data/03-train-input.txt'
        cfeature = FeatureReader(file_name)
        cfeature.read_feature()

        print({k: v for k, v in cfeature.feature_dict.items()})
        online = OnlineLearning(cfeature.feature_dict, unigram.word_dict, 'UNI:')
        online.online_learning()
        print({k: v for k, v in online.phi.items()})

        prediction = OnePrediction('data/03-train.txt', online.weight, online.phi, 'UNI:')
        prediction.predict()


if __name__ == "__main__":
    unittest.main()
