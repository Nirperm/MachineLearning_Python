import unittest
from forward_viterbi import ForwardViterbi
from backward_viterbi import BackwardViterbi


class TestSeaquenceFunction(unittest.TestCase):

    def test_word_count(self):
        model_name = 'data/unigram_model'
        file_name = 'data/04-input.txt'
        fviterbi = ForwardViterbi(model_name, file_name)
        fviterbi.forward_process()

        print('=' * 30)

        bviterbi = BackwardViterbi(model_name, file_name)
        bviterbi.backward_process()

if __name__ == '__main__':
    unittest.main()
